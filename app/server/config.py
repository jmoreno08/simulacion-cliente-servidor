"""Configuración del servidor."""

import os

from app.common.constants import DEFAULT_HOST, DEFAULT_PORT

SERVER_HOST = os.getenv("SERVER_HOST", DEFAULT_HOST)
SERVER_PORT = int(os.getenv("SERVER_PORT", DEFAULT_PORT))
MAX_CONNECTIONS = 5
LOG_FILE = "logs/server.log"
