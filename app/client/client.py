"""Cliente TCP interactivo por consola."""

import getpass
import socket

from app.client.config import LOG_FILE, SERVER_HOST, SERVER_PORT
from app.common.constants import MESSAGE_TYPE_CHAT, MESSAGE_TYPE_EXIT, MESSAGE_TYPE_LOGIN
from app.common.logger import setup_logger
from app.common.utils import build_message, receive_json, send_json

logger = setup_logger("client", LOG_FILE)


def login(sock: socket.socket) -> bool:
    """Solicita credenciales y realiza login contra el servidor."""
    username = input("Usuario: ").strip()
    password = getpass.getpass("Contraseña: ").strip()

    send_json(
        sock,
        build_message(
            MESSAGE_TYPE_LOGIN,
            {"username": username, "password": password},
        ),
    )

    response = receive_json(sock)
    if response:
        server_text = response.get("payload", {}).get("response", "")
        print(f"Servidor: {server_text}")
        logger.info("Respuesta de login: %s", server_text)
        return server_text == "Login exitoso"

    return False


def start_client(host: str = SERVER_HOST, port: int = SERVER_PORT) -> None:
    """Conecta el cliente al servidor y permite enviar mensajes."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            logger.info("Cliente conectado a %s:%s", host, port)
            print(f"Conectado al servidor {host}:{port}")

            if not login(client_socket):
                print("No fue posible iniciar sesión. Cerrando cliente.")
                return

            print("Escribe mensajes para enviarlos al servidor.")
            print("Escribe 'salir' para finalizar.")

            while True:
                text = input("Mensaje: ").strip()

                if text.lower() == "salir":
                    send_json(client_socket, build_message(MESSAGE_TYPE_EXIT))
                    response = receive_json(client_socket)
                    if response:
                        print("Servidor:", response.get("payload", {}).get("response", ""))
                    break

                send_json(client_socket, build_message(MESSAGE_TYPE_CHAT, {"text": text}))
                logger.info("Mensaje enviado: %s", text)

                response = receive_json(client_socket)
                if response:
                    print("Servidor:", response.get("payload", {}).get("response", ""))

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Verifica que esté en ejecución.")
        logger.error("Conexión rechazada por el servidor")
    except Exception as exc:
        print(f"Error en el cliente: {exc}")
        logger.exception("Error en cliente: %s", exc)


if __name__ == "__main__":
    start_client()
