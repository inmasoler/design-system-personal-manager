# Glosario Rápido de Comandos — Skill Notas de Sistema de Diseño

Guía rápida de los 14 comandos disponibles en la skill. Puedes invocar cualquiera de ellos simplemente escribiendo su nombre en el chat con el agente. La skill no asume una empresa ni un design system: foundations, modos y nombres de token salen de tus notas, de tus exports o de `foundations/convenciones.md`.

---

## 1. `renombrar-raw`
- **Qué hace:** Estandariza el nombre de tus notas raw al formato `<nombre>-<DDMMYYYY>.md` (ej. `apuntes-sesion-23102026.md`).
- **Qué toca:** Solo el nombre del archivo en disco. El contenido interno queda **100% idéntico** byte a byte. No duplica la fecha si ya la tiene.
- **Cuándo usarlo:** Al terminar de escribir una nota desordenada o al iniciar la jornada para tener trazabilidad temporal.

---

## 2. `reorganizar`
- **Qué hace:** Toma una nota raw caótica (incluso sin títulos ni estructura) y genera una versión limpia y bien jerarquizada. No junta la spec de un componente: eso lo hace `actualizar-spec`.
- **Qué toca:** Crea un archivo nuevo en `docs/sistema-diseno/ordenado/<nombre>-ordenado.md`. El archivo raw original **permanece intacto**. No escribe en `ordenado/specs/`.
- **Cuándo usarlo:** Cuando quieres leer tus propios apuntes en limpio sin riesgo de perder ningún dato ni fragmento técnico.

---

## 3. `update-changelog`
- **Qué hace:** Extrae los hechos técnicos del día y los clasifica por **Tipo de cambio** (`Añadido`, `Cambiado`, `Corregido`, etc.) con fecha y autor. A su vez, genera el **reporte diario** del día clasificado por **Área** (`Componentes`, `Tokens`, `Accesibilidad`, etc.).
- **Qué toca:** Añade la entrada al inicio de `docs/sistema-diseno/changelog.md` y crea/actualiza `docs/sistema-diseno/reportes/YYYY-MM-DD.md`.
- **Cuándo usarlo:** Al final de una jornada o sprint para consolidar los cambios en el historial oficial.

---

## 4. `update-deuda`
- **Qué hace:** Centraliza la deuda técnica. Lee el fichero raw de deuda y rastrea menciones dispersas (`TODO`, fallos, inconsistencias, dudas) en el resto de notas del día.
- **Qué toca:** Añade nuevos ítems numerados a `docs/sistema-diseno/deuda.md`, distinguiendo entre **Deuda Confirmada** y **Posible Deuda / Para Confirmar**.
- **Cuándo usarlo:** Para que ninguna deuda o error detectado en reuniones o pruebas se quede olvidado en notas sueltas.

---

## 5. `actualizar-spec`
- **Qué hace:** Junta en una spec fiel todo lo que las notas dicen de un componente: propósito, uso, anatomía, opciones, estados, propiedades, slots, tokens, eventos, métodos, accesibilidad, comportamiento, buenas prácticas y decisiones.
- **Qué toca:** `docs/sistema-diseno/ordenado/specs/<slug-componente>.md`. No escribe la guía de `componentes/`.
- **Regla clave:** Si un dato no figura en las notas, lo marca explícitamente como `No consta en las notas raw`. Nunca inventa propiedades.
- **Cuándo usarlo:** Cuando se discuten o acuerdan los hechos de un componente (ej. `actualizar-spec button`).

---

## 6. `escribir-guia`
- **Qué hace:** Redacta la guía publicada del componente, en español, con el orden de una página de design system: descripción general, uso, anatomía, buenas prácticas, opciones, comportamiento, accesibilidad, referencia de API y decisiones.
- **Qué toca:** `docs/sistema-diseno/componentes/<slug-componente>.md`.
- **Regla clave:** Solo lee la spec de `ordenado/specs/`. Publica las secciones que tienen datos y resume los huecos una sola vez en Información pendiente. No inventa contenido.
- **Cuándo usarlo:** Cuando la spec fiel ya está al día y quieres la página del componente (ej. `escribir-guia button`).

---

## 7. `preparar-storybook`
- **Qué hace:** Toma la spec fiel y genera el borrador del sample: `argTypes`, historias y fragmentos `.stories.tsx`. No reescribe la guía.
- **Qué toca:** Crea o actualiza `docs/sistema-diseno/storybook/<slug-componente>.md`.
- **Cuándo usarlo:** Cuando un desarrollador va a crear o actualizar las historias y controles del componente en Storybook.

