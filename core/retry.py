import time
from config import RETRY_MAX
from core.logger import logger

def retry(func):
    def wrapper(*args, **kwargs):
        for tentativa in range(1, RETRY_MAX + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.warning(f"Tentativa {tentativa} falhou: {e}")
                time.sleep(1)
        logger.error(f"Falha definitiva em {func.__name__}")
    return wrapper