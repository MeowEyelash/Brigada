import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(
                'logs/bot.log',
                maxBytes=5*1024*1024,
                backupCount=3
            ),
            logging.StreamHandler()
        ]
    )