from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import Salsa20
from cryptography.fernet import Fernet
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

# Funções de criptografia e descriptografia para Salsa20
def encrypt_salsa20(data, key):
    try:
        cipher = Salsa20.new(key=key)
        encrypted_data = cipher.nonce + cipher.encrypt(data)
        return encrypted_data
    except Exception as e:
        print(f"Erro na criptografia Salsa20: {e}")

def decrypt_salsa20(encrypted_data, key):
    try:
        nonce = encrypted_data[:8]
        cipher = Salsa20.new(key=key, nonce=nonce)
        data = cipher.decrypt(encrypted_data[8:])
        return data
    except Exception as e:
        print(f"Erro na descriptografia Salsa20: {e}")

# Funções de criptografia e descriptografia para Fernet
def encrypt_fernet(data, key):
    try:
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        return encrypted_data
    except Exception as e:
        print(f"Erro na criptografia Fernet: {e}")

def decrypt_fernet(encrypted_data, key):
    try:
        fernet = Fernet(key)
        data = fernet.decrypt(encrypted_data)
        return data
    except Exception as e:
        print(f"Erro na descriptografia Fernet: {e}")
