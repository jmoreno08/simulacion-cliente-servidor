# Arquitectura del Proyecto

## Objetivo

El proyecto implementa una comunicación cliente-servidor usando sockets TCP en Python.

## Componentes principales

### Servidor

Ubicado en `app/server/`.

Responsabilidades:

- Abrir un socket TCP.
- Escuchar conexiones entrantes.
- Crear un hilo por cliente conectado.
- Validar login.
- Recibir mensajes.
- Enviar confirmaciones.
- Registrar eventos con logging.

### Cliente

Ubicado en `app/client/`.

Responsabilidades:

- Conectarse al servidor.
- Solicitar usuario y contraseña.
- Enviar datos de login.
- Enviar mensajes escritos por el usuario.
- Mostrar respuestas del servidor.

### Common

Ubicado en `app/common/`.

Responsabilidades:

- Definir constantes compartidas.
- Configurar logging.
- Enviar y recibir mensajes JSON.
- Construir mensajes con estructura estándar.

## Separación de responsabilidades

El proyecto evita mezclar toda la lógica en un solo archivo. Cada módulo tiene una función clara:

- `server.py`: arranque del servidor.
- `handlers.py`: atención de clientes.
- `auth.py`: autenticación.
- `client.py`: lógica del cliente.
- `utils.py`: utilidades de red.
- `logger.py`: configuración de logs.

## Threading

El servidor usa `threading.Thread` para manejar múltiples clientes simultáneamente. Cada cliente conectado es atendido en un hilo independiente, evitando que un cliente bloquee a los demás.

## Formato de mensajes

La comunicación usa JSON con esta estructura:

```json
{
  "type": "login",
  "payload": {
    "username": "cliente1",
    "password": "1234"
  },
  "timestamp": "2026-05-25T17:00:00"
}
```

Tipos de mensajes usados:

- `login`
- `message`
- `exit`
- `ack`
- `error`
