#!/usr/bin/env python3
"""Vista local de solo lectura para los Markdown de un sistema de diseño.

No crea, modifica ni borra archivos. Sirve la interfaz que vive junto a este
script y lee la carpeta de documentación que se le indique.
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

# Orden de las secciones conocidas. Cualquier otra carpeta o Markdown de la
# raíz aparece después, con su propio nombre: la vista no asume un sistema.
SECCIONES = (
    ("componentes", "Componentes"),
    ("foundations", "Foundations"),
    ("tokens", "Tokens"),
    ("changelog", "Changelog"),
    ("deuda", "Deuda"),
    ("pendientes", "Pendientes"),
    ("reportes", "Reportes"),
    ("storybook", "Storybook"),
    ("marca", "Marca"),
    ("comandos", "Comandos"),
    ("ordenado", "Acopio"),
    ("clasificado", "Clasificado"),
    ("raw", "Notas raw"),
)
SECCION_IDS = {clave for clave, _ in SECCIONES}
SALTAR_DIRECTORIOS = {".git", "node_modules", "__pycache__"}
HEADING = re.compile(r"^#\s+(.+?)\s*$")


def dentro_de(raiz: Path, candidato: Path) -> Path:
    raiz_resuelta = raiz.resolve()
    destino = candidato.resolve()
    if destino != raiz_resuelta and raiz_resuelta not in destino.parents:
        raise PermissionError(destino)
    return destino


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
    if ruta in {"changelog.md", "deuda.md", "pendientes.md", "comandos.md"}:
        return nombre[:-3]
    if partes[0] == "foundations" and (
        nombre == "tokens.md" or (len(partes) > 1 and partes[1] == "tokens")
    ):
        return "tokens"
    if partes[0] in SECCION_IDS:
        return partes[0]
    if len(partes) == 1:
        return nombre[:-3]
    return partes[0]


def etiqueta_de(clave: str) -> str:
    for identificador, etiqueta in SECCIONES:
        if identificador == clave:
            return etiqueta
    return clave.replace("-", " ")


def listar_paginas(raiz: Path) -> list[dict[str, str]]:
    paginas = []
    if not raiz.is_dir():
        return paginas
    for archivo in sorted(raiz.rglob("*.md")):
        rel = archivo.relative_to(raiz)
        if any(parte.startswith(".") or parte in SALTAR_DIRECTORIOS for parte in rel.parts):
            continue
        ruta = rel.as_posix()
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
    orden = [clave for clave, _ in SECCIONES if clave in grupos]
    resto = sorted(clave for clave in grupos if clave not in SECCION_IDS)
    pestanas = [
        {"id": clave, "titulo": etiqueta_de(clave), "paginas": grupos[clave]}
        for clave in orden + resto
    ]
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
            if not relativa.endswith(".md"):
                self.send_error(404)
                return
            archivo = dentro_de(raiz, raiz / relativa)
            if not archivo.is_file():
                self.send_error(404)
                return
            texto = archivo.read_text(encoding="utf-8", errors="replace")[:MAX_BYTES]
            self._enviar_json(
                {"ruta": relativa, "titulo": titulo_de(archivo), "markdown": texto}
            )

        def _enviar_documento(self, relativa: str) -> None:
            archivo = dentro_de(raiz, raiz / relativa)
            if not archivo.is_file() or archivo.suffix.lower() == ".md":
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
