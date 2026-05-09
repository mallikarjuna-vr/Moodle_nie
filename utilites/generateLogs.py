import logging
import os

def log():
    log_dir = "../logs"
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(log_dir, "logfile1.log"),
        format="%(asctime)s: %(levelname)s: %(message)s",
        datefmt="%m/%d/%y %I:%M:%S %p",
        level=logging.INFO
    )

    return logging.getLogger()

logger = log()
logger.info("This is from utility function")