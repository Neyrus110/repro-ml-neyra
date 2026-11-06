"""Configuración del proyecto. Es el ÚNICO archivo que deben adaptar a su dataset."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Zonas del data lake
RAW = ROOT / "data" / "raw" / "sentrybox_enaho2025.csv"  # subconjunto recibido del grupo; no se edita
PROCESSED = ROOT / "data" / "processed" / "dataset.csv"  # zona processed (silver): la genera prepare_data.py
RESULTS = ROOT / "results" / "results_summary.csv"       # zona results (gold): la genera run_seeds.py

TARGET = "ganancia_neta_mes"  # ganancia neta mensual de la ocupación principal (S/)
TAREA = "regresion"           # "regresion" o "clasificacion"
COLS_NUM = ["edad", "horas_semana", "anios_en_ocupacion", "personas_en_negocio"]
COLS_CAT = [
    "sexo_mujer", "estado_civil", "nivel_educativo", "es_empleador",
    "ayuda_familiar_no_remunerado", "registro_sunat", "lleva_libros_contables",
    "tiene_ocupacion_secundaria", "subsector_ciiu", "dominio", "estrato", "mes_encuesta",
]
# El CSV recibido ya contiene los faltantes del subconjunto como celdas vacías.
# No se reemplaza un código global: un mismo número puede ser válido en otra columna.
CODIGOS_FALTANTES = []

MODELO = "knn"                # algoritmo asignado

SEMILLA_PARTICION = 42        # fija: todos los integrantes usan la misma partición 80/20
SEMILLAS = [0, 1, 2, 3, 42]   # semillas de la validación cruzada
