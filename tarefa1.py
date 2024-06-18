import socket
import threading
import random
import time
import json

# Função para simular geração de dados de sensores RFID
def generate_sensor_data():
    return {
        'sensor_id': random.randint(1, 100),
        'timestamp': time.time(),
        'data': random.random()
    }

# Função do servidor
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("Servidor esperando conexões...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão de {addr}")
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Dados recebidos: {data.decode()}")
        client_socket.close()

# Função do cliente
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    data = generate_sensor_data()
    client_socket.send(json.dumps(data).encode())
    client_socket.close()

# Iniciar servidor em uma thread separada
server_thread = threading.Thread(target=server)
server_thread.start()

# Simular envio de dados do cliente
time.sleep(1)
client()
