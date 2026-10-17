"""Variable objetivo y variables de entrada (etapa 2 del pipeline).

Toma la tabla de data/interim (las 54.704 personas con inversiones) y construye:

- `sold`, la variable objetivo: 1 si la persona vendió todo o parte durante
  la caída, 0 si mantuvo. Vendió el 19,87 %.
- Las 17 variables de entrada, con los nombres que usa la app. La lista, y las
  columnas que no entran, están en docs/variables.md.

Nunca usa como entrada las columnas con las que se construye `sold`. La tabla
final va a data/processed.

Uso: uv run python -m bolsalab.features
"""

import pandas as pd

from bolsalab.config import PROCESSED_DATA_DIR
from bolsalab.dataset import INVESTORS_FILE

TRAINING_FILE = PROCESSED_DATA_DIR / "japan_training.parquet"

# Columna del archivo -> nombre en la app.
RENAMES = {
    "Interest_Score": "knows_interest",
    "Inflation_Score": "knows_inflation",
    "Diversification_Score": "knows_diversification",
    "FinKnw_Confidence": "knowledge_confidence",
    "FinLit_Overconfidence": "overconfidence",
    "Age": "age",
    "AgeS": "age_squared",
    "Gender": "male",
    "Uni_Educ": "university",
    "Married": "married",
    "Childreen": "has_children",
    "Urban_Dummey": "urban",
    "Employment": "employed",
    "Risk_Aversion": "risk_aversion",
    "Myopic_View": "short_term_view",
}

# El archivo guarda cada tramo con una cifra en yenes. La posición en la lista
# es el número de tramo (1 = el más bajo).
INCOME_BRACKETS = [1_000_000, 1_500_000, 3_000_000, 5_000_000, 7_000_000, 9_000_000,
                   11_000_000, 13_000_000, 15_000_000, 17_000_000, 19_000_000, 20_000_000]
ASSET_BRACKETS = [2_500_000, 3_750_000, 6_250_000, 8_750_000, 12_500_000,
                  17_500_000, 25_000_000, 40_000_000, 75_000_000, 100_000_000]

FEATURES = list(RENAMES.values()) + ["income_bracket", "assets_bracket"]


def build_target(investors: pd.DataFrame) -> pd.Series:
    """Devuelve `sold`: 1 si vendió todo o parte, 0 si mantuvo."""
    sold = investors["Tot_Panic_Sell"].eq(1) | investors["Part_Panic_Sell"].eq(1)
    return sold.astype(int).rename("sold")


def to_bracket(values: pd.Series, brackets: list[int]) -> pd.Series:
    """Cambia la cifra en yenes por su número de tramo."""
    return values.map({yen: position for position, yen in enumerate(brackets, start=1)})


def build_features(investors: pd.DataFrame) -> pd.DataFrame:
    """Devuelve las 17 variables de entrada con los nombres que usa la app."""
    features = investors[list(RENAMES)].rename(columns=RENAMES)
    features["income_bracket"] = to_bracket(investors["H_Income"], INCOME_BRACKETS)
    features["assets_bracket"] = to_bracket(investors["H_Asset"], ASSET_BRACKETS)
    return features[FEATURES]


def main() -> None:
    investors = pd.read_parquet(INVESTORS_FILE)
    table = build_features(investors).assign(sold=build_target(investors))
    table.to_parquet(TRAINING_FILE, index=False)
    print(f"{len(table)} personas y {len(FEATURES)} variables guardadas en {TRAINING_FILE}")


if __name__ == "__main__":
    main()
