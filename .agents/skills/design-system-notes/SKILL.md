---
name: design-system-notes
description: Procesa y organiza notas raw de sistemas de diseño sin inventar ni eliminar información. Gestiona changelog acumulativo, reportes diarios por área, registro de deuda técnica, especificaciones de componentes, borradores para Storybook, reorganización limpia de notas y mensajes de actualización con tono de marca. Usar cuando el usuario mencione notas raw, changelog, reporte diario, deuda técnica de UI, especificaciones de componentes, Storybook o guías de marca de un sistema de diseño.
---

# Design System Notes — Skill de Gestión de Notas

Esta skill estandariza el flujo de trabajo para transformar notas desestructuradas y apuntes diarios (*raw*) en documentación formal, changelog, control de deuda y especificaciones de componentes para un sistema de diseño profesional.

---

## Principios y Reglas de Oro

### 1. Fidelidad Absoluta (Anti-Alucinación)
- **Nunca inventar datos:** Prohibido inventar nombres de componentes, props, tokens, variantes, decisiones de arquitectura o justificaciones que no figuren en las notas de origen.
- **Transparencia en vacíos:** Si un campo de una especificación o plantilla no se menciona en las notas, debe registrarse explícitamente como `No consta en las notas raw`.
- **Preservación total:** No eliminar ningún hecho técnico real ni descartar información. Lo que no encaje en las categorías predefinidas debe ir a la sección **Resto / Sin clasificar**.
- **Gestión de dudas:** Si una nota es ambigua o parece deuda sin confirmar, se registra bajo **Posible Deuda / Para Confirmar** o **Sin clasificar**, y se consulta al usuario al finalizar.

### 2. Regla Estricta: Ficheros Raw Intocables
- **Los ficheros bajo `raw/` son de SOLO LECTURA.**
- Ningún comando debe sobrescribir, editar, reordenar, truncar ni vaciar un fichero raw.
- La única excepción es el comando `renombrar-raw`, el cual modifica **únicamente** el nombre del archivo en disco; el contenido interior se mantiene byte a byte idéntico.
- Las salidas procesadas siempre se escriben en rutas dedicadas (`ordenado/`, `clasificado/`, `reportes/`, `componentes/`, etc.). Si un archivo de destino ya existe, advertir al usuario antes de sobrescribir.

### 3. Tono y Voz de Marca
- Si existe el archivo `docs/sistema-diseno/marca/voz.md`, aplicar sus principios de estilo, tratamiento y glosario a los textos generados (títulos, conectores y mensajes).
- La voz de marca **nunca** debe desvirtuar ni alterar la exactitud de los datos técnicos.
- Si no existe guía de marca, utilizar un tono profesional, claro, directo y neutro en el mismo idioma de las notas.

---

## Estructura de Documentación del Proyecto

La raíz predeterminada es `docs/sistema-diseno/`. Si el usuario indica otra ruta en su mensaje, usar la proporcionada. Si las carpetas no existen al momento de escribir, crearlas automáticamente.

```text
docs/sistema-diseno/
├── raw/                         <- Notas originales del usuario (SOLO LECTURA)
├── ordenado/                    <- Salidas del comando reorganizar
├── clasificado/                 <- Salidas del comando clasificar
├── componentes/                 <- Especificaciones vivas de cada componente (<slug>.md)
├── reportes/                    <- Reportes diarios agrupados por área (YYYY-MM-DD.md)
├── storybook/                   <- Borradores de contexto para Storybook (<slug>.md)
├── marca/
│   ├── fuente/                  <- Archivos de marca originales (PDF, MD, TXT)
│   └── voz.md                   <- Directrices extraídas de tono y redacción
├── changelog.md                 <- Registro cronológico acumulativo por tipo de cambio
└── deuda.md                     <- Registro centralizado de deuda técnica y tareas
```

---

## Metadatos Iniciales: Fecha y Autor

