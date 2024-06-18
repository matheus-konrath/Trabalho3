import subprocess
import threading
import time
import os

# Importar módulos das tarefas
import tarefa1
import tarefa2
import tarefa3
import tarefa5
import tarefa6

# Executar tarefa 1
server_thread = threading.Thread(target=tarefa1.server)
server_thread.start()
time.sleep(1)
tarefa1.client()

# Executar tarefa 2
key = os.urandom(32)
data = "Dados sensíveis do sensor".encode('utf-8')  # Codificar como UTF-8
encrypted_data_aes = tarefa2.encrypt_aes(data, key)
print(f"Dados encriptados com AES: {encrypted_data_aes}")
decrypted_data_aes = tarefa2.decrypt_aes(encrypted_data_aes, key)
print(f"Dados desencriptados com AES: {decrypted_data_aes.decode('utf-8')}")  # Decodificar como UTF-8

encrypted_data_chacha20 = tarefa2.encrypt_chacha20(data, key)
print(f"Dados encriptados com ChaCha20: {encrypted_data_chacha20}")
decrypted_data_chacha20 = tarefa2.decrypt_chacha20(encrypted_data_chacha20, key)
print(f"Dados desencriptados com ChaCha20: {decrypted_data_chacha20.decode('utf-8')}")  # Decodificar como UTF-8

# Executar tarefa 3
data_hash = tarefa3.generate_hash(data)
print(f"Hash dos dados: {data_hash}")

# Executar tarefa 4
subprocess.run(["tarefa4.bat"])

# Executar tarefa 5
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

data = "Dados importantes".encode('utf-8')  # Codificar como UTF-8
signature = tarefa5.sign_data(private_key, data)
print(f"Assinatura: {signature}")

try:
    tarefa5.verify_signature(public_key, data, signature)
    print("Assinatura verificada com sucesso!")
except Exception as e:
    print(f"Falha na verificação da assinatura: {e}")

# Executar tarefa 6
client = tarefa6.setup_mqtt_client()
client.publish("iot/sensor", "Mensagem segura")
client.loop_start()