---

## 8. `generar-mensaje`
- **Qué hace:** Redacta un mensaje de resumen conciso, atractivo y adaptado al tono de marca para comunicar los avances del día al equipo.
- **Qué toca:** **Ningún archivo.** Lo entrega directamente en el chat para que hagas `Copiar y Pegar` en Slack, Teams o email.
- **Cuándo usarlo:** Al terminar el día o al liberar una versión interna para mantener informado al resto del equipo.

---

## 9. `incluir-marca`
- **Qué hace:** Procesa un archivo o texto de directrices de marca (PDF, markdown o texto) para extraer personalidad, tono, tratamiento y glosario técnico.
- **Qué toca:** Guarda la fuente en `docs/sistema-diseno/marca/fuente/` y actualiza `docs/sistema-diseno/marca/voz.md`.
- **Cuándo usarlo:** Al iniciar con una nueva empresa o cuando el equipo de branding actualice las guías de estilo y lenguaje.

---

## 10. `clasificar`
- **Qué hace:** Toma una nota raw extremadamente densa o mezclada y separa su contenido en archivos específicos e independientes en `docs/sistema-diseno/clasificado/` (cambios, deuda, notas de componentes, foundations).
- **Qué toca:** Crea archivos nuevos en `clasificado/`. No altera el archivo raw original.
- **Cuándo usarlo:** Antes de procesar notas muy largas tomadas durante reuniones donde se mezclaron múltiples temas a la vez.

---

## 11. `actualizar-foundation`
- **Qué hace:** Junta en un acopio fiel todo lo que las fuentes dicen de una foundation (la que conste: color, tipografía, espaciado, bordes, layout u otra): principios, construcción, usos, modos, mediciones, limitaciones y decisiones.
- **Qué toca:** `docs/sistema-diseno/ordenado/foundations/<slug>.md`. No escribe la guía de `foundations/`.
- **Regla clave:** Conserva el detalle íntegro y marca lo que falta como `No consta en las notas raw`. No completa foundations que nadie haya pedido.
- **Cuándo usarlo:** Cuando llegan notas, capturas o exports nuevos de una foundation (ej. `actualizar-foundation color`).

---

## 12. `escribir-foundation`
- **Qué hace:** Redacta la guía publicada de la foundation: principios, cómo está construida, cómo usarla, modos, accesibilidad, implementación y limitaciones conocidas.
- **Qué toca:** `docs/sistema-diseno/foundations/<slug>.md` y, si detecta huecos nuevos, `docs/sistema-diseno/pendientes.md`.
- **Regla clave:** Solo lee el acopio fiel. Sin tablas de valores, sin frases sobre la procedencia y con los huecos resumidos una vez en Información pendiente.
- **Cuándo usarlo:** Cuando el acopio está al día y quieres la página de la foundation (ej. `escribir-foundation color`).

---

## 13. `referencia-tokens`
- **Qué hace:** Genera la tabla de tokens de un área desde los exports: semánticos de sistema primero, primitivos después, con el valor resuelto por modo cuando el export trae modos.
- **Qué toca:** `docs/sistema-diseno/foundations/tokens/<area>.md`. Los tokens de componente los entrega a `ordenado/specs/<slug>.md`. El export no se modifica.
- **Regla clave:** Nombres y valores exactos. Los tokens no válidos van a Tokens bloqueados, no a las tablas. La clasificación de grupos sale de `convenciones.md` si existe; si no, se usa el defecto de la skill.
- **Cuándo usarlo:** Cada vez que se reexportan los tokens de un área (ej. `referencia-tokens color`).

---

## 14. `previsualizar`
- **Qué hace:** Abre la documentación como una página local con pestañas, para leerla como una web sin usar la preview de cada Markdown.
- **Qué toca:** Ningún archivo. Lee la carpeta de documentación y sirve una vista que vive en la skill (`vista/`, junto a `SKILL.md`).
- **Regla clave:** Los `.md` no se modifican y la vista no se guarda a su lado. El código de la vista sí se versiona en el repositorio de la skill. Al subir la documentación a otro repositorio se copian solo esos `.md`.
- **Cuándo usarlo:** Cuando quieres revisar componentes, foundations, tokens, changelog o deuda como un sitio, no como ficheros sueltos.
