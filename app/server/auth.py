"""Módulo de autenticación simulada."""

# Usuarios simulados para fines educativos.
# En un sistema real, las contraseñas no deben guardarse en texto plano.
USERS = {
    "cliente1": "1234",
    "cliente2": "abcd",
    "admin": "admin123",
}


def validate_credentials(username: str, password: str) -> bool:
    """Valida usuario y contraseña contra el diccionario simulado."""
    return USERS.get(username) == password
