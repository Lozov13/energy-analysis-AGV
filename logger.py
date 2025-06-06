import logging
import sys
from datetime import datetime


def setup_custom_logger(name='AppLogger'):
    # Tworzenie obiektu loggera
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Konfiguracja formatu wyjścia
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Handler dla konsoli (zastępuje print)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Dodawanie handlerów
    logger.addHandler(console_handler)

    return logger
