"""Tabla del panel SCF 2007-2009 para contrastar el modelo entrenado con Japón.

Deja una fila por familia y por imputación (la Reserva Federal publica 5 versiones
de cada familia). Solo entran las familias que tenían acciones o fondos en 2007.
Las variables de entrada usan los mismos nombres que la tabla de Japón.

Uso: python -m bolsalab.scf_panel
"""

from pathlib import Path

import pandas as pd

from bolsalab.config import SCF_PANEL_FILE

COMMON_FEATURES = ["age", "university", "married", "has_children", "employed"]

# Columnas que leemos del archivo de la Reserva Federal (07 = 2007, 09 = 2009):
#   YY1       número de la familia
#   Y1        número de la familia + versión de la imputación (último dígito, 1 a 5)
#   WGT09     peso de la familia en la encuesta
#   DEQ       dinero en acciones y fondos
#   AGE       edad de quien encabeza el hogar
#   EDCL      educación en 4 niveles (4 = título universitario)
#   MARRIED   1 = casado o vive en pareja, 2 = no
#   KIDS      número de hijos que viven en el hogar
#   OCCAT1    ocupación (1 = empleado, 2 = por cuenta propia, 3 y 4 = no trabaja)
RAW_COLUMNS = ["YY1", "Y1", "WGT09", "DEQ07", "DEQ09",
               "AGE07", "EDCL07", "MARRIED07", "KIDS07", "OCCAT107"]


def load_scf_panel(path: Path = SCF_PANEL_FILE) -> pd.DataFrame:
    """Lee el extracto del panel y devuelve la tabla lista para el contraste."""
    raw = pd.read_stata(path, columns=RAW_COLUMNS, convert_categoricals=False)

    # Solo quien tenía acciones o fondos en 2007 podía salir de ellos.
    holders = raw[raw["DEQ07"] > 0]

    return pd.DataFrame({
        "family_id": holders["YY1"].astype(int),
        "implicate": (holders["Y1"] % 10).astype(int),
        "weight": holders["WGT09"],
        # 1 si en 2009 ya no tenía acciones ni fondos; 0 si seguía teniéndolos.
        "sold": (holders["DEQ09"] == 0).astype(int),
        "age": holders["AGE07"].astype(int),
        # EDCL = 4 es título universitario (fedstables.macro.txt).
        "university": (holders["EDCL07"] == 4).astype(int),
        # MARRIED = 1 es casado o vive en pareja.
        "married": (holders["MARRIED07"] == 1).astype(int),
        # KIDS cuenta los hijos que viven en el hogar.
        "has_children": (holders["KIDS07"] >= 1).astype(int),
        # OCCAT1 = 1 empleado, 2 por cuenta propia.
        "employed": holders["OCCAT107"].isin([1, 2]).astype(int),
    }).reset_index(drop=True)


if __name__ == "__main__":
    table = load_scf_panel()
    print(table.groupby("implicate")["sold"].agg(["size", "sum", "mean"]))
