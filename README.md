# Design System Personal Manager

> Skill portátil basada en el estándar abierto [Agent Skills](https://agentskills.io) para transformar notas *raw* y apuntes desestructurados de un sistema de diseño en documentación viva, changelog acumulativo, control de deuda técnica y especificaciones de componentes sin inventar información.

---

## Características Principales

- **Fidelidad Absoluta (Anti-Alucinación):** Prohibido inventar datos, props o tokens ficticios. Lo que no conste en las notas se marca explícitamente como `No consta en las notas raw`.
- **Ficheros Raw Intocables:** Tus notas originales en `docs/sistema-diseno/raw/` son estrictamente de solo lectura. Ningún comando reescribe o vacía notas raw.
- **Agnóstico a Marca:** Las guías de voz y tono se inyectan como datos vía `incluir-marca` en `docs/sistema-diseno/marca/voz.md`. Si no existen, se aplica un tono neutro y técnico.
- **Multi-Agente e IDE:** Compatible de forma nativa con **Cursor**, **GitHub Copilot (VS Code)**, **Claude Code**, **OpenAI Codex** y cualquier asistente que soporte la especificación `.agents/skills/`.

---

## Estructura del Repositorio

```text
├── .agents/
│   └── skills/
│       └── design-system-personal-manager/
│           ├── SKILL.md             # Instrucciones maestras del agente y definición de comandos
│           ├── reference.md         # Plantillas exactas para cada documento
│           └── examples.md          # Casos prácticos de notas sin formato y salidas esperadas
│
├── docs/
│   └── sistema-diseno/
│       ├── raw/                     # Notas diarias originales (SOLO LECTURA)
│       ├── ordenado/                # Salidas del comando 'reorganizar'
│       ├── clasificado/             # Salidas del comando 'clasificar'
│       ├── componentes/             # Especificaciones vivas por componente (<slug>.md)
│       ├── reportes/                # Reportes diarios agrupados por área (YYYY-MM-DD.md)
│       ├── storybook/               # Contexto y argTypes para Storybook Docs
│       ├── marca/
│       │   ├── fuente/              # Guías originales de branding (PDF, MD, TXT)
│       │   └── voz.md               # Pautas extraídas de redacción y glosario
│       ├── changelog.md             # Registro cronológico acumulativo por tipo de cambio
│       ├── deuda.md                 # Registro centralizado de deuda técnica y dudas
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
| `actualizar-spec` | Genera o actualiza la spec técnica de un componente (11 secciones) | Escribe en `docs/sistema-diseno/componentes/<slug>.md`. |
| `preparar-storybook` | Prepara `argTypes`, variantes y snippets `.stories.tsx` | Escribe en `docs/sistema-diseno/storybook/<slug>.md`. |
| `generar-mensaje` | Redacta un mensaje resumen con tono de marca para el equipo | **En el chat** (listo para copiar y pegar en Slack/Teams). |
| `incluir-marca` | Ingiere una guía de estilo y extrae directrices de tono y glosario | Guarda fuente en `marca/fuente/` y crea `marca/voz.md`. |
| `clasificar` | Separa notas raw muy complejas en temáticas independientes | Crea archivos nuevos en `docs/sistema-diseno/clasificado/`. |

---

## Flujo de Trabajo Diario

1. **Escribe:** Toma notas libremente durante reuniones o pruebas y guárdalas en `docs/sistema-diseno/raw/notas-hoy.md`.
2. **Fecha:** Pídele al agente: `renombrar-raw`.
3. **Consolida:** Pídele al agente: `update-changelog` y `update-deuda`.
4. **Comunica:** Pídele al agente: `generar-mensaje` para avisar al equipo en Slack o Teams.
5. **Especifica:** Cuando definas componentes, pide `actualizar-spec [componente]` y luego `preparar-storybook [componente]`.

---

## Licencia

MIT
