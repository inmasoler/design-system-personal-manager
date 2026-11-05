# Ejemplos Prácticos — Skill Notas de Sistema de Diseño

Este documento ilustra el comportamiento exacto de los comandos ante notas sin estructura y el criterio estricto para no inventar datos.

---

## 1. Entrada de Ejemplo: Nota Raw Desordenada

Imaginemos un archivo en `docs/sistema-diseno/raw/apuntes-sesion.md` con el siguiente contenido real, sin títulos ni formato claro:

```markdown
reunion de equipo sobre boton y tokens
cambiamos el padding horizontal del Button sm de 8px a 12px para cumplir con zona tactil
metimos variante ghost al Button, usa color de texto neutral-900 y en hover neutral-100
el focus ring en safari se ve cortado en los botones con icono a la derecha, revisar eso urgente
tambien migramos el token color.brand.primary de #0052CC a #0B5FFF
documentamos en la wiki el uso de Button ghost para barras de herramientas
ojo que alguien hardcodeo 16px en el margin del Dropdown en vez de usar spacing.md
habria que ver si metemos soporte para aria-pressed en Button toggle
el viernes hay demo con stakeholders
```

---

## 2. Resultado del Comando `reorganizar`

**Archivo creado:** `docs/sistema-diseno/ordenado/apuntes-sesion-ordenado.md`  
*(El archivo `raw/apuntes-sesion.md` permanece intacto).*

```markdown
# Apuntes de Sesión — Sistema de Diseño (Reorganizado)

- **Fichero origen:** `docs/sistema-diseno/raw/apuntes-sesion.md`
- **Fecha de reorganización:** 2026-10-23
- **Procesado por:** @autor

---

## Componente: Button
- Se modificó el padding horizontal de la variante `sm` de `8px` a `12px` para cumplir con zona táctil.
- Se agregó la nueva variante `ghost`:
  - Color de texto: token `neutral-900`.
  - Estado hover: fondo con token `neutral-100`.
- Documentación: registrado en la wiki el caso de uso de `Button ghost` para barras de herramientas.

## Tokens y Fundamentos
- Se actualizó el valor del token `color.brand.primary`: de `#0052CC` a `#0B5FFF`.

## Deuda Técnica y Observaciones
- **Error visual en Safari:** El focus ring se ve cortado en botones que llevan icono a la derecha.
- **Código hardcodeado:** Se detectaron `16px` directos en el margen de `Dropdown` en lugar de consumir `spacing.md`.
- **Accesibilidad / Duda:** Valorar soporte para `aria-pressed` en `Button` cuando actúe como toggle.

## Resto / Notas de Equipo
- El viernes hay demo con stakeholders.
```

---

## 3. Resultado del Comando `update-changelog`

### A) Entrada agregada a `docs/sistema-diseno/changelog.md`:

```markdown
## [2026-10-23] - @autor

### Añadido
- **Button:** Variante `ghost` con color de texto `neutral-900` y hover en `neutral-100`.

### Cambiado
- **Button:** Padding horizontal en tamaño `sm` aumentado de `8px` a `12px` por requisitos de zona táctil.
- **Tokens:** Actualización de `color.brand.primary` de `#0052CC` a `#0B5FFF`.

### Documentación
- **Button:** Guía de uso de la variante `ghost` en barras de herramientas.

### Sin clasificar
- Recordatorio de demo con stakeholders para el viernes.
```

### B) Archivo creado en `docs/sistema-diseno/reportes/2026-10-23.md`:

```markdown
# Reporte Diario — Sistema de Diseño

- **Fecha:** 2026-10-23
- **Autor:** @autor
- **Fuentes procesadas:** `docs/sistema-diseno/raw/apuntes-sesion.md`

## Resumen Ejecutivo
Se incorporó la variante ghost al componente Button y se ajustó el espaciado táctil en su tamaño sm. Asimismo, se actualizó el color primario de marca y se identificó deuda técnica en el focus ring de Safari y en márgenes de Dropdown.

## Componentes
### Button
- **Cambio / Novedad:** Añadida variante `ghost` y ajuste de padding horizontal de `8px` a `12px` en tamaño `sm`.
- **Detalles técnicos:** Texto `neutral-900`, hover `neutral-100`.
- **Impacto:** Cumplimiento de zona táctil y soporte para barras de herramientas.

## Tokens y Fundamentos
- **Tokens afectados:** `color.brand.primary`.
- **Modificación:** Actualizado valor de `#0052CC` a `#0B5FFF`.

## Documentación
- Guía de uso de Button ghost en barras de herramientas.

## Deuda Técnica
> ⚠️ Se ha identificado o registrado deuda técnica durante la jornada. El detalle completo se gestiona en `docs/sistema-diseno/deuda.md`.
- **Aviso:** Focus ring cortado en Safari en botones con icono.
- **Aviso:** Margen hardcodeado de 16px en Dropdown.

## Resto / Sin Clasificar
- El viernes hay demo con stakeholders.
```

---

## 4. Resultado del Comando `update-deuda`

**Añadido a `docs/sistema-diseno/deuda.md`:**

```markdown
## Deuda Confirmada

### [DEUDA-20261023-01] Focus ring cortado en Safari en botones con icono derecho
- **Fecha de registro:** 2026-10-23
- **Detectado por:** @autor
- **Origen:** `docs/sistema-diseno/raw/apuntes-sesion.md`
- **Área afectada:** Componentes (Button) / Accesibilidad
- **Descripción del problema:** Al renderizar un Button con icono en la posición derecha en el navegador Safari, el contorno de focus se visualiza recortado.
- **Impacto / Riesgo:** No consta en las notas raw.
- **Solución propuesta:** No consta en las notas raw.
- **Estado:** Pendiente

