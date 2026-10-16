"""Carga del modelo publicado y predicción. Es lo que llama el backend (FastAPI).

Recibe las respuestas del cuestionario y devuelve:

- la categoría: más, igual o menos propenso a vender que el promedio;
- las respuestas que más pesaron en el resultado;
- avisos cuando la persona queda fuera de lo que vio el modelo, por ejemplo
  un patrimonio por debajo del tramo más bajo de los datos de entrenamiento.

Nunca rehace el preprocesamiento: usa el que quedó guardado en el .joblib.

Ejemplo:
    model = CrashReactionModel("models/crash_reaction_v1.joblib")
    model.predict({"age": 27, "university": False, ...})
"""

from pathlib import Path


class CrashReactionModel:
    def __init__(self, artifact_path: str | Path):
        raise NotImplementedError

    def predict(self, answers: dict) -> dict:
        """Devuelve la categoría, los factores que más pesaron y los avisos."""
        raise NotImplementedError
