(function () {
  const pestanasEl = document.getElementById("pestanas");
  const indiceEl = document.getElementById("indice");
  const lecturaEl = document.getElementById("lectura");
  const raizEl = document.getElementById("raiz");
  const marcoEl = document.querySelector(".marco");
  let arbol = { pestanas: [] };

  function destinoActual() {
    const crudo = location.hash.replace(/^#/, "");
    const corte = crudo.indexOf("?");
    const ruta = decodeURIComponent(corte === -1 ? crudo : crudo.slice(0, corte));
    const ancla = new URLSearchParams(corte === -1 ? "" : crudo.slice(corte + 1)).get("ancla") || "";
    return { ruta: ruta.replace(/^\/+/, ""), ancla: ancla };
  }

  function ir(ruta, ancla) {
    const destino = "#" + encodeURI(ruta) + (ancla ? "?ancla=" + encodeURIComponent(ancla) : "");
    if (location.hash === destino) pintar();
    else location.hash = destino;
  }

  function seccionDe(ruta) {
    const pagina = arbol.pestanas
      .flatMap(function (pestana) { return pestana.paginas.map(function (p) { return { id: pestana.id, ruta: p.ruta }; }); })
      .find(function (item) { return item.ruta === ruta.split("#")[0]; });
    return pagina ? pagina.id : (arbol.pestanas[0] && arbol.pestanas[0].id);
  }

  function pintarPestanas(activa) {
    pestanasEl.replaceChildren();
    arbol.pestanas.forEach(function (pestana) {
      const boton = document.createElement("button");
      boton.type = "button";
      boton.textContent = pestana.titulo;
      boton.setAttribute("aria-selected", pestana.id === activa ? "true" : "false");
      boton.addEventListener("click", function () {
        ir(pestana.paginas[0].ruta);
      });
      pestanasEl.appendChild(boton);
    });
  }

  function pintarIndice(pestana, ruta) {
    if (!pestana || pestana.paginas.length < 2) {
      indiceEl.hidden = true;
      indiceEl.replaceChildren();
      marcoEl.classList.add("sin-indice");
      return;
    }
    marcoEl.classList.remove("sin-indice");
    indiceEl.hidden = false;
    indiceEl.replaceChildren();
    const etiqueta = document.createElement("p");
    etiqueta.textContent = "Páginas";
    indiceEl.appendChild(etiqueta);
    pestana.paginas.forEach(function (pagina) {
      const boton = document.createElement("button");
      boton.type = "button";
      boton.textContent = pagina.titulo;
      if (pagina.ruta === ruta) boton.setAttribute("aria-current", "page");
      boton.addEventListener("click", function () { ir(pagina.ruta); });
      indiceEl.appendChild(boton);
    });
  }

  function mensaje(texto) {
    lecturaEl.replaceChildren();
    const p = document.createElement("p");
    p.className = "vacio";
    p.textContent = texto;
    lecturaEl.appendChild(p);
  }

  async function pintar() {
    if (!arbol.pestanas.length) {
      pestanasEl.replaceChildren();
      indiceEl.hidden = true;
      marcoEl.classList.add("sin-indice");
      mensaje("Esta carpeta todavía no tiene Markdown.");
      return;
    }
    const actual = destinoActual();
    let ruta = actual.ruta;
    const existe = arbol.pestanas.some(function (pestana) {
      return pestana.paginas.some(function (pagina) { return pagina.ruta === ruta; });
    });
    if (!existe) ruta = arbol.pestanas[0].paginas[0].ruta;
    const seccion = seccionDe(ruta);
    const pestana = arbol.pestanas.find(function (item) { return item.id === seccion; });
    pintarPestanas(seccion);
    pintarIndice(pestana, ruta);
    const respuesta = await fetch("/api/pagina?ruta=" + encodeURIComponent(ruta));
    if (!respuesta.ok) {
      mensaje("No se pudo leer esa página.");
      return;
    }
    const datos = await respuesta.json();
    const html = window.renderMarkdown(datos.markdown, { base: datos.ruta });
    lecturaEl.innerHTML = html;
    lecturaEl.querySelectorAll("table").forEach(function (tabla) {
      const marco = document.createElement("div");
      marco.className = "tabla-scroll";
      tabla.replaceWith(marco);
      marco.appendChild(tabla);
    });
    document.title = datos.titulo + " · Documentación";
    if (actual.ancla) {
      const destino = document.getElementById(actual.ancla);
      if (destino) destino.scrollIntoView();
      else window.scrollTo(0, 0);
    } else {
      window.scrollTo(0, 0);
    }
  }

  document.addEventListener("click", function (evento) {
    const enlace = evento.target.closest("a[data-ruta]");
    if (!enlace) return;
    evento.preventDefault();
    ir(enlace.getAttribute("data-ruta"), enlace.getAttribute("data-ancla") || "");
  });

  window.addEventListener("hashchange", pintar);

  fetch("/api/arbol")
    .then(function (respuesta) { return respuesta.json(); })
    .then(function (datos) {
      arbol = datos;
      raizEl.textContent = datos.raiz || "";
      return pintar();
    })
    .catch(function () {
      mensaje("No se pudo leer la documentación.");
    });
})();