Antes de generar cualquier documento o entrada:
1. **Fecha:** Determinar la fecha local actual en formato `YYYY-MM-DD` (o `DDMMYYYY` para nombres de archivo con `renombrar-raw`). Si el usuario especifica una fecha distinta, usar esa.
2. **Autor:** Consultar el autor ejecutando `git config user.name` en la terminal. Si no devuelve resultado o no hay git configurado, preguntar al usuario cómo firmar la entrada.

Consulte [reference.md](reference.md) para acceder a las plantillas completas de cada documento y [examples.md](examples.md) para ejemplos de transformación.

---

## Comandos Disponibles

Ejecutar el flujo correspondiente según la solicitud del usuario o el comando invocado:

### 1. `update-changelog`
Procesa las notas raw de la jornada para actualizar el changelog acumulativo y generar el reporte diario.
1. Localizar los ficheros raw del día en `docs/sistema-diseno/raw/` o la ruta indicada por el usuario.
2. Extraer los hechos técnicos y categorizarlos por **Tipo de cambio** según la plantilla de `reference.md`:
   - `Añadido`, `Cambiado`, `Corregido`, `Eliminado`, `Documentación`, `Deprecado`, `Sin clasificar`.
   - **Regla:** Solo escribir las secciones que contengan notas. Omitir secciones vacías.
3. Añadir la nueva entrada al principio de `docs/sistema-diseno/changelog.md` precedida por `## [YYYY-MM-DD] - @autor`. Si el archivo no existe, crearlo con su título general.
4. Generar o actualizar el reporte diario en `docs/sistema-diseno/reportes/YYYY-MM-DD.md` categorizado por **Área** (Componentes, Tokens y Fundamentos, Documentación, Accesibilidad, Deuda, Contenido y Redacción, Patrones y Flujos, Resto).
5. Cerrar informando qué se agregó al changelog, qué se guardó en el reporte y si quedó información en *Sin clasificar*.

### 2. `reorganizar`
Limpia y estructura una nota raw sin modificar el original.
1. Leer el fichero raw especificado.
2. Identificar todos los datos, decisiones, listas y fragmentos desordenados.
3. Generar un **nuevo archivo** en `docs/sistema-diseno/ordenado/<nombre-original>-ordenado.md` siguiendo la plantilla de `reference.md`.
4. Asignar títulos claros, listas legibles y agrupar por temáticas afines, conservando el 100% de los datos exactos. Corregir erratas tipográficas solo si la palabra es inequívoca.
5. Recordar al usuario que el fichero raw original permanece intacto.

### 3. `update-deuda`
Centraliza la deuda técnica en el archivo maestro `deuda.md`.
1. Leer el fichero raw específico de deuda del día (si existe).
2. Revisar exhaustivamente el resto de ficheros raw de la jornada en busca de menciones de deuda, inconsistencias, `TODO`, `FIXME` o tareas pendientes olvidadas.
3. Clasificar cada hallazgo:
   - **Deuda Confirmada:** Problemas concretos bien definidos -> Asignar ID `[DEUDA-YYYYMMDD-XX]`.
   - **Posible Deuda / Para Confirmar:** Menciones ambiguas o dudas ("revisar luego", "parece que falla...") -> Asignar ID `[POSIBLE-YYYYMMDD-XX]`.
4. Agregar los nuevos ítems en `docs/sistema-diseno/deuda.md` bajo sus respectivas secciones respetando la plantilla de `reference.md`.
5. Informar al usuario de los ítems agregados y preguntar sobre las posibles deudas para confirmarlas o descartarlas.

### 4. `generar-mensaje`
Redacta un mensaje de actualización conciso y profesional listo para enviar al equipo.
1. Leer los cambios del día registrados en el changelog o en los ficheros raw.
2. Aplicar el tono definido en `docs/sistema-diseno/marca/voz.md` (o tono neutro/profesional si no existe).
3. Redactar el mensaje en el cuerpo de la respuesta del chat siguiendo la estructura de `reference.md` (resumen clave, novedades por componente, tokens, avisos de breaking changes/deuda y enlaces a los documentos).
4. **No crear ningún archivo en disco.** El usuario copiará y pegará el texto directamente en su canal de comunicación (Slack, Teams, etc.).

