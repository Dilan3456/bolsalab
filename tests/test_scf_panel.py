"""Pruebas de la tabla del panel SCF. Los valores esperados están en docs/datos.md."""

import pytest

from bolsalab.config import SCF_PANEL_FILE
from bolsalab.scf_panel import COMMON_FEATURES, load_scf_panel

pytestmark = pytest.mark.skipif(
    not SCF_PANEL_FILE.exists(),
    reason="Falta el archivo del panel SCF en data/external (no se versiona)",
)


@pytest.fixture(scope="module")
def table():
    """Carga la tabla una sola vez para todas las pruebas."""
    return load_scf_panel()


def test_five_implicates(table):
    """Están las 5 versiones (imputaciones) de cada familia."""
    assert sorted(table["implicate"].unique()) == [1, 2, 3, 4, 5]


def test_families_with_holdings_per_implicate(table):
    """Cada versión tiene 1.563 o 1.564 familias con acciones o fondos en 2007."""
    sizes = table.groupby("implicate").size()
    assert sizes.between(1563, 1564).all()


def test_exits_per_implicate(table):
    """En cada versión salieron entre 310 y 313 familias."""
    exits = table.groupby("implicate")["sold"].sum()
    assert exits.between(310, 313).all()


def test_family_appears_once_per_implicate(table):
    """Ninguna familia aparece dos veces en la misma versión."""
    assert not table.duplicated(["family_id", "implicate"]).any()


def test_common_features_are_binary_except_age(table):
    """Las variables de sí o no solo valen 0 o 1."""
    for column in COMMON_FEATURES:
        if column != "age":
            assert set(table[column].unique()) <= {0, 1}, column


def test_age_range(table):
    """La edad está entre 18 y 100 años."""
    assert table["age"].between(18, 100).all()


def test_no_missing_values(table):
    """La tabla no tiene celdas vacías."""
    assert not table.isna().any().any()
