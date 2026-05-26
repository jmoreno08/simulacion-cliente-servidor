"""Constantes compartidas entre cliente y servidor."""

ENCODING = "utf-8"
BUFFER_SIZE = 4096
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5000

MESSAGE_TYPE_LOGIN = "login"
MESSAGE_TYPE_CHAT = "message"
MESSAGE_TYPE_EXIT = "exit"
MESSAGE_TYPE_ACK = "ack"
MESSAGE_TYPE_ERROR = "error"
