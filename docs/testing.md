# Estrategia de testing

<!-- Documento vivo. Actualizar cuando cambie el stack o las convenciones de testing.
     Los cambios deben registrarse también en changelog/. -->

---

## Filosofía

<!-- Describe el enfoque de testing del proyecto.
     Ejemplo: "Priorizamos tests de integración sobre unitarios porque nuestro valor
     está en los flujos completos, no en funciones aisladas."
     o: "Seguimos la pirámide clásica: muchos unitarios, integración selectiva, pocos e2e." -->

---

## Cuándo se escriben los tests

**Después de implementar, en una pasada propia.** No durante la planificación, y no a la vez que
el código.

El compromiso de que un requisito se va a validar se adquiere antes: es la tercera columna de la
tabla de cobertura de `docs/features/`. Pero el test en sí se escribe cuando el código ya existe,
leyéndolo. Es una diferencia de calendario pequeña con una consecuencia grande: un test escrito
antes que el código apunta a selectores, rutas y respuestas *imaginados*. Cuando luego no
coinciden con la realidad, casi nadie reescribe el test — se le van quitando aserciones hasta que
pasa, y acaba siendo un test que no comprueba nada pero que da luz verde. Escrito después, apunta
a lo que hay.

Reglas que se derivan de eso:

- **Antes de escribir una aserción, verifica que el selector existe en el código.** No lo
  supongas por el nombre del componente.
- **Si un elemento no tiene selector estable, añádele uno.** Meter un `data-testid` en el código
  es un cambio mínimo aceptable y preferible a colgar el test de una clase de estilos o de un
  texto que cambiará con el próximo ajuste de copy.
- **Cada "entonces" del criterio de aceptación necesita al menos una aserción.** Si el criterio
  define caso negativo, va su propio test.
- **Un test que falla no se arregla quitándole aserciones.** Si falla, o el código está mal o el
  criterio estaba mal escrito. Ambas cosas se corrigen donde toca; degradar el test para forzar el
  verde convierte la suite en decoración.
- **Los datos que crea un test los borra ese test.** Prefija lo que insertes para poder
  identificarlo y limpia al terminar, aunque el test falle a mitad.

---

## Stack de testing

<!-- Herramientas utilizadas por tipo de test.
     Ejemplo:
     | Tipo | Herramienta |
     |------|-------------|
     | Unitario | Vitest |
     | Integración | Vitest + Testing Library |
     | E2E | Playwright | -->

| Tipo | Herramienta |
|------|-------------|
| Unitario | <!-- --> |
| Integración | <!-- --> |
| E2E | <!-- --> |

---

## Qué testear

<!-- Distingue explícitamente qué merece test y qué no, para no perder tiempo.
     Ejemplo:
     SÍ → lógica de negocio, transformaciones de datos, componentes con estado complejo
     NO → componentes puramente visuales, integraciones con terceros (mockear en su lugar) -->

### Sí testear
- <!-- -->

### No testear (o mockear)
- <!-- -->

---

## Convenciones

<!-- Naming, ubicación de archivos, estructura interna de los tests.
     Ejemplo:
     - Archivos: `nombre.test.ts` junto al archivo que testa
     - Describe en presente: "calcula el total con descuento"
     - Un assert por test cuando sea posible -->

---

## Cobertura objetivo

<!-- Porcentaje objetivo y cómo medirlo.
     Ejemplo: ≥ 80% en lógica de negocio. Ignorar archivos de configuración y tipos. -->

---

## Cómo correr los tests

```bash
# Todos los tests
pnpm test

# Modo watch
pnpm test:watch

# Con cobertura
pnpm test:coverage

# E2E
pnpm test:e2e
```

<!-- Ajusta los comandos al stack elegido una vez relleno architecture.md. -->
