# Plantillas de Referencia — Skill Notas de Sistema de Diseño

Este archivo define la estructura exacta que deben seguir todos los documentos generados por la skill `design-system-notes`. 

---

## Reglas Generales de Aplicación

1. **Fidelidad Absoluta**: Nunca inventar valores, propiedades, tokens, decisiones ni datos ficticios. En la spec fiel (`ordenado/specs/`), si un campo no aparece en las notas raw, debe indicarse explícitamente como `No consta en las notas raw`. En la guía publicada (`componentes/`), no se escribe ese marcador dentro de la sección: el apartado se omite y el hueco se resume en **Información pendiente**.
2. **Omisión de Secciones Vacías**: En el **Reporte Diario** y en el **Changelog**, una sección SOLO se incluye si ese día existen notas correspondientes a esa área o tipo de cambio. No dejar secciones vacías.
3. **Gestión de Restos**: Todo fragmento de información que no encaje de forma clara en las secciones predefinidas debe colocarse en un apartado final de **Resto / Sin clasificar**. Al finalizar el comando, el agente debe señalarlo explícitamente y preguntar al usuario dónde desea clasificarlo.
4. **Voz de Marca**: Si existe `docs/sistema-diseno/marca/voz.md`, se aplican sus directrices a títulos, conectores y mensajes sin alterar la veracidad del contenido técnico. Si no existe, se emplea un tono profesional, claro y neutro.

---

## 1. Plantilla: Reporte Diario de Cambios

**Ruta de destino:** `docs/sistema-diseno/reportes/YYYY-MM-DD.md`  
**Criterio de agrupación:** Por **Área** del sistema de diseño.

```markdown
# Reporte Diario — Sistema de Diseño

- **Fecha:** YYYY-MM-DD
- **Autor:** @autor
- **Fuentes procesadas:** [Lista de ficheros raw leídos]

## Resumen Ejecutivo
[2 a 4 frases concisas que resuman los hitos más relevantes del día. Sin adornos innecesarios.]

<!-- A continuación, solo se incluyen las áreas que contengan notas en el día -->

## Componentes
### [Nombre del Componente]
- **Cambio / Novedad:** [Descripción fiel a las notas]
- **Detalles técnicos:** [Props, estados, variantes mencionadas o "No consta"]
- **Impacto:** [Si consta en notas o "No consta"]

## Tokens y Fundamentos
- **Tokens afectados:** [Color, tipografía, espaciado, elevación, breakpoints...]
- **Modificación:** [Descripción del cambio extraída de las notas]

## Documentación
- [Nuevas guías, revisiones de textos o lineamientos anotados]

## Accesibilidad
- [Criterios WCAG, navegación por teclado, contraste o roles indicados]

## Deuda Técnica
> ⚠️ Se ha identificado o registrado deuda técnica durante la jornada. El detalle completo se gestiona en `docs/sistema-diseno/deuda.md`.
- **Aviso:** [Breve resumen de 1 línea por cada deuda registrada]

## Contenido y Redacción
- [Directrices de microcopy, naming o etiquetas anotadas]

## Patrones y Flujos
- [Interacciones compuestas, modales, navegación o flujos de usuario]

## Resto / Sin Clasificar
<!-- Si nada queda suelto, esta sección no se escribe -->
- [Fragmento textual o información que no encaja en las áreas anteriores para revisión con el usuario]
```

---

## 2. Plantilla: Entrada de Changelog

**Ruta de destino:** `docs/sistema-diseno/changelog.md`  
**Criterio de agrupación:** Por **Tipo de Cambio**.  
**Modo de actualización:** Solo añadir al inicio o bajo el historial cronológico descendente. No sobrescribir entradas anteriores.

```markdown
## [YYYY-MM-DD] - @autor

### Añadido
- [Nuevo componente, variante, token, historia o funcionalidad que no existía]

### Cambiado
- [Modificación en comportamiento, visual, tokens o API de elementos existentes]

### Corregido
- [Corrección de bugs visuales, accesibilidad, tipografía o comportamiento]

### Eliminado
- [Elementos, tokens o propiedades que han sido removidos del sistema]

### Documentación
- [Actualizaciones en guías de uso, specs o documentación técnica]

### Deprecado
- [Elementos marcados para futura eliminación, con alternativa si consta en notas]

### Sin clasificar
- [Elementos que el usuario debe ubicar tras la revisión]
```

---