### [DEUDA-20261023-02] Margen hardcodeado en componente Dropdown
- **Fecha de registro:** 2026-10-23
- **Detectado por:** @autor
- **Origen:** `docs/sistema-diseno/raw/apuntes-sesion.md`
- **Área afectada:** Componentes (Dropdown) / Tokens
- **Descripción del problema:** Se introdujo un margen de `16px` de forma manual en lugar de consumir el token correspondiente `spacing.md`.
- **Impacto / Riesgo:** Rompe la consistencia de espaciado del sistema de diseño.
- **Solución propuesta:** Sustituir valor estático por el token de spacing.
- **Estado:** Pendiente

---

## Posible Deuda / Para Confirmar

### [POSIBLE-20261023-01] Soporte para aria-pressed en Button toggle
- **Fecha de registro:** 2026-10-23
- **Detectado por:** @autor
- **Origen:** `docs/sistema-diseno/raw/apuntes-sesion.md`
- **Mención textual en notas:** "habria que ver si metemos soporte para aria-pressed en Button toggle"
- **Duda a resolver:** Determinar si el botón debe gestionar internamente el atributo de accesibilidad o si es responsabilidad del contenedor.
- **Estado:** En evaluación
```

---

## 5. Resultado del Comando `actualizar-spec` (Button)

**Archivo actualizado/creado en `docs/sistema-diseno/componentes/button.md`:**  
*(Nótese la estricta presencia de `No consta en las notas raw` en los campos no documentados).*

```markdown
# Componente: Button

- **Slug:** `button`
- **Estado de la spec:** En revisión
- **Última actualización:** 2026-10-23 por @autor

---

## 1. Descripción y Propósito
Elemento interactivo para desencadenar acciones. Se añade variante ghost orientada a barras de herramientas.

## 2. Cuándo usar y Cuándo no usar
- **Usar cuando:** Barras de herramientas (variante ghost). Otros casos: No consta en las notas raw.
- **No usar cuando:** No consta en las notas raw.

## 3. Anatomía
Texto y posible icono a la derecha (según notas). Resto de la anatomía: No consta en las notas raw.

## 4. Variantes
| Variante | Descripción | Valores válidos |
| :--- | :--- | :--- |
| ghost | Para barras de herramientas | No consta en las notas raw |
| sm | Tamaño pequeño con padding táctil de 12px | No consta en las notas raw |

## 5. Estados
- **Default / Reposo:** Texto en `neutral-900` para variante ghost.
- **Hover:** Fondo `neutral-100` para variante ghost.
- **Focus:** Reportado bug de foco cortado en Safari con icono derecho.
- **Active / Pressed:** No consta en las notas raw.
- **Disabled:** No consta en las notas raw.
- **Loading:** No consta en las notas raw.
- **Error:** No consta en las notas raw.

## 6. Propiedades / API
| Propiedad | Tipo | Obligatoria | Valor por defecto | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| variant | string | No consta | No consta | Incluye variante 'ghost' |
| size | string | No consta | No consta | Incluye tamaño 'sm' |
| aria-pressed | boolean | No consta | No consta | En evaluación para botones toggle |

## 7. Tokens Asociados
- **Color:** `neutral-900` (texto ghost), `neutral-100` (hover ghost).
- **Espaciado / Padding:** `12px` horizontal para tamaño `sm`.
- **Tipografía:** No consta en las notas raw.
- **Borde / Radio:** No consta en las notas raw.
- **Sombra / Elevación:** No consta en las notas raw.

## 8. Accesibilidad (a11y)
- **Rol ARIA:** Posible evaluación de `aria-pressed`.
- **Navegación por teclado:** Bug en focus ring de Safari.
- **Contraste mínimo:** No consta en las notas raw.

## 9. Comportamiento e Interacciones
No consta en las notas raw.

## 10. Decisiones de Diseño y Contexto
- Aumento de padding de 8px a 12px en `sm` para garantizar el área táctil mínima de interacción.

## 11. Información Pendiente / Resto
- Confirmar comportamiento del focus ring en navegadores distintos a Safari.
```

---

## 6. Resultado del Comando `generar-mensaje`

**Salida entregada en el chat (sin escribir archivo en disco):**

```text
🚀 **Actualización Sistema de Diseño — 23/10/2026**

¡Hola a todos! Os dejamos el resumen de los cambios incorporados en la jornada de hoy:

**Lo más destacado:**
• Mejorada la accesibilidad táctil del `Button` tamaño `sm` (aumento de padding a 12px).
• Incorporada la nueva variante `Button ghost` para su uso en barras de herramientas.
• Actualizado el token de color primario de marca (`color.brand.primary` a `#0B5FFF`).

📦 **Novedades en Componentes:**
• **Button:** Nueva variante ghost y ajustes de padding en `sm`.

🎨 **Tokens:**
• `color.brand.primary`: Nuevo valor hexadecimal `#0B5FFF`.

⚠️ **Avisos de Deuda y Seguimiento:**
• Se ha detectado un bug visual en el focus ring de Safari para botones con icono y un espaciado hardcodeado en `Dropdown`. Ambos están registrados en el backlog de deuda técnica (`docs/sistema-diseno/deuda.md`).

📄 *Podéis consultar el changelog completo en `docs/sistema-diseno/changelog.md` y el reporte diario en `docs/sistema-diseno/reportes/2026-10-23.md`.*
```
