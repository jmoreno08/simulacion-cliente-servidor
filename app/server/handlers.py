"""Manejadores de clientes conectados al servidor."""

import socket

from app.common.constants import (
    MESSAGE_TYPE_ACK,
    MESSAGE_TYPE_CHAT,
    MESSAGE_TYPE_ERROR,
    MESSAGE_TYPE_EXIT,
    MESSAGE_TYPE_LOGIN,
)
from app.common.utils import build_message, receive_json, send_json
from app.server.auth import validate_credentials


def handle_client(client_socket: socket.socket, address: tuple, logger) -> None:
    """Atiende a un cliente de forma independiente usando threading."""
    authenticated_user = None
    logger.info("Cliente conectado: %s:%s", address[0], address[1])

    try:
        while True:
            data = receive_json(client_socket)

            if data is None:
                logger.info("Cliente desconectado: %s:%s", address[0], address[1])
                break

            message_type = data.get("type")
            payload = data.get("payload", {})

            if message_type == MESSAGE_TYPE_LOGIN:
                username = payload.get("username", "")
                password = payload.get("password", "")

                if validate_credentials(username, password):
                    authenticated_user = username
                    logger.info("Usuario autenticado: %s", username)
                    send_json(
                        client_socket,
                        build_message(MESSAGE_TYPE_ACK, {"response": "Login exitoso"}),
                    )
                else:
                    logger.warning("Credenciales inválidas desde %s:%s", address[0], address[1])
                    send_json(
                        client_socket,
                        build_message(MESSAGE_TYPE_ERROR, {"response": "Credenciales inválidas"}),
                    )

            elif message_type == MESSAGE_TYPE_CHAT:
                if authenticated_user is None:
                    send_json(
                        client_socket,
                        build_message(MESSAGE_TYPE_ERROR, {"response": "Debe iniciar sesión primero"}),
                    )
                    continue

                text = payload.get("text", "")
                logger.info("Mensaje recibido de %s: %s", authenticated_user, text)
                send_json(
                    client_socket,
                    build_message(
                        MESSAGE_TYPE_ACK,
                        {"response": "Mensaje recibido correctamente"},
                    ),
                )
                logger.info("Confirmación enviada a %s", authenticated_user)

            elif message_type == MESSAGE_TYPE_EXIT:
                logger.info("Usuario salió: %s", authenticated_user or address)
                send_json(
                    client_socket,
                    build_message(MESSAGE_TYPE_ACK, {"response": "Conexión cerrada"}),
                )
                break

            else:
                send_json(
                    client_socket,
                    build_message(MESSAGE_TYPE_ERROR, {"response": "Tipo de mensaje no reconocido"}),
                )

    except ConnectionResetError:
        logger.warning("Conexión reiniciada por el cliente: %s:%s", address[0], address[1])
    except Exception as exc:
        logger.exception("Error atendiendo cliente %s:%s -> %s", address[0], address[1], exc)
    finally:
        client_socket.close()