## 3. Plantilla: Fichero Central de Deuda Técnica

**Ruta de destino:** `docs/sistema-diseno/deuda.md`  
**Modo de actualización:** Añadir nuevas entradas numeradas secuencialmente bajo la sección correspondiente.

```markdown
# Registro Central de Deuda Técnica — Sistema de Diseño

Este documento consolida la deuda técnica, inconsistencias y tareas pendientes detectadas durante el trabajo en el sistema de diseño.

---

## Deuda Confirmada

### [DEUDA-YYYYMMDD-01] [Título breve y descriptivo del problema]
- **Fecha de registro:** YYYY-MM-DD
- **Detectado por:** @autor
- **Origen:** [Fichero raw de procedencia]
- **Área afectada:** [Componentes / Tokens / Accesibilidad / Arquitectura / Documentación]
- **Descripción del problema:** [Hecho concreto y técnico extraído de las notas]
- **Impacto / Riesgo:** [Consecuencia técnica o de diseño, o "No consta"]
- **Solución propuesta:** [Si las notas indican una propuesta o "No consta"]
- **Estado:** Pendiente

---

## Posible Deuda / Para Confirmar
<!-- Aquí se registran menciones informales como "habría que revisar...", "ojo con...", o dudas -->

### [POSIBLE-YYYYMMDD-01] [Título o asunto detectado]
- **Fecha de registro:** YYYY-MM-DD
- **Detectado por:** @autor
- **Origen:** [Fichero raw de procedencia]
- **Mención textual en notas:** "[Cita o paráfrasis fiel]"
- **Duda a resolver:** [Qué debe aclarar el equipo antes de confirmarlo como deuda]
- **Estado:** En evaluación
```

---

## 4. Plantilla: Spec fiel del componente

**Ruta de destino:** `docs/sistema-diseno/ordenado/specs/<slug-componente>.md`  
**Regla:** Este archivo junta, sin redactar para publicación, todo lo que las notas dicen del componente. El slug se toma del nombre en minúsculas y guiones (ej. `button-action.md`). Si un campo no está en las notas raw, colocar `No consta en las notas raw`. No escribir esta spec en `componentes/`.

```markdown
# Spec: [Nombre del Componente]

- **Slug:** `<slug>`
- **Estado de la spec:** [Borrador / Estable / En revisión]
- **Última actualización:** YYYY-MM-DD por @autor
- **Fuentes:** [Ficheros raw de los que se extrajo]

---

## 1. Descripción y propósito
[Finalidad del componente según las notas. Si no consta: "No consta en las notas raw."]

## 2. Cuándo usar y cuándo no usar
- **Usar cuando:** [Casos de uso mencionados o "No consta"]
- **No usar cuando:** [Casos no recomendados o "No consta"]

## 3. Anatomía
[Elementos visuales que conforman el componente: icono, etiqueta, contenedor, etc.]

## 4. Variantes y opciones
| Variante u opción | Descripción | Valores válidos |
| :--- | :--- | :--- |
| [Nombre] | [Detalle o "No consta"] | [Valores o "No consta"] |

## 5. Estados
- **Reposo:** [Comportamiento visual o "No consta"]
- **Hover:** [Detalle o "No consta"]
- **Foco:** [Detalle o "No consta"]
- **Pulsado:** [Detalle o "No consta"]
- **Deshabilitado:** [Detalle o "No consta"]
- **Cargando:** [Detalle o "No consta"]
- **Error:** [Detalle o "No consta"]

## 6. Propiedades
| Propiedad | Tipo | Obligatoria | Valor por defecto | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| [prop] | [tipo o "No consta"] | [Sí/No o "No consta"] | [default o "No consta"] | [descripción o "No consta"] |

## 7. Slots
| Slot | Descripción |
| :--- | :--- |
| [nombre o "No consta"] | [detalle o "No consta"] |

## 8. Estilos y tokens
- **Color:** [Tokens de fondo, borde, texto o "No consta"]
- **Espaciado:** [Tokens o valores o "No consta"]
- **Tipografía:** [Tokens de fuente, peso, tamaño o "No consta"]
- **Borde y radio:** [Tokens o "No consta"]
- **Sombra y elevación:** [Tokens o "No consta"]

## 9. Eventos
| Evento | Cuándo se emite |
| :--- | :--- |
| [nombre o "No consta"] | [detalle o "No consta"] |

## 10. Métodos
| Método | Descripción |
| :--- | :--- |
| [nombre o "No consta"] | [detalle o "No consta"] |

## 11. Accesibilidad
- **Rol:** [Rol semántico o "No consta"]
- **Teclado:** [Tecla y función, o "No consta"]
- **Contraste:** [Datos de contraste o "No consta"]

## 12. Comportamiento
[Comportamiento ante clic, scroll, responsive o animaciones indicadas, o "No consta".]

## 13. Buenas prácticas
- **Hacer:** [Práctica recomendada o "No consta"]
- **Evitar:** [Práctica desaconsejada o "No consta"]

## 14. Decisiones
[Razones o acuerdos del equipo registrados en las notas raw, o "No consta".]

## 15. Información pendiente / resto
[Dudas o anotaciones del componente que no encajan en los apartados anteriores.]
```

