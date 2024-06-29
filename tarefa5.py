from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def sign_data(private_key, data):
    try:
        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    except Exception as e:
        print(f"Erro na assinatura: {e}")

def verify_signature(public_key, data, signature):
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except Exception as e:
        print(f"Erro na verificação da assinatura: {e}")

if __name__ == "__main__":
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    data = b"Dados importantes"
    signature = sign_data(private_key, data)
    print(f"Assinatura: {signature}")

    try:
        verify_signature(public_key, data, signature)
        print("Assinatura verificada com sucesso!")
    except Exception as e:
        print(f"Falha na verificação da assinatura: {e}")
