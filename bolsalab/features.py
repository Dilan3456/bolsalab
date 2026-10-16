"""Variable objetivo y variables de entrada (etapa 2 del pipeline).

Toma la tabla de data/interim y construye:

- `sold`, la variable objetivo: 1 si la persona vendió todo o parte durante
  la caída, 0 si mantuvo. Vendió el 19,87 %.
- Las variables de entrada, una por cada pregunta que la app le hace al
  usuario: conocimiento financiero (tres preguntas), confianza en lo que sabe,
  edad, sexo, educación, estado civil, hijos, zona urbana, empleo, ingreso,
  activos, aversión al riesgo y visión de corto plazo.

Nunca usa como entrada las columnas con las que se construye `sold`. La tabla
final va a data/processed.

Uso: uv run python -m bolsalab.features
"""

import pandas as pd


def build_target(investors: pd.DataFrame) -> pd.Series:
    """Devuelve `sold`: 1 si vendió todo o parte, 0 si mantuvo."""
    raise NotImplementedError


def build_features(investors: pd.DataFrame) -> pd.DataFrame:
    """Devuelve las variables de entrada con los nombres que usa la app."""
    raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