---

## 5. Plantilla: Guía del componente

**Ruta de destino:** `docs/sistema-diseno/componentes/<slug-componente>.md`  
**Fuente única:** `docs/sistema-diseno/ordenado/specs/<slug>.md`. Si la spec no existe, no generar la guía.  
**Idioma:** español. Los títulos de sección se escriben como en esta plantilla.  
**Regla de lectura:** se redacta como la página de un componente en un design system. Solo entran secciones con datos reales en la spec. Un apartado entero en `No consta en las notas raw` no se publica. Los huecos se resumen al final, sin repetir el marcador dentro del cuerpo.

```markdown
# [Nombre del componente]

[Una o dos frases de propósito, copiadas en sentido de la spec. Sin añadir usos que no consten.]

- **Slug:** `<slug>`
- **Estado:** [El estado de la spec]
- **Última actualización:** YYYY-MM-DD por @autor
- **Fuente:** `docs/sistema-diseno/ordenado/specs/<slug>.md`

## Descripción general
[Qué es y para qué sirve, solo con lo que dice la spec.]

## Uso
- **Usar cuando:** [Casos que constan]
- **No usar cuando:** [Casos que constan. Omitir la viñeta si no hay ninguno.]

## Anatomía
[Partes del componente que constan en la spec.]

## Buenas prácticas
**Hacer**
- [Práctica que consta]

**Evitar**
- [Práctica que consta. Omitir el bloque si no hay ninguna.]

## Opciones
[Variantes, tamaños y configuración que constan.]

| Variante u opción | Descripción | Valores |
| :--- | :--- | :--- |
| [Nombre] | [Detalle] | [Valores, si constan] |

## Comportamiento
[Estados e interacción que constan. Un estado sin datos no se lista.]

## Accesibilidad
- **Rol:** [Si consta]
- **Teclado:**

| Tecla | Función |
| :--- | :--- |
| [Tecla] | [Función] |

- **Contraste:** [Si consta]

## Referencia de API

### Propiedades
| Propiedad | Tipo | Obligatoria | Valor por defecto | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| [prop] | [tipo] | [Sí/No] | [default] | [descripción] |

### Slots
| Slot | Descripción |
| :--- | :--- |
| [nombre] | [detalle] |

### Estilos y tokens
- **Color:** [Tokens que constan]
- **Espaciado:** [Tokens o valores que constan]
- **Tipografía:** [Tokens que constan]
- **Borde y radio:** [Tokens que constan]
- **Sombra y elevación:** [Tokens que constan]

### Eventos
| Evento | Cuándo se emite |
| :--- | :--- |
| [nombre] | [detalle] |

### Métodos
| Método | Descripción |
| :--- | :--- |
| [nombre] | [detalle] |

## Decisiones
[Acuerdos de la spec que explican una opción de la guía.]

## Información pendiente
- [Hueco de la spec que un lector de la guía necesita saber que falta]
```

---

## 6. Plantilla: Borrador para Storybook

**Ruta de destino:** `docs/sistema-diseno/storybook/<slug-componente>.md`  
**Fuente:** la spec fiel en `docs/sistema-diseno/ordenado/specs/<slug>.md`.  
**Finalidad:** Contexto para crear `.stories.tsx` y el sample interactivo. La guía de uso, las buenas prácticas y la referencia de API viven en `componentes/` y no se reescriben aquí.

