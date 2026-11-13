---
name: design-system-personal-manager
description: Procesa y organiza notas raw de sistemas de diseño sin inventar ni eliminar información. Gestiona changelog acumulativo, reportes diarios por área, registro de deuda técnica, el acopio fiel y la guía publicada de cada componente, el acopio y la guía de foundations, la referencia de tokens y el registro de información pendiente. Las convenciones de cada sistema se leen como datos del proyecto y no se asume una empresa ni un design system concreto. También abre una vista local de solo lectura, con pestañas, sin modificar ni acompañar a los Markdown. Usar cuando el usuario mencione notas raw, changelog, reporte diario, deuda técnica de UI, especificaciones o guías de componentes, foundations, tokens, pendientes, Storybook, guías de marca o quiera ver la documentación como una página.
---

# Design System Personal Manager — Skill de Gestión de Notas

Esta skill estandariza el flujo de trabajo para transformar notas desestructuradas y apuntes diarios (*raw*) en documentación formal, changelog, control de deuda, una spec fiel por componente, la guía publicada de ese componente, el acopio y la guía de cada foundation, y la referencia de sus tokens. Sirve para cualquier sistema de diseño: no trae nombres, modos, capas ni prefijos de una empresa o de un sistema concreto.

---

## Principios y Reglas de Oro

### 1. Fidelidad Absoluta (Anti-Alucinación)
- **Nunca inventar datos:** Prohibido inventar nombres de componentes, props, tokens, variantes, decisiones de arquitectura o justificaciones que no figuren en las notas de origen.
- **Transparencia en vacíos:** En el acopio fiel (`ordenado/specs/` y `ordenado/foundations/`), si un campo no se menciona en las notas, debe registrarse explícitamente como `No consta en las notas raw`. En las páginas publicadas (`componentes/`, `foundations/` y `foundations/tokens/`), el apartado vacío no se rellena: se omite y el hueco se resume una sola vez en **Información pendiente**.
- **Preservación total:** No eliminar ningún hecho técnico real ni descartar información. Lo que no encaje en las categorías predefinidas debe ir a la sección **Resto / Sin clasificar**.
- **Gestión de dudas:** Si una nota es ambigua o parece deuda sin confirmar, se registra bajo **Posible Deuda / Para Confirmar** o **Sin clasificar**, y se consulta al usuario al finalizar.

### 2. Regla Estricta: Ficheros Raw Intocables
- **Los ficheros bajo `raw/` son de SOLO LECTURA.**
- Ningún comando debe sobrescribir, editar, reordenar, truncar ni vaciar un fichero raw.
- La única excepción es el comando `renombrar-raw`, el cual modifica **únicamente** el nombre del archivo en disco; el contenido interior se mantiene byte a byte idéntico.
- Las salidas procesadas siempre se escriben en rutas dedicadas (`ordenado/`, `clasificado/`, `reportes/`, `componentes/`, `foundations/`, `pendientes.md`, etc.). Si un archivo de destino ya existe, advertir al usuario antes de sobrescribir. `pendientes.md` y `deuda.md` no se sobrescriben: se les añaden entradas.

### 3. Tono y Voz de Marca
- Si existe el archivo `docs/sistema-diseno/marca/voz.md`, aplicar sus principios de estilo, tratamiento y glosario a los textos generados (títulos, conectores y mensajes).
- La voz de marca **nunca** debe desvirtuar ni alterar la exactitud de los datos técnicos.
- Si no existe guía de marca, utilizar un tono profesional, claro, directo y neutro en el mismo idioma de las notas.

### 4. Genérica: convenciones del proyecto, no de un sistema concreto
- La skill no asume empresa, producto, colección, prefijo de token, nombres de modo ni una lista cerrada de foundations. Esos datos, si existen, viven en `docs/sistema-diseno/foundations/convenciones.md`.
- Ese fichero lo escribe el usuario, o el agente solo cuando el usuario confirma cada dato. No se deduce de nombres sueltos, de un export parcial ni de otro sistema trabajado antes.
- Si `convenciones.md` no existe, se usan los valores por defecto de [reference.md](reference.md): capas primitivo, semántico de sistema, componente y dominio; prefijo de pendientes `PEND`; modos solo cuando constan; valor tal como viene en el export.
- Foundations, áreas y slugs salen de lo que pidan las notas, el export o el usuario. Un export de solo un área no autoriza a documentar el resto del sistema.
- Los ficheros de export de tokens son de solo lectura, igual que `raw/`.

