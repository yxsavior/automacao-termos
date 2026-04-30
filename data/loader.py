import pandas as pd
from core.logger import logger

def carregar_csv(caminho):
    try:
        df = pd.read_csv(caminho, sep=None, engine="python")
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        logger.error(f"Erro ao carregar CSV: {e}")
        return None