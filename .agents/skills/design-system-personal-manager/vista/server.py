#!/usr/bin/env python3
"""Vista local de solo lectura para los Markdown publicados de un sistema de diseño.

No crea, modifica ni borra archivos. Sirve la interfaz que vive junto a este
script y lee solo los documentos de la allowlist dentro de la carpeta indicada.
"""

from __future__ import annotations

import argparse
import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

STATIC = Path(__file__).resolve().parent / "static"
MAX_BYTES = 2_000_000
MEDIA_TYPES = {
    ".css": "text/css; charset=utf-8",
    ".gif": "image/gif",
    ".html": "text/html; charset=utf-8",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".webp": "image/webp",
}

# Solo estas categorías, en este orden. No se crean pestañas para carpetas
# detectadas ni para secciones sin documentos.
SECCIONES = (
    ("foundations", "Foundations"),
    ("tokens", "Tokens"),
    ("componentes", "Componentes"),
    ("changelog", "Changelog"),
    ("deuda", "Deuda y pendientes"),
    ("comandos", "Comandos"),
    ("convenciones", "Convenciones"),
    ("vocabulario", "Vocabulario"),
)
RAIZ_MD = (
    "changelog.md",
    "changelog-documentacion.md",
    "deuda.md",
    "comandos.md",
)
ORDEN_CHANGELOG = {
    "changelog.md": 0,
    "changelog-documentacion.md": 1,
}
SALTAR_DIRECTORIOS = {".git", "node_modules", "__pycache__"}
HEADING = re.compile(r"^#\s+(.+?)\s*$")


def normalizar(raiz: Path, relativa: str) -> str:
    if relativa.startswith(("/", "\\")) or "\\" in relativa:
        raise PermissionError(relativa)
    if not relativa:
        return ""
    raiz_resuelta = raiz.resolve()
    destino = (raiz_resuelta / relativa).resolve()
    if destino != raiz_resuelta and raiz_resuelta not in destino.parents:
        raise PermissionError(destino)
    return destino.relative_to(raiz_resuelta).as_posix()


def _partes_visibles(ruta: str) -> list[str] | None:
    partes = ruta.split("/")
    if any(not parte or parte.startswith(".") or parte in SALTAR_DIRECTORIOS for parte in partes):
        return None
    return partes


def es_md_publicado(ruta: str) -> bool:
    """Allowlist de Markdown relativo a la raíz documental."""
    if not ruta.endswith(".md"):
        return False
    partes = _partes_visibles(ruta)
    if partes is None:
        return False
    if len(partes) == 1:
        return partes[0] in RAIZ_MD
    if partes[0] != "guias":
        return False
    if len(partes) == 2:
        return partes[1] in {"convenciones.md", "vocabulario.md"}
    if len(partes) == 3 and partes[1] == "componentes":
        return True
    if partes[1] != "foundations":
        return False
    if len(partes) == 3:
        return True
    return len(partes) == 4 and partes[2] == "tokens"


def es_asset_publicado(ruta: str) -> bool:
    """Imágenes y otros archivos de las guías. Los Markdown van por la allowlist."""
    if not ruta or ruta.endswith(".md") or not ruta.startswith("guias/"):
        return False
    return _partes_visibles(ruta) is not None


def titulo_de(archivo: Path) -> str:
    try:
        with archivo.open("r", encoding="utf-8", errors="replace") as handle:
            for _ in range(40):
                linea = handle.readline()
                if not linea:
                    break
                coincide = HEADING.match(linea.strip())
                if coincide:
                    return coincide.group(1).strip()
    except OSError:
        pass
    return archivo.stem.replace("-", " ")


def seccion_de(ruta: str) -> str:
    partes = ruta.split("/")
    nombre = partes[-1]
    if len(partes) == 1 and nombre in {"changelog.md", "changelog-documentacion.md"}:
        return "changelog"
    if len(partes) == 1 and nombre == "deuda.md":
        return "deuda"
    if len(partes) == 1 and nombre == "comandos.md":
        return "comandos"
    if partes == ["guias", "convenciones.md"]:
        return "convenciones"
    if partes == ["guias", "vocabulario.md"]:
        return "vocabulario"
    if len(partes) >= 2 and partes[0] == "guias" and partes[1] == "componentes":
        return "componentes"
    if partes[0] == "guias" and partes[1] == "foundations" and (
        nombre == "tokens.md" or (len(partes) > 2 and partes[2] == "tokens")
    ):
        return "tokens"
    if len(partes) >= 2 and partes[0] == "guias" and partes[1] == "foundations":
        return "foundations"
    raise ValueError(ruta)


def candidatos(raiz: Path) -> list[Path]:
    hallados: list[Path] = []
    for nombre in RAIZ_MD:
        hallados.append(raiz / nombre)
    guias = raiz / "guias"
    if not guias.is_dir():
        return hallados
    for nombre in ("convenciones.md", "vocabulario.md"):
        hallados.append(guias / nombre)
    componentes = guias / "componentes"
    if componentes.is_dir():
        hallados.extend(componentes.glob("*.md"))
    foundations = guias / "foundations"
    if foundations.is_dir():
        hallados.extend(foundations.glob("*.md"))
        tokens = foundations / "tokens"
        if tokens.is_dir():
            hallados.extend(tokens.glob("*.md"))
    return hallados


