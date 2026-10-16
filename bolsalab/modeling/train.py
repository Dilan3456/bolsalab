"""Entrenamiento, comparación y exportación del modelo (etapa 3 del pipeline).

Sigue las reglas de docs/protocolo-evaluacion.md:

1. Aparta el 20 % de los datos para la prueba final, con la semilla 42.
2. Compara con validación cruzada anidada siete modelos: el trivial, la
   regresión logística, Random Forest, XGBoost, LightGBM, CatBoost y una red
   neuronal pequeña. Todos usan los mismos datos y las mismas particiones.
3. Elige el ganador con la regla fijada antes de entrenar: si un modelo más
   simple queda a menos de una desviación estándar del mejor, gana el simple.
4. Mide al ganador en la prueba final y lo exporta a models/ como .joblib,
   con su metadata (métricas, parámetros y versiones) en un .json.

Uso: uv run python -m bolsalab.modeling.train
"""

import pandas as pd


def split_data(table: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Separa el 80 % para entrenar y el 20 % para la prueba final."""
    raise NotImplementedError


def compare_models(train: pd.DataFrame) -> pd.DataFrame:
    """Devuelve una fila por modelo con su AUROC, AUPRC y calibración."""
    raise NotImplementedError


def export_model(model, metrics: dict) -> None:
    """Guarda el modelo ganador y su metadata en models/."""
    raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
