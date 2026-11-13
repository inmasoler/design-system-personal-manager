# Plantillas de Referencia — Skill Notas de Sistema de Diseño

Este archivo define la estructura exacta que deben seguir todos los documentos generados por la skill `design-system-personal-manager`. 

---

## Reglas Generales de Aplicación

1. **Fidelidad Absoluta**: Nunca inventar valores, propiedades, tokens, decisiones ni datos ficticios. En el acopio fiel (`ordenado/specs/` y `ordenado/foundations/`), si un campo no aparece en las notas raw, debe indicarse explícitamente como `No consta en las notas raw`. En las páginas publicadas (`componentes/` y `foundations/`), no se escribe ese marcador dentro de la sección: el apartado se omite y el hueco se resume en **Información pendiente**.
2. **Omisión de Secciones Vacías**: En el **Reporte Diario** y en el **Changelog**, una sección SOLO se incluye si ese día existen notas correspondientes a esa área o tipo de cambio. No dejar secciones vacías. En la referencia de tokens se omite igual cualquier grupo vacío.
3. **Gestión de Restos**: Todo fragmento de información que no encaje de forma clara en las secciones predefinidas debe colocarse en un apartado final de **Resto / Sin clasificar**. Al finalizar el comando, el agente debe señalarlo explícitamente y preguntar al usuario dónde desea clasificarlo.
4. **Voz de Marca**: Si existe `docs/sistema-diseno/marca/voz.md`, se aplican sus directrices a títulos, conectores y mensajes sin alterar la veracidad del contenido técnico. Si no existe, se emplea un tono profesional, claro y neutro.
5. **Convenciones del Proyecto**: Si existe `docs/sistema-diseno/foundations/convenciones.md`, las plantillas 10 a 12 se rellenan con sus modos, clasificación de grupos, formato de valores y prefijo de pendientes. Ese fichero lo escribe el usuario, o el agente a petición suya con datos confirmados por él. La skill lo lee y no lo deduce. No se copian nombres, modos ni prefijos de otra empresa o de otro design system.
6. **Valores por defecto sin convenciones**: Si `convenciones.md` no existe, no se inventa uno durante el comando. Se aplican estos defectos, y solo a la foundation o al área pedida:
   - No hay lista cerrada de foundations, áreas ni nombres de token.
   - Modos: solo los que consten en las notas o en el export. Si no hay, la referencia usa la tabla sin columnas de modo.
   - Capas: primitivos, semánticos de sistema, componente y dominio. Los primitivos no se consumen directamente en producto.
   - Valor: el del export, resuelto en la celda y con el alias entre paréntesis. No se convierten unidades ni espacios de color.
   - Prefijo de pendientes: `PEND`.
   - Los exports de tokens son de solo lectura.

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

---

## 10. Plantilla: Acopio fiel de la foundation

**Ruta de destino:** `docs/sistema-diseno/ordenado/foundations/<slug>.md`  
**Regla de lectura:** junta todo lo que consta de la foundation, con el detalle íntegro. Aquí sí se conservan mediciones completas, notaciones de origen y procedencia. Todo campo sin datos queda como `No consta en las notas raw`. El nombre de la foundation y el slug salen de las fuentes o de `convenciones.md`, no de una lista fija.

```markdown
# Acopio: [Nombre de la foundation]

- **Slug:** `<slug>`
- **Fecha:** YYYY-MM-DD
- **Autor:** @autor
- **Fuentes procesadas:** [Ficheros raw, notas ordenadas, exports y capturas leídos]

## 1. Propósito y principios
[Qué resuelve y qué criterios la guían, o "No consta en las notas raw"]

## 2. Construcción
- **Escalas / familias:** [Detalle o "No consta"]
- **Capas:** [Primitivos, semánticos, otras o "No consta"]
- **Unidades:** [Detalle o "No consta"]
- **Método de construcción:** [Detalle o "No consta"]

## 3. Roles y usos
| Rol o token | Uso que consta | Restricción que consta | Origen |
| :--- | :--- | :--- | :--- |
| [rol] | [uso o "No consta"] | [restricción o "No consta"] | [fichero] |

## 4. Combinaciones
[Parejas o tríos fondo/contenido/borde, estilos y contextos, con su resultado si consta]

## 5. Modos y variantes
[Qué modos existen, qué cambia en cada uno y cómo se seleccionan, o "No consta"]

## 6. Estados interactivos
[Reglas por estado, o "No consta"]

## 7. Accesibilidad y mediciones
[Objetivos, mediciones completas con sus valores exactos y qué combinaciones cubren]

## 8. Implementación
- **Diseño:** [Colecciones, modos, variables o "No consta"]
- **Código:** [Nombres exportados, formato, unidad o "No consta"]

## 9. Limitaciones y excepciones
[Detalle íntegro de cada limitación: valores, alcance, propósito aceptado, revisión propuesta]

## 10. Decisiones
[Acuerdos con fecha y origen]

## 11. Procedencia y notas de origen
[Qué aportó cada fuente; denominaciones distintas para una misma cosa; notaciones del origen]

## 12. Información pendiente / resto
- [Hueco o fragmento sin clasificar, con el ID de pendiente si ya existe]
```

