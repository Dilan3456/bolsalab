"""Datos compartidos por las pruebas. El Excel de Japón tarda unos 35 segundos en
leerse, así que se lee una sola vez para todos los archivos de pruebas."""

import pytest

from bolsalab.dataset import load_japan_survey, select_investors


@pytest.fixture(scope="session")
def survey():
    """La encuesta japonesa completa (191.762 personas)."""
    return load_japan_survey()


@pytest.fixture(scope="session")
def investors(survey):
    """Las personas que vendieron todo, vendieron parte o mantuvieron."""
    return select_investors(survey)
