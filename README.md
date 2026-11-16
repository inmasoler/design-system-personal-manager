# Design System Personal Manager

> Skill portátil basada en el estándar abierto [Agent Skills](https://agentskills.io) para transformar notas *raw* y apuntes desestructurados de un sistema de diseño en documentación viva, changelog acumulativo, control de deuda técnica, una spec fiel por componente, la guía publicada de ese componente, las guías de foundations y las referencias de tokens, sin inventar información. No está atada a una empresa ni a un design system concreto: las convenciones de cada proyecto se leen como datos.

---

## Características Principales

- **Fidelidad Absoluta (Anti-Alucinación):** Prohibido inventar datos, props o tokens ficticios. Lo que no conste en las notas se marca explícitamente como `No consta en las notas raw`.
- **Ficheros Raw Intocables:** Tus notas originales en `docs/sistema-diseno/raw/` son estrictamente de solo lectura. Ningún comando reescribe o vacía notas raw.
- **Agnóstico a Marca:** Las guías de voz y tono se inyectan como datos vía `incluir-marca` en `docs/sistema-diseno/marca/voz.md`. Si no existen, se aplica un tono neutro y técnico.
- **Convenciones por Proyecto:** Las decisiones propias de cada sistema (modos, clasificación de tokens, nombres, prefijo de pendientes) se leen del archivo de convenciones localizado. Se busca en `guias/foundations/`, también con prefijo numérico (`01-convenciones.md`), y en `guias/convenciones.md`. Si no existe, se aplican los valores por defecto de la skill y no se copia el esquema de otro sistema. El prefijo numérico de una guía no pasa al acopio ni a la referencia de tokens.
- **Vista aparte:** `previsualizar` abre solo los documentos publicados como una página local con pestañas. No escribe en la carpeta de documentación. Esa carpeta se puede subir a otro repositorio sin arrastrar la vista.
- **Multi-Agente e IDE:** Compatible de forma nativa con **Cursor**, **GitHub Copilot (VS Code)**, **Claude Code**, **OpenAI Codex** y cualquier asistente que soporte la especificación `.agents/skills/`.

---

## Estructura del Repositorio

```text
├── .agents/
│   └── skills/
│       └── design-system-personal-manager/
│           ├── SKILL.md             # Instrucciones maestras del agente y definición de comandos
│           ├── reference.md         # Plantillas exactas para cada documento
│           ├── examples.md          # Casos prácticos de notas sin formato y salidas esperadas
│           └── vista/               # Página local. Va en el repo de la skill, no con los .md
│
├── docs/
│   └── sistema-diseno/
│       ├── raw/                     # Notas diarias originales (SOLO LECTURA)
│       ├── ordenado/                # Notas limpias y acopio fiel
│       │   ├── <nota>-ordenado.md   # Salida de 'reorganizar'
│       │   ├── specs/<slug>.md      # Acopio fiel de 'actualizar-spec'
│       │   └── foundations/<slug>.md # Acopio fiel de 'actualizar-foundation'
│       ├── clasificado/             # Salidas del comando 'clasificar'
│       ├── guias/                   # Páginas publicadas que muestra la vista
│       │   ├── convenciones.md      # Opcional, si no está en foundations/
│       │   ├── vocabulario.md       # Vocabulario publicado (opcional)
│       │   ├── componentes/<slug>.md
│       │   └── foundations/
│       │       ├── <guia>.md        # Puede llevar prefijo, p. ej. 02-colores.md
│       │       ├── convenciones.md  # O 01-convenciones.md
│       │       ├── tokens.md        # Introducción a los tokens, si hay material
│       │       └── tokens/<area>.md # Referencia de tokens, sin prefijo numérico
│       ├── reportes/                # Reportes diarios agrupados por área (YYYY-MM-DD.md)
│       ├── storybook/               # Contexto y argTypes para Storybook Docs
│       ├── marca/
│       │   ├── fuente/              # Guías originales de branding (PDF, MD, TXT)
│       │   └── voz.md               # Pautas extraídas de redacción y glosario
│       ├── changelog.md             # Registro cronológico del sistema de diseño
│       ├── changelog-documentacion.md # Registro de la documentación y del gestor
│       ├── deuda.md                 # Registro centralizado de deuda técnica y dudas
│       ├── pendientes.md            # Registro único de información por aportar
│       └── comandos.md              # Glosario rápido de uso para humanos
│
└── README.md
```

---

## Comandos Disponibles

Ejecuta cualquiera de estos comandos directamente en el chat con tu agente:

| Comando | Acción principal | Destino / Salida |
| :--- | :--- | :--- |
| `renombrar-raw` | Estandariza el nombre a `<nombre>-<DDMMYYYY>.md` | Renombra el raw en disco (contenido 100% intacto). |
| `reorganizar` | Limpia y estructura una nota raw caótica | Crea un nuevo archivo en `docs/sistema-diseno/ordenado/`. |
| `update-changelog` | Clasifica cambios del día por tipo y genera reporte diario por área | Actualiza `changelog.md` y crea `reportes/YYYY-MM-DD.md`. |
| `update-deuda` | Centraliza problemas, fallos y dudas en el registro de deuda | Añade ítems a `docs/sistema-diseno/deuda.md`. |
| `actualizar-spec` | Junta en una spec fiel todo lo que las notas dicen de un componente | Escribe en `docs/sistema-diseno/ordenado/specs/<slug>.md`. |
| `escribir-guia` | Redacta la guía publicada del componente, en español, solo con lo que consta en la spec | Escribe en `docs/sistema-diseno/guias/componentes/<slug>.md`. |
| `actualizar-foundation` | Junta en un acopio fiel todo lo que consta de una foundation | Escribe en `docs/sistema-diseno/ordenado/foundations/<slug>.md`. |
| `escribir-foundation` | Redacta la guía publicada de la foundation, solo con lo que consta en el acopio | Escribe en `docs/sistema-diseno/guias/foundations/<guia>.md` y actualiza `pendientes.md`. |
| `referencia-tokens` | Genera la referencia de tokens de un área desde los exports | Escribe en `docs/sistema-diseno/guias/foundations/tokens/<area>.md`. |
| `preparar-storybook` | Prepara `argTypes`, variantes y fragmentos `.stories.tsx` | Escribe en `docs/sistema-diseno/storybook/<slug>.md`. |
| `generar-mensaje` | Redacta un mensaje resumen con tono de marca para el equipo | **En el chat** (listo para copiar y pegar en Slack/Teams). |
| `incluir-marca` | Ingiere una guía de estilo y extrae directrices de tono y glosario | Guarda fuente en `marca/fuente/` y crea `marca/voz.md`. |
| `clasificar` | Separa notas raw muy complejas en temáticas independientes | Crea archivos nuevos en `docs/sistema-diseno/clasificado/`. |
| `previsualizar` | Abre los documentos publicados como una página local con pestañas | No escribe archivos. Solo lee la allowlist (`guias/` y los registros de la raíz). El servidor vive en la skill. |

---

## Flujo de Trabajo Diario

1. **Escribe:** Toma notas libremente durante reuniones o pruebas y guárdalas en `docs/sistema-diseno/raw/notas-hoy.md`.
2. **Fecha:** Pídele al agente: `renombrar-raw`.
3. **Consolida:** Pídele al agente: `update-changelog` y `update-deuda`.
4. **Comunica:** Pídele al agente: `generar-mensaje` para avisar al equipo en Slack o Teams.
5. **Documenta el componente:** Pide `actualizar-spec [componente]`, después `escribir-guia [componente]` y, cuando toque el sample, `preparar-storybook [componente]`.
6. **Documenta una foundation:** Pide `actualizar-foundation [foundation]`, después `escribir-foundation [foundation]` y `referencia-tokens [área]` cuando haya un export nuevo. El nombre es el de ese sistema, no uno prefijado por la skill.

---

## Licencia

MIT
