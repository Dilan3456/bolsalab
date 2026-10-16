"""Carga y limpieza del dataset de Japón (etapa 1 del pipeline).

Lee la encuesta de Bawalle, Khan y Kadoya (2025) desde data/external/crash.
Cada fila es un cliente de un corredor en línea de Japón que contó qué hizo
con sus inversiones durante la caída de marzo de 2020.

Deja solo a quienes vendieron todo, vendieron parte o mantuvieron: 54.704 de
191.762 personas. Quien no tenía inversiones queda fuera porque no tenía nada
que vender. La tabla resultante va a data/interim.

Uso: uv run python -m bolsalab.dataset
"""

from pathlib import Path

import pandas as pd

from bolsalab.config import INTERIM_DATA_DIR, JAPAN_SURVEY_FILE

# Columnas de conducta en marzo de 2020 (1 = sí, 0 = no):
#   Tot_Panic_Sell   vendió todas sus acciones o fondos
#   Part_Panic_Sell  vendió una parte
#   Cons_Investor    mantuvo sus inversiones
BEHAVIOR_COLUMNS = ["Tot_Panic_Sell", "Part_Panic_Sell", "Cons_Investor"]

INVESTORS_FILE = INTERIM_DATA_DIR / "japan_investors.parquet"


def load_japan_survey(path: Path = JAPAN_SURVEY_FILE) -> pd.DataFrame:
    """Lee el archivo original de la encuesta (archivo S1 del artículo)."""
    return pd.read_excel(path)


def select_investors(survey: pd.DataFrame) -> pd.DataFrame:
    """Deja a quienes vendieron todo, vendieron parte o mantuvieron sus inversiones."""
    had_investments = survey[BEHAVIOR_COLUMNS].eq(1).any(axis=1)
    return survey[had_investments].reset_index(drop=True)


def main() -> None:
    investors = select_investors(load_japan_survey())
    investors.to_parquet(INVESTORS_FILE, index=False)
    print(f"{len(investors)} personas guardadas en {INVESTORS_FILE}")


if __name__ == "__main__":
    main()
