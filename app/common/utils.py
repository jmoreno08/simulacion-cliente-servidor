"""Funciones utilitarias para enviar y recibir mensajes JSON por TCP."""

import json
import socket
from datetime import datetime

from app.common.constants import BUFFER_SIZE, ENCODING


def now_iso() -> str:
    """Retorna la fecha y hora actual en formato ISO."""
    return datetime.now().isoformat(timespec="seconds")


def build_message(message_type: str, payload: dict | None = None) -> dict:
    """Construye un mensaje estándar para la comunicación cliente-servidor."""
    return {
        "type": message_type,
        "payload": payload or {},
        "timestamp": now_iso(),
    }


def send_json(sock: socket.socket, data: dict) -> None:
    """Envía un diccionario como JSON usando salto de línea como delimitador."""
    serialized = json.dumps(data) + "\n"
    sock.sendall(serialized.encode(ENCODING))


def receive_json(sock: socket.socket) -> dict | None:
    """Recibe datos desde el socket y los convierte en diccionario Python."""
    raw_data = sock.recv(BUFFER_SIZE)
    if not raw_data:
        return None

    decoded = raw_data.decode(ENCODING).strip()
    if not decoded:
        return None

    return json.loads(decoded)