def listar_paginas(raiz: Path) -> list[dict[str, str]]:
    paginas = []
    if not raiz.is_dir():
        return paginas
    for archivo in candidatos(raiz):
        if not archivo.is_file():
            continue
        ruta = archivo.relative_to(raiz).as_posix()
        if not es_md_publicado(ruta):
            continue
        paginas.append(
            {
                "ruta": ruta,
                "titulo": titulo_de(archivo),
                "seccion": seccion_de(ruta),
            }
        )
    return paginas


def arbol(raiz: Path) -> dict:
    grupos: dict[str, list[dict[str, str]]] = {}
    for pagina in listar_paginas(raiz):
        grupos.setdefault(pagina["seccion"], []).append(
            {"ruta": pagina["ruta"], "titulo": pagina["titulo"]}
        )
    pestanas = []
    for clave, etiqueta in SECCIONES:
        if clave not in grupos:
            continue
        paginas = grupos[clave]
        if clave == "changelog":
            paginas = sorted(paginas, key=lambda pagina: (ORDEN_CHANGELOG.get(pagina["ruta"], 99), pagina["ruta"]))
        else:
            paginas = sorted(paginas, key=lambda pagina: pagina["ruta"])
        pestanas.append({"id": clave, "titulo": etiqueta, "paginas": paginas})
    return {"raiz": raiz.name, "pestanas": pestanas}


def hacer_manejador(raiz: Path):
    class Manejador(BaseHTTPRequestHandler):
        def log_message(self, formato: str, *args) -> None:
            return

        def do_GET(self) -> None:  # noqa: N802
            url = urlparse(self.path)
            ruta = unquote(url.path)
            try:
                if ruta in {"/", "/index.html"}:
                    self._enviar_archivo(STATIC / "index.html")
                elif ruta == "/estilos.css":
                    self._enviar_archivo(STATIC / "estilos.css")
                elif ruta == "/app.js":
                    self._enviar_archivo(STATIC / "app.js")
                elif ruta == "/markdown.js":
                    self._enviar_archivo(STATIC / "markdown.js")
                elif ruta == "/api/arbol":
                    self._enviar_json(arbol(raiz))
                elif ruta == "/api/pagina":
                    self._enviar_pagina(url.query)
                elif ruta.startswith("/archivo/"):
                    self._enviar_documento(ruta[len("/archivo/") :])
                else:
                    self.send_error(404)
            except PermissionError:
                self.send_error(403)
            except FileNotFoundError:
                self.send_error(404)
            except OSError:
                self.send_error(500)

        def _enviar_pagina(self, query: str) -> None:
            relativa = parse_qs(query).get("ruta", [""])[0]
            normal = normalizar(raiz, relativa)
            if not es_md_publicado(normal):
                self.send_error(404)
                return
            archivo = raiz / normal
            if not archivo.is_file():
                self.send_error(404)
                return
            texto = archivo.read_text(encoding="utf-8", errors="replace")[:MAX_BYTES]
            self._enviar_json(
                {"ruta": normal, "titulo": titulo_de(archivo), "markdown": texto}
            )

        def _enviar_documento(self, relativa: str) -> None:
            normal = normalizar(raiz, relativa)
            if not es_asset_publicado(normal):
                self.send_error(404)
                return
            archivo = raiz / normal
            if not archivo.is_file():
                self.send_error(404)
                return
            self._enviar_archivo(archivo)

        def _enviar_json(self, datos: dict) -> None:
            cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(cuerpo)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(cuerpo)

        def _enviar_archivo(self, archivo: Path) -> None:
            if not archivo.is_file():
                self.send_error(404)
                return
            datos = archivo.read_bytes()
            tipo = MEDIA_TYPES.get(archivo.suffix.lower(), "application/octet-stream")
            self.send_response(200)
            self.send_header("Content-Type", tipo)
            self.send_header("Content-Length", str(len(datos)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(datos)

    return Manejador


def servir(raiz: Path, puerto: int) -> None:
    raiz = raiz.resolve()
    if not raiz.is_dir():
        raise SystemExit(f"No existe la carpeta de documentación: {raiz}")
    try:
        servidor = ThreadingHTTPServer(("127.0.0.1", puerto), hacer_manejador(raiz))
    except OSError as error:
        raise SystemExit(f"No se pudo abrir el puerto {puerto}: {error}") from error
    url = f"http://127.0.0.1:{servidor.server_address[1]}/"
    print(url, flush=True)
    print(f"Leyendo {raiz}", flush=True)
    print("Solo lectura: no se escribe ningún archivo.", flush=True)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nVista detenida.", flush=True)
    finally:
        servidor.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Vista local de solo lectura de los Markdown.")
    parser.add_argument(
        "--raiz",
        default="docs/sistema-diseno",
        help="Carpeta de documentación que se lee. No se escribe dentro de ella.",
    )
    parser.add_argument("--puerto", type=int, default=8765)
    args = parser.parse_args()
    servir(Path(args.raiz), args.puerto)


if __name__ == "__main__":
    main()
