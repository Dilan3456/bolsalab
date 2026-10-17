"""Pruebas de la tabla de entrenamiento. La lista de variables está en
docs/variables.md. Los datos se cargan en conftest.py."""

import pandas as pd
import pytest

from bolsalab.config import JAPAN_SURVEY_FILE
from bolsalab.dataset import BEHAVIOR_COLUMNS
from bolsalab.features import (
    ASSET_BRACKETS,
    FEATURES,
    INCOME_BRACKETS,
    build_features,
    build_target,
    to_bracket,
)

needs_japan_data = pytest.mark.skipif(
    not JAPAN_SURVEY_FILE.exists(),
    reason="Falta el archivo de la encuesta japonesa en data/external (no se versiona)",
)

COMMON_WITH_SCF = ["age", "university", "married", "has_children", "employed"]


@pytest.fixture(scope="module")
def features(investors):
    """Las 17 variables de entrada."""
    return build_features(investors)


@needs_japan_data
def test_has_the_17_features(features):
    """La tabla tiene exactamente las 17 variables de docs/variables.md, en orden."""
    assert list(features.columns) == FEATURES
    assert len(FEATURES) == 17


@needs_japan_data
def test_target_counts(investors):
    """`sold` tiene 10.869 unos (vendieron) y 43.835 ceros (mantuvieron)."""
    sold = build_target(investors)
    assert sold.value_counts().to_dict() == {1: 10869, 0: 43835}


@needs_japan_data
def test_no_behavior_column_leaks(features):
    """Ninguna columna con la que se construye `sold` entra como variable."""
    assert not set(BEHAVIOR_COLUMNS) & set(features.columns)


@needs_japan_data
def test_common_columns_with_scf(features):
    """Están las 5 variables que también tiene el panel SCF de EE. UU."""
    assert set(COMMON_WITH_SCF) <= set(features.columns)


@needs_japan_data
def test_brackets_have_no_gaps(features):
    """El ingreso va del tramo 1 al 12 y los activos del 1 al 10, sin vacíos."""
    assert sorted(features["income_bracket"].unique()) == list(range(1, 13))
    assert sorted(features["assets_bracket"].unique()) == list(range(1, 11))


@needs_japan_data
def test_no_missing_values(features):
    """La tabla no tiene celdas vacías."""
    assert not features.isna().any().any()


def test_bracket_of_a_single_person():
    """Una sola persona recibe su tramo correcto, igual que en el entrenamiento."""
    assert to_bracket(pd.Series([5_000_000]), INCOME_BRACKETS).tolist() == [4]
    assert to_bracket(pd.Series([100_000_000]), ASSET_BRACKETS).tolist() == [10]
