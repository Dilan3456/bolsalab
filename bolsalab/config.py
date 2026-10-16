"""Configuración central: rutas y semilla.

Todo módulo del pipeline importa sus rutas y parámetros desde aquí para que
ningún valor quede repetido o escrito a mano en notebooks o scripts.
"""

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# --- Rutas (estructura Cookiecutter Data Science) ---------------------------
PROJ_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
EXTERNAL_DATA_DIR = DATA_DIR / "external"  # datasets descargados a mano (data/external/crash)
INTERIM_DATA_DIR = DATA_DIR / "interim"    # tablas limpias por fuente
PROCESSED_DATA_DIR = DATA_DIR / "processed"  # datasets finales de entrenamiento

MODELS_DIR = PROJ_ROOT / "models"
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# --- Reproducibilidad ---------------------------------------------------------
RANDOM_STATE = 42