### 5. `incluir-marca`
Incorpora y procesa directrices de marca de cualquier empresa u organización.
1. Si el usuario suministra un archivo (PDF, Markdown o texto), archivarlo en `docs/sistema-diseno/marca/fuente/`.
   - Si es un archivo PDF y el entorno de herramientas permite leerlo, extraer su contenido. Si no es legible de forma nativa, solicitar al usuario que pegue los extractos relevantes de tono y redacción.
2. Analizar el texto fuente y extraer:
   - Personalidad y tono de comunicación.
   - Criterios de redacción para documentación (tratamiento, formato de listas, oraciones).
   - Glosario de términos preferidos y prohibidos.
   - Pautas de mensajes para el equipo.
3. Escribir o actualizar `docs/sistema-diseno/marca/voz.md` respetando la plantilla de `reference.md`.
4. Confirmar al usuario que a partir de ese momento todos los comandos aplicarán esa voz.

### 6. `renombrar-raw`
Estandariza los nombres de los archivos raw para su trazabilidad temporal sin tocar su contenido.
1. Localizar los ficheros raw indicados (o los del día en `docs/sistema-diseno/raw/`).
2. Comprobar el nombre actual. Si ya termina con el formato de fecha `<nombre>-<DDMMYYYY>.md` (ej. `notas-23102026.md`), no duplicar la fecha.
3. Si el nombre no tiene fecha o usa otro formato, renombrarlo al esquema `<nombre-base>-<DDMMYYYY>.md`.
4. Si el archivo de destino ya existe, detenerse y advertir al usuario para no sobrescribir nada.
5. Garantizar que el contenido del archivo no sufra ninguna alteración.

### 7. `actualizar-spec`
Crea o actualiza la especificación técnica de un componente a partir de las notas.
1. Extraer del raw todas las menciones asociadas al componente solicitado (props, variantes, tokens, estados, accesibilidad, etc.).
2. Determinar el slug del componente tal como viene en las notas (ej. `badge.md`, `action-button.md`).
3. Crear o actualizar `docs/sistema-diseno/componentes/<slug>.md` con las 11 secciones de la plantilla en `reference.md`.
4. Rellenar cada sección con la información encontrada. Todo campo no mencionado en las notas debe quedar explícitamente como `No consta en las notas raw`.
5. Reportar al usuario qué secciones quedaron completas y cuáles en `No consta`.

### 8. `preparar-storybook`
Genera el borrador de contexto necesario para documentar el componente en Storybook.
1. Leer la especificación viva del componente en `docs/sistema-diseno/componentes/<slug>.md`.
2. Generar `docs/sistema-diseno/storybook/<slug>.md` siguiendo la plantilla de `reference.md`.
3. Mapear argTypes preliminares, variantes y estados documentados.
4. Señalar de forma explícita qué props o controles requieren confirmación del desarrollador frente al código fuente (`[No consta en notas / Validar con código]`).

### 9. `clasificar`
Separa notas raw extremadamente mezcladas en ficheros limpios independientes.
1. Leer la nota raw caótica.
2. Identificar bloques temáticos: cambios para changelog, puntos de deuda técnica y especificaciones de componentes.
3. Generar archivos nuevos en `docs/sistema-diseno/clasificado/` (ej. `cambios-<fecha>.md`, `deuda-<fecha>.md`, `componente-<nombre>.md`).
4. **No modificar el fichero raw original.**
5. Presentar un resumen de cómo se distribuyó el contenido y preguntar al usuario si desea ejecutar `update-changelog`, `update-deuda` o `actualizar-spec` sobre dichos ficheros.

---

## Cierre de Cada Operación

Al concluir la ejecución de cualquier comando, el agente debe presentar un informe de cierre con:
1. **Artefactos procesados y generados:** Lista clara de ficheros leídos y ficheros creados o actualizados.
2. **Restos o elementos sin clasificar:** Si hubo datos que no encajaron en las plantillas, mostrarlos de forma destacada y preguntar al usuario dónde deben archivarse.
3. **Campos con información pendiente:** Indicar los apartados que quedaron marcados con `No consta en las notas raw`.
