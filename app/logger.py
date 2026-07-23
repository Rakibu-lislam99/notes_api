import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(app):
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")

    file_handler = RotatingFileHandler(
        'logs/app.log' ,
        maxBytes= 1024 * 1024 ,
        backupCount=5,
    )

    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.info("============Application started=============")