---

## Estructura de Documentación del Proyecto

La raíz predeterminada es `docs/sistema-diseno/`. Si el usuario indica otra ruta en su mensaje, usar la proporcionada. Si las carpetas no existen al momento de escribir, crearlas automáticamente.

```text
docs/sistema-diseno/
├── raw/                         <- Notas originales del usuario (SOLO LECTURA)
├── ordenado/                    <- Notas limpias y acopio fiel
│   ├── <nota>-ordenado.md       <- Salida del comando reorganizar
│   ├── specs/<slug>.md          <- Spec fiel: junta todo lo que consta del componente
│   └── foundations/<slug>.md    <- Acopio fiel de una foundation
├── clasificado/                 <- Salidas del comando clasificar
├── componentes/                 <- Guía publicada del componente, en español (<slug>.md)
├── foundations/                 <- Guías publicadas de foundations (<slug>.md)
│   ├── tokens.md                <- Introducción a los tokens, si consta material para ella
│   ├── tokens/<area>.md         <- Referencia de tokens por área
│   └── convenciones.md          <- Convenciones del proyecto (opcional; no se inventa)
├── reportes/                    <- Reportes diarios agrupados por área (YYYY-MM-DD.md)
├── storybook/                   <- Borradores de contexto para Storybook (<slug>.md)
├── marca/
│   ├── fuente/                  <- Archivos de marca originales (PDF, MD, TXT)
│   └── voz.md                   <- Directrices extraídas de tono y redacción
├── changelog.md                 <- Registro cronológico acumulativo por tipo de cambio
├── deuda.md                     <- Registro centralizado de deuda técnica y tareas
└── pendientes.md                <- Registro único de información por aportar
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
3. Generar un **nuevo archivo** en `docs/sistema-diseno/ordenado/<nombre-original>-ordenado.md` siguiendo la plantilla de `reference.md`. No escribir en `ordenado/specs/`: esa carpeta es solo el acopio por componente.
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
Junta en una spec fiel todo lo que las notas dicen de un componente. No redacta la guía pública.
1. Extraer del raw todas las menciones asociadas al componente solicitado (props, slots, variantes, tokens, estados, eventos, métodos, accesibilidad, buenas prácticas, etc.).
2. Determinar el slug del componente tal como viene en las notas (ej. `badge.md`, `action-button.md`).
3. Crear o actualizar `docs/sistema-diseno/ordenado/specs/<slug>.md` con la plantilla de spec fiel de `reference.md`.
4. Rellenar cada sección con la información encontrada. Todo campo no mencionado en las notas debe quedar explícitamente como `No consta en las notas raw`.
5. No escribir este acopio en `componentes/`. Esa carpeta es solo la guía publicada.
6. Reportar al usuario qué secciones quedaron completas y cuáles en `No consta`.

### 8. `escribir-guia`
Redacta la guía del componente al estilo de una página de design system (Calcite, Material, Atlassian), en español, a partir de la spec fiel.
1. Leer `docs/sistema-diseno/ordenado/specs/<slug>.md`. Si no existe, detenerse y pedir `actualizar-spec` antes. No volver a las notas raw para completar la guía.
2. Crear o actualizar `docs/sistema-diseno/componentes/<slug>.md` con la plantilla de guía de `reference.md`.
3. Escribir solo las secciones que tengan datos reales en la spec. Títulos en español: Descripción general, Uso, Anatomía, Buenas prácticas, Opciones, Comportamiento, Accesibilidad, Referencia de API, Decisiones, Información pendiente.
4. No inventar ejemplos, props, tokens ni recomendaciones. No rellenar huecos con `No consta` dentro del cuerpo: resumirlos una sola vez en **Información pendiente**.
5. Si ya existe una guía, advertir antes de sobrescribir.
6. Reportar qué secciones se publicaron y qué quedó pendiente.

### 9. `preparar-storybook`
Genera el borrador de contexto necesario para documentar el componente en Storybook. No sustituye a la guía.
1. Leer la spec fiel en `docs/sistema-diseno/ordenado/specs/<slug>.md`. Si no existe, detenerse y pedir `actualizar-spec` antes.
2. Generar `docs/sistema-diseno/storybook/<slug>.md` siguiendo la plantilla de `reference.md`.
3. Mapear argTypes preliminares, variantes y estados documentados en la spec.
4. Enlazar la guía publicada en `docs/sistema-diseno/componentes/<slug>.md` si existe. No reescribir ahí el uso, las buenas prácticas ni la referencia de API.
5. Señalar de forma explícita qué props o controles requieren confirmación del desarrollador frente al código fuente (`[No consta en notas / Validar con código]`).

### 10. `clasificar`
Separa notas raw extremadamente mezcladas en ficheros limpios independientes.
1. Leer la nota raw caótica.
2. Identificar bloques temáticos: cambios para changelog, puntos de deuda técnica, especificaciones de componentes y material de foundations o tokens.
3. Generar archivos nuevos en `docs/sistema-diseno/clasificado/` (ej. `cambios-<fecha>.md`, `deuda-<fecha>.md`, `componente-<nombre>.md`, `foundation-<nombre>.md`).
4. **No modificar el fichero raw original.**
5. Presentar un resumen de cómo se distribuyó el contenido y preguntar al usuario si desea ejecutar `update-changelog`, `update-deuda`, `actualizar-spec`, `escribir-guia`, `actualizar-foundation`, `escribir-foundation` o `referencia-tokens` sobre dichos ficheros.

### 11. `actualizar-foundation`
Junta en un acopio fiel todo lo que las fuentes dicen de una foundation. No redacta la guía pública.
1. Leer las notas, capturas y exports que el usuario indique, o los que hablen de esa foundation. Foundations y slug salen de ese material (color, tipografía, espaciado, bordes, layout u otra que conste). No completar una lista fija de foundations.
2. Crear o actualizar `docs/sistema-diseno/ordenado/foundations/<slug>.md` con la plantilla de acopio de `reference.md`.
3. Conservar el detalle íntegro: mediciones completas, notaciones de origen y procedencia. Todo campo sin datos queda como `No consta en las notas raw`.
4. No escribir este acopio en `foundations/` fuera de `ordenado/`. Esa carpeta es solo la guía publicada.
5. Si `convenciones.md` existe, usar sus nombres de foundation y slug. Si no existe, usar el nombre que conste en las fuentes, en minúsculas y con guiones.
6. Reportar qué secciones quedaron completas y cuáles en `No consta`.

### 12. `escribir-foundation`
Redacta la guía publicada de la foundation a partir del acopio fiel.
1. Leer `docs/sistema-diseno/ordenado/foundations/<slug>.md`. Si no existe, detenerse y pedir `actualizar-foundation` antes. No volver a las notas raw para completar la guía.
2. Crear o actualizar `docs/sistema-diseno/foundations/<slug>.md` con la plantilla de guía de foundation de `reference.md`.
3. Responder a qué usar, cuándo y por qué. Publicar solo secciones con datos reales, en el orden de la plantilla. Sin tablas de valores y sin frases sobre la procedencia del contenido.
4. No inventar principios, roles, combinaciones, modos ni limitaciones. Los huecos se resumen una sola vez en **Información pendiente**.
5. Cada hueco nuevo se registra en `docs/sistema-diseno/pendientes.md` con la plantilla de `reference.md`. No reutilizar, renumerar ni borrar IDs. Un pendiente ya abierto se actualiza en sus páginas afectadas; no se duplica. El prefijo es el de `convenciones.md` o, en su defecto, `PEND`.
6. Enlazar la referencia de tokens de `foundations/tokens/<area>.md` solo si ese archivo existe.
7. Si ya existe una guía, advertir antes de sobrescribir.
8. Reportar qué secciones se publicaron, qué quedó pendiente y qué IDs se abrieron o actualizaron.

### 13. `referencia-tokens`
Genera la referencia de tokens de un área desde los exports. No redacta la guía de la foundation.
1. Leer solo los exports que el usuario indique o que `convenciones.md` liste para esa área. No modificar esos ficheros. Si no hay export ni convención que lo localice, detenerse y pedirlo. No buscar tokens en otro sistema.
2. Crear o actualizar `docs/sistema-diseno/foundations/tokens/<area>.md` con la plantilla de referencia de `reference.md`. El área es la pedida, no un catálogo predefinido.
3. Nombres y valores exactos del export. Valor resuelto en la celda y alias entre paréntesis, salvo que `convenciones.md` fije otro formato. No convertir unidades ni espacios de color.
4. Clasificar con `convenciones.md` si existe. Si no existe, aplicar el defecto: semánticos de sistema en **Semánticos**, primitivos en **Primitivos**, tokens de componente fuera de esas tablas y tokens de dominio aparte. Los primitivos no se documentan como consumo directo de producto salvo que las convenciones lo permitan.
5. Modos: columnas solo para los modos que consten en el export o en `convenciones.md`. Sin modos, usar la tabla de una sola columna de valor. No inventar un modo alternativo.
6. Los tokens no válidos van a **Tokens bloqueados**, no a las tablas, y abren o actualizan una entrada en `pendientes.md`.
7. Los tokens de componente se incorporan a `ordenado/specs/<slug>.md`, en Estilos y tokens, sin borrar el resto de la spec. Si la spec no existe, crearla con la plantilla y rellenar solo los tokens que constan; el resto queda en `No consta en las notas raw`. En la referencia del área se listan en **Tokens reubicados**. No se escribe con ellos la guía de `componentes/`.
8. Un grupo de dominio sin destino en `convenciones.md` queda en **Tokens reubicados** con destino pendiente y se pregunta al usuario. No se crea una guía de dominio para alojarlo.
9. Omitir grupos vacíos. Reportar cuántos tokens entraron por capa, cuáles quedaron bloqueados o reubicados y qué pendientes se abrieron.

### 14. `previsualizar`
Muestra la documentación como una página local con pestañas. Es una capa de lectura: no forma parte de los documentos del sistema.
1. No crear, editar, mover, renombrar ni formatear ningún fichero de la raíz de documentación (`docs/sistema-diseno/` o la ruta que indique el usuario). No crear carpetas ahí.
2. No generar HTML, JSON, caché ni ninguna otra salida dentro de esa raíz ni junto a los `.md`.
3. Arrancar el servidor de solo lectura que viaja con la skill (`vista/server.py`, junto a este `SKILL.md`), no con los documentos. La raíz es la del proyecto en curso; si el usuario indicó otra, usar esa.

```bash
python3 "<directorio-de-este-SKILL>/vista/server.py" --raiz "<raiz-de-documentacion>"
```

   Si el puerto `8765` está ocupado, elegir otro con `--puerto`.
4. Abrir en el navegador la URL que imprime el servidor (`http://127.0.0.1:…/`).
5. La vista agrupa por las carpetas que existan (componentes, foundations, tokens, changelog, deuda, pendientes y cualquier otra carpeta con Markdown). No inventa secciones vacías ni nombres de un sistema concreto.
6. `vista/` forma parte de la skill y sí se incluye en el repositorio de la skill. No se copia a la carpeta de documentación ni al repositorio donde se publican los `.md`: ahí solo van esos Markdown. No añadir un `.gitignore` que excluya `vista/` en el repositorio de la skill.

---

## Cierre de Cada Operación

Al concluir la ejecución de cualquier comando, el agente debe presentar un informe de cierre con:
1. **Artefactos procesados y generados:** Lista clara de ficheros leídos y ficheros creados o actualizados.
2. **Restos o elementos sin clasificar:** Si hubo datos que no encajaron en las plantillas, mostrarlos de forma destacada y preguntar al usuario dónde deben archivarse.
3. **Campos con información pendiente:** Indicar los apartados que quedaron marcados con `No consta en las notas raw` y los IDs abiertos o actualizados en `pendientes.md`. La deuda del sistema sigue en `deuda.md`; un hueco de documentación no se registra como deuda.
