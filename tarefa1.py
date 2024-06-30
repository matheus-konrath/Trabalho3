import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Servidor aguardando conexao...")
    client_socket, addr = server_socket.accept()
    print(f"Conexao estabelecida com {addr}")

    data = client_socket.recv(1024)
    print(f"Dados recebidos: {data.decode('utf-8')}")
    client_socket.sendall(b"Dados recebidos")
    client_socket.close()

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345)) 
    client_socket.sendall(b"Dados do cliente")
    data = client_socket.recv(1024)
    print(f"Resposta do servidor: {data.decode('utf-8')}")
    client_socket.close()
