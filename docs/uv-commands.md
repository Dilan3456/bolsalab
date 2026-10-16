# Comandos

Todos se ejecutan desde la raíz del repositorio (`bolsalab/`), en PowerShell o en cualquier terminal.

## Preparar el entorno

Solo la primera vez, o cuando cambie `uv.lock`:

```
uv sync
```

Crear el archivo de variables de entorno (una sola vez):

```
cp .env.example .env
```

## Datos

Los datos no se versionan. Cada integrante los descarga de su fuente y los guarda en `data/external/crash/`:

- **Japón:** archivo S1 del artículo de Bawalle, Khan y Kadoya (2025) en PLOS ONE, https://doi.org/10.1371/journal.pone.0315622
- **Panel SCF 2007-2009:** Reserva Federal de EE. UU., https://www.federalreserve.gov/econres/scf_2009p.htm

## Pruebas y calidad del código

Tests:

```
uv run pytest tests -v
```

Revisión de estilo y errores (linter):

```
uv run ruff check bolsalab tests
```

Corregir automáticamente lo que se pueda:

```
uv run ruff check bolsalab tests --fix
```

## Dependencias

Agregar una librería (actualiza `pyproject.toml` y `uv.lock`):

```
uv add <paquete>
```

Agregar una herramienta solo de desarrollo:

```
uv add --dev <paquete>
```

Abrir Jupyter con el entorno del proyecto:

```
uv run jupyter lab
```
