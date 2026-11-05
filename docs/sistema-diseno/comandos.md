# Glosario Rápido de Comandos — Skill Notas de Sistema de Diseño

Guía rápida de los 9 comandos disponibles en la skill. Puedes invocar cualquiera de ellos simplemente escribiendo su nombre en el chat con el agente.

---

## 1. `renombrar-raw`
- **Qué hace:** Estandariza el nombre de tus notas raw al formato `<nombre>-<DDMMYYYY>.md` (ej. `apuntes-sesion-23102026.md`).
- **Qué toca:** Solo el nombre del archivo en disco. El contenido interno queda **100% idéntico** byte a byte. No duplica la fecha si ya la tiene.
- **Cuándo usarlo:** Al terminar de escribir una nota desordenada o al iniciar la jornada para tener trazabilidad temporal.

---

## 2. `reorganizar`
- **Qué hace:** Toma una nota raw caótica (incluso sin títulos ni estructura) y genera una versión limpia y bien jerarquizada.
- **Qué toca:** Crea un archivo nuevo en `docs/sistema-diseno/ordenado/<nombre>-ordenado.md`. El archivo raw original **permanece intacto**.
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
- **Qué hace:** Crea o actualiza la especificación viva de un componente a partir de las notas raw. Estructura 11 apartados clave (props, variantes, estados, a11y, tokens, decisiones).
- **Qué toca:** `docs/sistema-diseno/componentes/<slug-componente>.md`.
- **Regla clave:** Si un dato no figura en las notas, lo marca explícitamente como `No consta en las notas raw`. Nunca inventa propiedades.
- **Cuándo usarlo:** Cuando se discuten o acuerdan especificaciones de un componente (ej. `actualizar-spec button`).

---

## 6. `preparar-storybook`
- **Qué hace:** Toma la spec viva del componente y genera un borrador de contexto optimizado para Storybook con sugerencias de `argTypes`, variantes a documentar y snippets de código `.stories.tsx`.
- **Qué toca:** Crea o actualiza `docs/sistema-diseno/storybook/<slug-componente>.md`.
- **Cuándo usarlo:** Cuando un desarrollador va a crear o actualizar las historias y controles del componente en Storybook.

---

## 7. `generar-mensaje`
- **Qué hace:** Redacta un mensaje de resumen conciso, atractivo y adaptado al tono de marca para comunicar los avances del día al equipo.
- **Qué toca:** **Ningún archivo.** Lo entrega directamente en el chat para que hagas `Copiar y Pegar` en Slack, Teams o email.
- **Cuándo usarlo:** Al terminar el día o al liberar una versión interna para mantener informado al resto del equipo.

---

## 8. `incluir-marca`
- **Qué hace:** Procesa un archivo o texto de directrices de marca (PDF, markdown o texto) para extraer personalidad, tono, tratamiento y glosario técnico.
- **Qué toca:** Guarda la fuente en `docs/sistema-diseno/marca/fuente/` y actualiza `docs/sistema-diseno/marca/voz.md`.
- **Cuándo usarlo:** Al iniciar con una nueva empresa o cuando el equipo de branding actualice las guías de estilo y lenguaje.

---

## 9. `clasificar`
- **Qué hace:** Toma una nota raw extremadamente densa o mezclada y separa su contenido en archivos específicos e independientes en `docs/sistema-diseno/clasificado/` (cambios, deuda, notas de componentes).
- **Qué toca:** Crea archivos nuevos en `clasificado/`. No altera el archivo raw original.
- **Cuándo usarlo:** Antes de procesar notas muy largas tomadas durante reuniones donde se mezclaron múltiples temas a la vez.
