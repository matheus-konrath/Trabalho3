from hashlib import sha256

def generate_hash(data):
    return sha256(data).hexdigest()

if __name__ == "__main__":
    data = b"Dados para hash"
    data_hash = generate_hash(data)
    print(f"Hash dos dados: {data_hash}")