---

## 11. Plantilla: Guía de foundation

**Ruta de destino:** `docs/sistema-diseno/foundations/<slug>.md`  
**Fuente única:** `docs/sistema-diseno/ordenado/foundations/<slug>.md`. Si el acopio no existe, no generar la guía.  
**Idioma:** español. Los títulos de sección se escriben como en esta plantilla y en este orden.  
**Regla de lectura:** responde a qué usar, cuándo y por qué. Solo entran secciones con datos reales en el acopio. No contiene tablas de valores ni frases sobre la procedencia del contenido. Los huecos se resumen al final, una sola vez. Los modos, roles y grupos son los que consten, no un esquema de un sistema concreto.

```markdown
# [Nombre de la foundation]

[Una o dos frases: qué resuelve esta foundation y para quién.]

- **Estado:** [Borrador | En revisión | Estable | Obsoleto]
- **Última actualización:** YYYY-MM-DD por @autor
- **Fuentes:** `docs/sistema-diseno/ordenado/foundations/<slug>.md`
- **Referencia de tokens:** [Enlace a `tokens/<area>.md`]

## Principios
- **[Principio].** [Qué implica en la práctica.]

## Cómo está construido
[Anatomía del sistema: escalas, familias, capas y unidades. Resumen del porqué técnico, sin tablas de valores.]

## Cómo usarlo

### [Grupo de roles]
| Rol | Úsalo para | No lo uses para | Token |
| :--- | :--- | :--- | :--- |
| [rol] | [uso que consta] | [restricción que consta] | `[token]` |

### Combinaciones
| Fondo | Contenido | Borde | Contraste | Estado |
| :--- | :--- | :--- | :--- | :--- |
| `[token]` | `[token]` | `[token]` | [ratio medido] | [Verificado / Aceptado con limitación] |

## Modos y variantes
| Modo | Qué cambia | Qué se mantiene | Cómo se activa |
| :--- | :--- | :--- | :--- |
| [modo] | [detalle] | [detalle] | [detalle] |

## Estados interactivos
[La regla general de default, hover, focus, pressed y disabled. No el listado token a token.]

## Accesibilidad
- **Objetivo:** [Criterio]
- **Verificado:** [Combinaciones o estilos comprobados]
- **Sin verificar:** [Lo que queda fuera]

## Correcto e incorrecto
| Correcto | Incorrecto |
| :--- | :--- |
| [Ejemplo que consta] | [Ejemplo que consta] |

## Implementación
- **Diseño:** [Colección y modo; cómo aplicar la variable]
- **Código:** [Nombre exportado, formato y unidad; ejemplo mínimo que conste]

## Limitaciones conocidas
| Limitación | Alcance | Decisión | Revisar cuando |
| :--- | :--- | :--- | :--- |
| [Resumen con una cifra como máximo] | [Dónde aplica] | [Aceptada / En revisión] | [Condición] |

El detalle de las mediciones está en [el acopio o registro de decisiones].

## Relacionado
- [Componentes que la aplican]
- [Registro de decisiones]

## Información pendiente
- [[ID](../pendientes.md#id): hueco que un lector de la guía necesita saber que falta]
```

---

## 12. Plantilla: Referencia de tokens

**Ruta de destino:** `docs/sistema-diseno/foundations/tokens/<area>.md`  
**Fuente:** exports de tokens del área (solo lectura).  
**Regla de lectura:** responde a cómo se llama cada token y cuánto vale. Solo tokens primitivos y semánticos de sistema, salvo que `convenciones.md` clasifique de otro modo. Los tokens de componente van a la spec y la guía de su componente. Valor resuelto en la celda y alias entre paréntesis. El área y los nombres de modo son los del export o de las convenciones.

````markdown
# Tokens — [Área]

[Una frase que describe el contenido.] Para saber cuándo usar cada token, consulta la [guía de [Área]](../<slug>.md).

- **Estado:** [Borrador | Estable]
- **Última actualización:** YYYY-MM-DD por @autor
- **Fuentes:** [Ficheros de tokens]
- **Modos:** [Base] y [Alternativo] <!-- omitir si el área no tiene modos -->

## Semánticos

