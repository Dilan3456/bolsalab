"""Pruebas de la carga del dataset de Japón. Los valores esperados están en
docs/protocolo-evaluacion.md (sección 2) y docs/datos.md. Los datos se cargan en conftest.py."""

import pytest

from bolsalab.config import JAPAN_SURVEY_FILE
from bolsalab.dataset import BEHAVIOR_COLUMNS

pytestmark = pytest.mark.skipif(
    not JAPAN_SURVEY_FILE.exists(),
    reason="Falta el archivo de la encuesta japonesa en data/external (no se versiona)",
)

BINARY_COLUMNS = ["Interest_Score", "Inflation_Score", "Diversification_Score",
                  "Gender", "Uni_Educ", "Married", "Childreen", "Urban_Dummey", "Employment"]


def test_file_size(survey):
    """El archivo tiene 191.762 filas y 26 columnas."""
    assert survey.shape == (191762, 26)


def test_no_missing_values(survey):
    """El archivo no tiene celdas vacías."""
    assert not survey.isna().any().any()


def test_behavior_counts(survey):
    """Vendieron todo 2.379, vendieron parte 8.490 y mantuvieron 43.835."""
    counts = survey[BEHAVIOR_COLUMNS].eq(1).sum()
    assert counts.to_dict() == {
        "Tot_Panic_Sell": 2379, "Part_Panic_Sell": 8490, "Cons_Investor": 43835,
    }


def test_no_person_has_two_behaviors(survey):
    """Ninguna persona aparece con más de una conducta a la vez."""
    assert (survey[BEHAVIOR_COLUMNS].sum(axis=1) <= 1).all()


def test_investors_count(investors):
    """Quedan 54.704 personas con inversiones."""
    assert len(investors) == 54704


def test_investors_who_sold(investors):
    """De ellas, 10.869 vendieron todo o parte."""
    sold = investors["Tot_Panic_Sell"].eq(1) | investors["Part_Panic_Sell"].eq(1)
    assert sold.sum() == 10869


def test_age_range(survey):
    """La edad está entre 18 y 94 años."""
    assert survey["Age"].between(18, 94).all()


def test_binary_columns(survey):
    """Las preguntas de conocimiento y las variables de sí o no solo valen 0 o 1."""
    for column in BINARY_COLUMNS:
        assert set(survey[column].unique()) <= {0, 1}, column


def test_scales_from_1_to_5(survey):
    """La confianza y la visión de corto plazo van de 1 a 5."""
    for column in ["FinKnw_Confidence", "Myopic_View"]:
        assert set(survey[column].unique()) <= {1, 2, 3, 4, 5}, column