```markdown
# Contexto de Storybook: [Nombre del componente]

> Borrador para montar historias y controles. Los campos marcados como `[No consta en notas / Validar con código]` deben contrastarse con el código del componente.
>
> Guía publicada: `docs/sistema-diseno/componentes/<slug>.md`

## Meta
- **Title:** `Componentes/[Categoría]/[Nombre]`
- **Component:** `[NombreComponente]`

## ArgTypes y props para los controles
```typescript
// Mapeo inicial a partir de la spec fiel. No añadir props que no consten.
export const argTypes = {
  // propName: { control: 'select', options: [...], description: '...' },
};
```

## Historias recomendadas
1. **Base:** componente en su estado de reposo.
2. **Opciones:** [Variantes documentadas en la spec].
3. **Estados:** [Estados documentados en la spec].
4. **Casos límite:** [Casos especiales o errores que consten en la spec].

## Fragmentos de historias
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { [NombreComponente] } from './[NombreComponente]';

const meta: Meta<typeof [NombreComponente]> = {
  title: 'Componentes/[NombreComponente]',
  component: [NombreComponente],
};
export default meta;

type Story = StoryObj<typeof [NombreComponente]>;

export const Base: Story = {
  args: {
    // args tomados de la spec
  },
};
```
```

---

## 7. Plantilla: Directrices de Voz y Tono de Marca

**Ruta de destino:** `docs/sistema-diseno/marca/voz.md`  
**Origen:** Extraído exclusivamente del material provisto por el usuario vía `incluir-marca` (texto, markdown o PDF).

```markdown
# Guía de Voz y Tono del Sistema de Diseño

- **Documento fuente:** [Nombre del archivo fuente guardado en docs/sistema-diseno/marca/fuente/]
- **Fecha de incorporación:** YYYY-MM-DD
- **Registrado por:** @autor

---

## 1. Personalidad y Tono
[Principios fundamentales de la marca reflejados en el texto fuente: ej. cercano, riguroso, minimalista, dinámico.]

## 2. Criterios de Redacción para Documentación
- **Tratamiento:** [Tú / Usted / Impersonal según la guía]
- **Estructura de oraciones:** [Frases cortas, voz activa, etc.]
- **Uso de mayúsculas y puntuación:** [Reglas de estilo de la marca]

## 3. Glosario y Vocabulario Clave
| Término Recomendado | Término Evitado | Motivo / Contexto |
| :--- | :--- | :--- |
| [Término] | [Evitar] | [Justificación de marca] |

## 4. Aplicación en Mensajes y Actualizaciones
[Pautas para los resúmenes y mensajes hacia el equipo de desarrollo y diseño.]
```

---

## 8. Plantilla: Nota Reorganizada

**Ruta de destino:** `docs/sistema-diseno/ordenado/<nombre-original>-ordenado.md`  
**Regla de oro:** El archivo raw original NO se modifica. Se crea este nuevo fichero con la información limpia, con títulos lógicos y sintaxis pulida, preservando el 100% de los datos.

```markdown
# [Título Principal Inferido del Contenido] — Nota Reorganizada

- **Fichero origen:** `docs/sistema-diseno/raw/<nombre-original>.md`
- **Fecha de reorganización:** YYYY-MM-DD
- **Procesado por:** @autor

---

## [Sección Temática 1]
- [Puntos limpios, redactados con claridad pero sin perder datos técnicos]

## [Sección Temática 2]
- [Detalles, valores numéricos, nombres de tokens conservados íntegros]

## Deuda / Observaciones Detectadas
- [Avisos o tareas que se encontraban dispersas en la nota raw]

## Resto / Notas Adicionales
- [Cualquier anotación que no encajaba en los bloques anteriores]
```

---

## 9. Plantilla: Mensaje de Update para Compañeros

**Destino:** Se imprime directamente en el chat para que el usuario copie y pegue (Slack, Microsoft Teams, Email, etc.). NO crea archivo en disco.

```markdown
🚀 **Actualización Sistema de Diseño — [DD/MM/YYYY]**

¡Hola equipo! Os dejamos el resumen de los cambios incorporados hoy:

**Lo más destacado:**
• [1-3 puntos clave redactados de forma clara según el tono de marca]

📦 **Novedades en Componentes:**
• [Componente]: [Breve resumen del cambio]

🎨 **Tokens y Estilos:**
• [Cambios de tokens o fundamentos, si los hay]

⚠️ **Avisos importantes / Deuda:**
• [Alertas de breaking changes, migraciones o deuda relevante]

📄 *Podéis consultar el changelog completo en `docs/sistema-diseno/changelog.md`.*
```
