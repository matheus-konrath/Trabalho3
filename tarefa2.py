from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_aes(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(data) + encryptor.finalize()
    return iv + ct

def decrypt_aes(data, key):
    iv = data[:16]
    ct = data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ct) + decryptor.finalize()

# Função para encriptar dados usando ChaCha20
def encrypt_chacha20(data, key):
    nonce = os.urandom(16)
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(data) + encryptor.finalize()
    return nonce + ct

# Função para desencriptar dados usando ChaCha20
def decrypt_chacha20(data, key):
    nonce = data[:16]
    ct = data[16:]
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ct) + decryptor.finalize()

if __name__ == "__main__":
    key = os.urandom(32)
    data = "Dados sensíveis do sensor".encode('utf-8')  # Codificar como UTF-8

    # Teste com AES
    encrypted_data_aes = encrypt_aes(data, key)
    print(f"Dados encriptados com AES: {encrypted_data_aes}")
    decrypted_data_aes = decrypt_aes(encrypted_data_aes, key)
    print(f"Dados desencriptados com AES: {decrypted_data_aes.decode('utf-8')}")  # Decodificar como UTF-8

    # Teste com ChaCha20
    encrypted_data_chacha20 = encrypt_chacha20(data, key)
    print(f"Dados encriptados com ChaCha20: {encrypted_data_chacha20}")
    decrypted_data_chacha20 = decrypt_chacha20(encrypted_data_chacha20, key)
    print(f"Dados desencriptados com ChaCha20: {decrypted_data_chacha20.decode('utf-8')}")  # Decodificar como UTF-8
