from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_aes(data, key):
    try:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return iv + encrypted_data
    except Exception as e:
        print(f"Erro na criptografia AES: {e}")

def decrypt_aes(encrypted_data, key):
    try:
        iv = encrypted_data[:16]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        padded_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
        data = unpadder.update(padded_data) + unpadder.finalize()
        return data
    except Exception as e:
        print(f"Erro na descriptografia AES: {e}")

def encrypt_chacha20(data, key):
    try:
        nonce = os.urandom(16)
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
        return nonce + encrypted_data
    except Exception as e:
        print(f"Erro na criptografia ChaCha20: {e}")

def decrypt_chacha20(encrypted_data, key):
    try:
        nonce = encrypted_data[:16]
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
        decryptor = cipher.decryptor()
        data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
        return data
    except Exception as e:
        print(f"Erro na descriptografia ChaCha20: {e}")
