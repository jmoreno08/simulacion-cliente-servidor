"""Configuración del cliente."""

import os

from app.common.constants import DEFAULT_HOST, DEFAULT_PORT

SERVER_HOST = os.getenv("SERVER_HOST", DEFAULT_HOST)
SERVER_PORT = int(os.getenv("SERVER_PORT", DEFAULT_PORT))
LOG_FILE = "logs/client.log"
