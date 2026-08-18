# Product Requirements Document (PRD)

<!-- Fuente de verdad sobre qué construimos y por qué.
     Actualizar este archivo cuando cambie el alcance, las funcionalidades o el usuario objetivo.
     Si algo se mueve a "fuera de alcance", no borrar: mover a la sección correspondiente. -->

---

## Resumen ejecutivo

<!-- 2-3 párrafos que expliquen el producto a alguien que no lo conoce.
     Qué es, para quién, por qué existe ahora. -->

---

## Problema que resuelve

<!-- Describir el problema desde la perspectiva del usuario, no desde la solución técnica. -->

---

## Usuario objetivo

<!-- Describir quién es el usuario principal.
     Si hay varios perfiles de usuario, describir cada uno por separado.
     Incluir persona si se ha definido:
     - Nombre ficticio
     - Edad, contexto
     - Motivación principal
     - Frustración principal que este producto resuelve -->

---

## Funcionalidades core (MoSCoW)

<!-- Priorizar con:
     - MUST: imprescindible para el MVP
     - SHOULD: importante pero no bloqueante
     - COULD: deseable si hay tiempo
     - WON'T: explícitamente fuera de alcance en esta versión

     Cada funcionalidad lleva dos cosas obligatorias:

     1. UN IDENTIFICADOR ESTABLE — `M-01`, `S-01`, `C-01`. Es el nombre por el que la
        funcionalidad se cita en el resto del repo: en la ficha de `docs/features/`, en el
        changelog, en el PR y en el nombre del test. Nunca se reutiliza ni se renumera: si una
        funcionalidad se cae, su ID se queda vacante.

     2. UN CRITERIO DE ACEPTACIÓN COMPROBABLE — redactado como
        "Dado [contexto], cuando [acción], entonces [resultado observable]".

     El criterio no es literatura: es lo que después se convierte en aserción del test. Por eso
     el "entonces" tiene que ser algo que se pueda mirar y decir sí o no (un mensaje visible, una
     redirección, un registro creado), no un adjetivo. "Entonces la experiencia es fluida" no vale.
     Añade el caso negativo siempre que el fallo sea previsible: es donde se esconden los bugs.

     Sin criterio de aceptación, "hecho" acaba siendo una opinión, y con agentes de por medio
     acaba siendo la del agente.

     Ejemplo:

     ### MUST
     - **[M-01] Registro con email** — Dado un visitante sin cuenta, cuando envía un email válido
       y una contraseña de 8+ caracteres, entonces recibe email de confirmación y accede al
       dashboard vacío.
       *Negativo:* dado un email ya registrado, cuando lo envía, entonces ve un error inline y no
       se crea ninguna cuenta. -->

### MUST
- <!-- **[M-01] Título** — Dado ..., cuando ..., entonces ... -->

### SHOULD
- <!-- **[S-01] Título** — Dado ..., cuando ..., entonces ... -->

### COULD
- <!-- **[C-01] Título** — Dado ..., cuando ..., entonces ... -->

### WON'T (esta versión)
- <!-- ... -->

<!-- Las WON'T no llevan ID ni criterio: no se van a construir. Si alguna entra más adelante,
     se le asigna ID nuevo al moverla de sección. -->

---

## Flujos de usuario principales

<!-- Describir narrativamente los flujos más importantes.
     No hace falta diagramas aquí (van en architecture.md si se necesitan).
     Ejemplo:
     
     **Flujo de registro:**
     El usuario llega a la landing, hace clic en "Crear cuenta", introduce email y contraseña,
     recibe email de confirmación, confirma y accede al dashboard vacío. -->

---

## Requisitos no funcionales

<!-- Rendimiento, accesibilidad, SEO, internacionalización, seguridad, etc.
     Solo los que sean relevantes para este proyecto. -->

---

## Fuera de alcance (explícito)

<!-- Lista de cosas que se han discutido y decidido NO incluir.
     Tenerlas escritas evita reabrir decisiones ya tomadas. -->
