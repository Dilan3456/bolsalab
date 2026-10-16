# Pruebas

Comprueban que los datos y el código del pipeline den lo que esperamos. Si alguien cambia un filtro por error o descarga otra versión de un archivo, una prueba falla y lo avisa.

Correr todas:

```
uv run pytest tests -v
```

Correr solo las del panel SCF:

```
uv run pytest tests/test_scf_panel.py -v
```

Si los datos no están en `data/external/crash/`, las pruebas se saltan en vez de fallar: los datos no se suben a git.

Más comandos en [`docs/uv-commands.md`](../docs/uv-commands.md).
