"""Servidor TCP multicliente."""

import socket
import threading

from app.common.logger import setup_logger
from app.server.config import LOG_FILE, MAX_CONNECTIONS, SERVER_HOST, SERVER_PORT
from app.server.handlers import handle_client

logger = setup_logger("server", LOG_FILE)


def start_server(host: str = SERVER_HOST, port: int = SERVER_PORT) -> None:
    """Inicia el servidor TCP y acepta múltiples clientes."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(MAX_CONNECTIONS)

    logger.info("Servidor iniciado en %s:%s", host, port)
    logger.info("Esperando conexiones de clientes...")

    try:
        while True:
            client_socket, address = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address, logger),
                daemon=True,
            )
            client_thread.start()
            logger.info("Hilo creado para cliente %s:%s", address[0], address[1])
    except KeyboardInterrupt:
        logger.info("Servidor detenido manualmente")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
