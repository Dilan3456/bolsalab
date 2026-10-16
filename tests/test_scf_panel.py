"""Pruebas de la tabla del panel SCF. Los valores esperados están en la hoja 8
del Excel de estado del arte y en docs/protocolo-evaluacion.md."""

import pytest

from bolsalab.config import SCF_PANEL_FILE
from bolsalab.scf_panel import COMMON_FEATURES, load_scf_panel

pytestmark = pytest.mark.skipif(
    not SCF_PANEL_FILE.exists(),
    reason="Falta el archivo del panel SCF en data/external (no se versiona)",
)


@pytest.fixture(scope="module")
def table():
    return load_scf_panel()


def test_five_implicates(table):
    assert sorted(table["implicate"].unique()) == [1, 2, 3, 4, 5]


def test_families_with_holdings_per_implicate(table):
    sizes = table.groupby("implicate").size()
    assert sizes.between(1563, 1564).all()


def test_exits_per_implicate(table):
    exits = table.groupby("implicate")["sold"].sum()
    assert exits.between(310, 313).all()


def test_family_appears_once_per_implicate(table):
    assert not table.duplicated(["family_id", "implicate"]).any()


def test_common_features_are_binary_except_age(table):
    for column in COMMON_FEATURES:
        if column != "age":
            assert set(table[column].unique()) <= {0, 1}, column


def test_age_range(table):
    assert table["age"].between(18, 100).all()


def test_no_missing_values(table):
    assert not table.isna().any().any()
