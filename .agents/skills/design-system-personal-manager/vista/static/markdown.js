/* Render de un subconjunto de Markdown (títulos, listas, tablas, código, citas e inline).
   El texto de origen se escapa; solo se emiten las etiquetas de este módulo. */
(function (global) {
  function escapeHtml(texto) {
    return texto
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function slug(texto) {
    return texto
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/<[^>]*>/g, "")
      .replace(/[^a-z0-9\s-]/g, "")
      .trim()
      .replace(/\s+/g, "-") || "seccion";
  }

  function resolver(base, href) {
    if (/^[a-z]+:/i.test(href) || href.startsWith("#") || href.startsWith("/")) {
      return { externo: true, href: href };
    }
    const trozo = href.split("#");
    const camino = trozo[0];
    const ancla = trozo[1] ? "#" + trozo[1] : "";
    const basePartes = base.split("/").slice(0, -1);
    const pila = [];
    basePartes.concat(camino.split("/")).forEach(function (parte) {
      if (!parte || parte === ".") return;
      if (parte === "..") pila.pop();
      else pila.push(parte);
    });
    const ruta = pila.join("/");
    if (ruta.endsWith(".md")) return { interno: true, ruta: ruta, ancla: ancla };
    return { externo: true, href: "/archivo/" + ruta.split("/").map(encodeURIComponent).join("/") };
  }

  function renderInline(texto, base) {
    let i = 0;
    let html = "";
    while (i < texto.length) {
      if (texto[i] === "`") {
        const fin = texto.indexOf("`", i + 1);
        if (fin !== -1) {
          html += "<code>" + escapeHtml(texto.slice(i + 1, fin)) + "</code>";
          i = fin + 1;
          continue;
        }
      }
      if (texto.startsWith("**", i) || texto.startsWith("__", i)) {
        const marca = texto.slice(i, i + 2);
        const fin = texto.indexOf(marca, i + 2);
        if (fin !== -1) {
          html += "<strong>" + renderInline(texto.slice(i + 2, fin), base) + "</strong>";
          i = fin + 2;
          continue;
        }
      }
      if (texto[i] === "*" && texto[i + 1] !== " ") {
        const fin = texto.indexOf("*", i + 1);
        if (fin > i + 1) {
          html += "<em>" + renderInline(texto.slice(i + 1, fin), base) + "</em>";
          i = fin + 1;
          continue;
        }
      }
      if (texto[i] === "!" && texto[i + 1] === "[") {
        const cierre = texto.indexOf("]", i + 2);
        if (cierre !== -1 && texto[cierre + 1] === "(") {
          const fin = texto.indexOf(")", cierre + 2);
          if (fin !== -1) {
            const alt = escapeHtml(texto.slice(i + 2, cierre));
            const destino = resolver(base, texto.slice(cierre + 2, fin).trim());
            html += '<img alt="' + alt + '" src="' + escapeHtml(destino.href || "") + '">';
            i = fin + 1;
            continue;
          }
        }
      }
      if (texto[i] === "[") {
        const cierre = texto.indexOf("]", i + 1);
        if (cierre !== -1 && texto[cierre + 1] === "(") {
          const fin = texto.indexOf(")", cierre + 2);
          if (fin !== -1) {
            const etiqueta = renderInline(texto.slice(i + 1, cierre), base);
            const href = texto.slice(cierre + 2, fin).trim();
            const destino = resolver(base, href);
            if (destino.interno) {
              const ancla = destino.ancla ? destino.ancla.slice(1) : "";
              html +=
                '<a href="#' +
                escapeHtml(destino.ruta + (ancla ? "?ancla=" + ancla : "")) +
                '" data-ruta="' +
                escapeHtml(destino.ruta) +
                '" data-ancla="' +
                escapeHtml(ancla) +
                '">' +
                etiqueta +
                "</a>";
            } else {
              const externo = /^[a-z]+:/i.test(destino.href);
              html +=
                '<a href="' +
                escapeHtml(destino.href) +
                '"' +
                (externo ? ' target="_blank" rel="noreferrer"' : "") +
                ">" +
                etiqueta +
                "</a>";
            }
            i = fin + 1;
            continue;
          }
        }
      }
      html += escapeHtml(texto[i]);
      i += 1;
    }
    return html;
  }

  function esSeparador(linea) {
    return /^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$/.test(linea) && linea.indexOf("-") !== -1;
  }

  function celdas(linea) {
    let texto = linea.trim();
    if (texto.startsWith("|")) texto = texto.slice(1);
    if (texto.endsWith("|")) texto = texto.slice(0, -1);
    return texto.split("|").map(function (celda) {
      return celda.trim();
    });
  }

  function alineacion(separador) {
    return celdas(separador).map(function (celda) {
      const izq = celda.startsWith(":");
      const der = celda.endsWith(":");
      if (izq && der) return "center";
      if (der) return "right";
      return "left";
    });
  }

  function renderTabla(lineas, indice, base) {
    const cabecera = celdas(lineas[indice]);
    const align = alineacion(lineas[indice + 1]);
    let i = indice + 2;
    const filas = [];
    while (i < lineas.length && lineas[i].trim().startsWith("|")) {
      filas.push(celdas(lineas[i]));
      i += 1;
    }
    let html = "<table><thead><tr>";
    cabecera.forEach(function (celda, n) {
      html += '<th style="text-align:' + (align[n] || "left") + '">' + renderInline(celda, base) + "</th>";
    });
    html += "</tr></thead><tbody>";
    filas.forEach(function (fila) {
      html += "<tr>";
      cabecera.forEach(function (_, n) {
        html += '<td style="text-align:' + (align[n] || "left") + '">' + renderInline(fila[n] || "", base) + "</td>";
      });
      html += "</tr>";
    });
    return { html: html + "</tbody></table>", siguiente: i };
  }

  function marcaLista(linea) {
    const coincide = /^(\s*)([-*+]|\d+\.)\s+(.+)$/.exec(linea);
    if (!coincide) return null;
    return { sangria: coincide[1].length, ordenada: /\d/.test(coincide[2]), texto: coincide[3] };
  }

  function renderLista(lineas, indice, base) {
    const items = [];
    let i = indice;
    const raiz = marcaLista(lineas[i]);
    const ordenada = raiz.ordenada;
    const sangria = raiz.sangria;
    while (i < lineas.length) {
      if (lineas[i].trim() === "") {
        const siguiente = marcaLista(lineas[i + 1] || "");
        if (siguiente && siguiente.sangria >= sangria) {
          i += 1;
          continue;
        }
        break;
      }
      const marca = marcaLista(lineas[i]);
      if (!marca || marca.sangria < sangria) break;
      if (marca.sangria > sangria) {
        const anidada = renderLista(lineas, i, base);
        if (items.length) items[items.length - 1].html += anidada.html;
        i = anidada.siguiente;
        continue;
      }
      if (marca.ordenada !== ordenada && items.length) break;
      let cuerpo = renderInline(marca.texto, base);
      i += 1;
      while (i < lineas.length && lineas[i].trim() !== "" && !marcaLista(lineas[i]) && /^\s+\S/.test(lineas[i])) {
        cuerpo += " " + renderInline(lineas[i].trim(), base);
        i += 1;
      }
      items.push({ html: cuerpo });
    }
    const etiqueta = ordenada ? "ol" : "ul";
    return {
      html: "<" + etiqueta + ">" + items.map(function (item) { return "<li>" + item.html + "</li>"; }).join("") + "</" + etiqueta + ">",
      siguiente: i,
    };
  }

  function renderMarkdown(origen, opciones) {
    const base = (opciones && opciones.base) || "";
    const lineas = String(origen).replace(/\r\n/g, "\n").replace(/\r/g, "\n").split("\n");
    const usados = {};
    const bloques = [];
    let i = 0;

    function identificador(textoPlano) {
      let id = slug(textoPlano);
      if (usados[id]) {
        usados[id] += 1;
        id = id + "-" + usados[id];
      } else {
        usados[id] = 1;
      }
      return id;
    }

    while (i < lineas.length) {
      const linea = lineas[i];
      if (linea.trim() === "") {
        i += 1;
        continue;
      }
      if (linea.startsWith("```")) {
        const idioma = linea.slice(3).trim();
        const trozos = [];
        i += 1;
        while (i < lineas.length && !lineas[i].startsWith("```")) {
          trozos.push(lineas[i]);
          i += 1;
        }
        if (i < lineas.length) i += 1;
        bloques.push(
          "<pre><code" +
            (idioma ? ' class="idioma-' + escapeHtml(idioma) + '"' : "") +
            ">" +
            escapeHtml(trozos.join("\n")) +
            "</code></pre>"
        );
        continue;
      }
      if (/^\s*([-*_])(\s*\1){2,}\s*$/.test(linea)) {
        bloques.push("<hr>");
        i += 1;
        continue;
      }
      const titulo = /^(#{1,6})\s+(.+?)\s*#*$/.exec(linea);
      if (titulo) {
        const nivel = titulo[1].length;
        const plano = titulo[2].replace(/[`*]/g, "");
        bloques.push(
          "<h" + nivel + ' id="' + identificador(plano) + '">' + renderInline(titulo[2], base) + "</h" + nivel + ">"
        );
        i += 1;
        continue;
      }
      if (linea.trim().startsWith("|") && esSeparador(lineas[i + 1] || "")) {
        const tabla = renderTabla(lineas, i, base);
        bloques.push(tabla.html);
        i = tabla.siguiente;
        continue;
      }
      if (marcaLista(linea)) {
        const lista = renderLista(lineas, i, base);
        bloques.push(lista.html);
        i = lista.siguiente;
        continue;
      }
      if (linea.trim().startsWith(">")) {
        const citas = [];
        while (i < lineas.length && lineas[i].trim().startsWith(">")) {
          citas.push(lineas[i].replace(/^\s*>\s?/, ""));
          i += 1;
        }
        bloques.push("<blockquote>" + renderMarkdown(citas.join("\n"), opciones) + "</blockquote>");
        continue;
      }
      const parrafo = [];
      while (
        i < lineas.length &&
        lineas[i].trim() !== "" &&
        !lineas[i].startsWith("```") &&
        !/^(#{1,6})\s+/.test(lineas[i]) &&
        !marcaLista(lineas[i]) &&
        !(lineas[i].trim().startsWith("|") && esSeparador(lineas[i + 1] || "")) &&
        !/^\s*([-*_])(\s*\1){2,}\s*$/.test(lineas[i]) &&
        !lineas[i].trim().startsWith(">")
      ) {
        parrafo.push(lineas[i].trim());
        i += 1;
      }
      if (parrafo.length) bloques.push("<p>" + renderInline(parrafo.join(" "), base) + "</p>");
    }
    return bloques.join("\n");
  }

  global.renderMarkdown = renderMarkdown;
})(typeof window !== "undefined" ? window : globalThis);
