import logging
import os

# garante pasta de logs
os.makedirs("logs", exist_ok=True)

# configuração global do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

# instância reutilizável
logger = logging.getLogger(__name__)