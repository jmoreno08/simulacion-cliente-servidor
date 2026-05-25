import socket

def iniciar_cliente(host='localhost', puerto=5000):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, puerto))

    try:
        while True:
            data = cliente.recv(1024).decode('utf-8')
            if not data:
                break
            print(data, end="")
            entrada = input()
            cliente.sendall(entrada.encode('utf-8'))
            if entrada.lower() == "salir":
                print("Desconectado del servidor.")
                break
    finally:
        cliente.close()

if __name__ == "__main__":
    iniciar_cliente()