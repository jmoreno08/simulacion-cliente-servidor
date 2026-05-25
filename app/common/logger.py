# Logger base
"""
Definimos configuraciones de logging para servidor y cliente.
"""
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='logs/server.log',
                    filemode='a')