"""Pruebas básicas de utilidades del proyecto."""

from app.common.constants import MESSAGE_TYPE_LOGIN
from app.common.utils import build_message
from app.server.auth import validate_credentials


def test_build_message():
    message = build_message(MESSAGE_TYPE_LOGIN, {"username": "cliente1"})
    assert message["type"] == MESSAGE_TYPE_LOGIN
    assert message["payload"]["username"] == "cliente1"
    assert "timestamp" in message


def test_valid_credentials():
    assert validate_credentials("cliente1", "1234") is True


def test_invalid_credentials():
    assert validate_credentials("cliente1", "wrong") is False
