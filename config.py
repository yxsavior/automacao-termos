import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise ValueError("BASE_URL não definida no .env")

DATA_PATH = "data/dados.csv"
PASTA_BASE = "TERMOS"

CONFIG = {
    "base_pasta": PASTA_BASE,
    "termos": [
        {
            "nome": "confidencialidade",
            "url": f"{BASE_URL}",
            "botao": "Gerar Termo de Confidencialidade"
        },
        {
            "nome": "imagem",
            "url": f"{BASE_URL}/image",
            "botao": "Gerar Termo de Imagem"
        },
        {
            "nome": "voluntariado",
            "url": f"{BASE_URL}/volunteering",
            "botao": "Gerar Termo de Voluntariado"
        }
    ]
}

USUARIO = os.getenv("USUARIO_LOGIN")
SENHA = os.getenv("SENHA_LOGIN")

TIMEOUT = 15000
RETRY_MAX = 3