### [grupo]

<!-- Área con modos -->
| Muestra | Token | Uso | [Modo base] | [Modo alternativo] |
| :--- | :--- | :--- | :--- | :--- |
| | `grupo.rol` | [una línea o —] | `valor` (`{alias}`) | `valor` (`{alias}`) o `=` |

<!-- Área sin modos -->
| Token | Uso | Valor |
| :--- | :--- | :--- |
| `grupo.rol` | [una línea o —] | `valor` (`{alias}`) |

## Primitivos

> Los primitivos no se consumen directamente en producto. Usa los semánticos.

### [familia]
| Muestra | Token | Valor |
| :--- | :--- | :--- |
| | `familia.paso` | `valor` |

## Tokens bloqueados
<!-- Solo si existen tokens no válidos en el export. No se listan en las tablas anteriores. -->
| Token | Motivo | Pendiente |
| :--- | :--- | :--- |
| `grupo.rol` | [Motivo breve] | [ID](../../pendientes.md#id) |

## Tokens reubicados
<!-- Solo si el export del área contiene tokens de componente o de dominio. -->
| Grupo | Destino |
| :--- | :--- |
| `grupo` | [Enlace a la guía del componente o del dominio] |

## Información pendiente
- [[ID](../../pendientes.md#id): hueco que afecta a esta referencia]
````

Si `convenciones.md` permite consumir primitivos en producto, no se escribe la cita de esta sección.

---

## 13. Plantilla: Registro de pendientes

**Ruta de destino:** `docs/sistema-diseno/pendientes.md`  
**Modo de actualización:** añadir entradas con ID secuencial. No reutilizar, renumerar ni borrar. Un pendiente resuelto pasa a la sección **Resueltos** con su fecha. El prefijo sale de `convenciones.md`; si no hay convenciones, es `PEND`. Los problemas del sistema no se anotan aquí: van a `deuda.md`.

```markdown
# Registro de Pendientes — Sistema de Diseño

Información que falta por aportar para completar la documentación. Los problemas del sistema se gestionan en `deuda.md`.

---

## Abiertos

### [PREFIJO-01] [Título breve]
- **Fecha de registro:** YYYY-MM-DD
- **Registrado por:** @autor
- **Qué falta:** [Hueco concreto]
- **Qué hay que aportar:** [Dato, decisión o archivo necesario]
- **Quién lo aporta:** [Persona o rol, o "No consta"]
- **Páginas afectadas:** [Lista de rutas]
- **Deuda relacionada:** [ID de `deuda.md` o "Ninguna"]

---

## Resueltos

### [PREFIJO-00] [Título breve]
- **Fecha de resolución:** YYYY-MM-DD
- **Resolución:** [Qué se aportó y dónde quedó documentado]
```

---

## 14. Plantilla: Convenciones del proyecto

**Ruta de destino:** `docs/sistema-diseno/foundations/convenciones.md`  
**Quién lo escribe:** el usuario, o el agente a petición suya con datos confirmados por él. La skill lo lee, no lo deduce. Todas las celdas son del proyecto en curso. Ningún ejemplo de esta plantilla se copia como si fuera un dato real.

```markdown
# Convenciones de Foundations — [Nombre del sistema]

- **Última actualización:** YYYY-MM-DD por @autor

## 1. Foundations y slugs
| Foundation | Slug de la guía | Referencias de tokens | Notas |
| :--- | :--- | :--- | :--- |
| [nombre] | `<slug>` | `tokens/<area>.md` | [p. ej. integra otra área como sección] |

## 2. Fuentes de tokens
| Área | Ficheros |
| :--- | :--- |
| [área] | [ficheros del export] |

## 3. Modos
| Área | Modo base | Modo alternativo | Cómo se declara en el export |
| :--- | :--- | :--- | :--- |
| [área] | [nombre] | [nombre] | [extensión o clave] |

## 4. Clasificación de grupos de tokens
| Capa | Grupos | Destino |
| :--- | :--- | :--- |
| Primitivos | [grupos] | Referencia, «Primitivos» |
| Semánticos de sistema | [grupos] | Referencia, «Semánticos» |
| Componente | [grupo → componente] | Spec y guía del componente |
| Dominio | [grupos] | [Guía o patrón] |

## 5. Formato de valores
- **Color:** [formato principal y secundario]
- **Números y unidades:** [regla]

## 6. Nombres preferidos
| Usar | En lugar de | Nota |
| :--- | :--- | :--- |
| [término] | [variante] | [dónde aparece la variante] |

## 7. Pendientes
- **Prefijo de ID:** [PREFIJO]

## 8. Registros de decisiones
- [Ruta y tema de cada registro]
```
