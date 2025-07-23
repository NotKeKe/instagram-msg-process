import logging
import logging.handlers
from pathlib import Path
from datetime import datetime

def setup_logging():
    log_format = logging.Formatter(
        fmt="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    file_handler = logging.handlers.RotatingFileHandler(
        filename=log_dir / f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(log_format)

    if not root_logger.handlers:
        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)
        
    logging.info("已載入 logger")