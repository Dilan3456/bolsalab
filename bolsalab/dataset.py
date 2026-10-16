"""Carga y limpieza del dataset de Japón (etapa 1 del pipeline).

Lee la encuesta de Bawalle, Khan y Kadoya (2025) desde data/external/crash.
Cada fila es un cliente de un corredor en línea de Japón que contó qué hizo
con sus inversiones durante la caída de marzo de 2020.

Deja solo a quienes vendieron todo, vendieron parte o mantuvieron: 54.704 de
191.762 personas. Quien no tenía inversiones queda fuera porque no tenía nada
que vender. La tabla resultante va a data/interim.

Uso: uv run python -m bolsalab.dataset
"""

import pandas as pd


def load_japan_survey() -> pd.DataFrame:
    """Lee el archivo original de la encuesta (archivo S1 del artículo)."""
    raise NotImplementedError


def select_investors(survey: pd.DataFrame) -> pd.DataFrame:
    """Deja a quienes vendieron todo, vendieron parte o mantuvieron sus inversiones."""
    raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
