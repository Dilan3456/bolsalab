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

JAPAN_SURVEY_FILE = (
    EXTERNAL_DATA_DIR / "crash" / "japan_panic_selling_2020" / "pone.0315622.s001.xlsx"
)
SCF_PANEL_FILE = EXTERNAL_DATA_DIR / "crash" / "scf_panel_2007_2009" / "raw" / "rscfp2009panel.dta"

MODELS_DIR = PROJ_ROOT / "models"
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# --- Reproducibilidad: misma semilla para que el azar siempre salga igual ---
RANDOM_STATE = 42
