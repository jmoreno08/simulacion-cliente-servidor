# Configuración base para el cliente
"""
Este archivo representa el cliente para conexión a la simulación cliente-servidor.
"""
import socket
import logging

# Configuración base de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def start_client():
    logging.info("Cliente iniciado. Configura la conexión al servidor.")

if __name__ == "__main__":
    start_client()