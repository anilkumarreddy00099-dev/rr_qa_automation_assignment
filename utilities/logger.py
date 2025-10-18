import logging
import os

def get_logger():
    logger = logging.getLogger("RapyutaQA")
    if not logger.handlers:
        os.makedirs("reports", exist_ok=True)
        fh = logging.FileHandler("reports/execution.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.setLevel(logging.INFO)
    return logger
