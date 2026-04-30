import unicodedata
import re
import pandas as pd

def limpar_texto(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).strip()
    return re.sub(r'[^\x00-\x7FÀ-ÿ]+', '', texto)


def apenas_numeros(texto):
    return re.sub(r'\D', '', texto)


def sanitize_filename(nome):
    nome = unicodedata.normalize('NFKD', nome)
    nome = nome.encode('ascii', 'ignore').decode('ascii')
    nome = re.sub(r'\s+', '_', nome)
    return re.sub(r'[^a-zA-Z0-9_\-]', '', nome)