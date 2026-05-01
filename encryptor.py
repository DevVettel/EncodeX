from cryptography.fernet import Fernet
from core import load_key

def encrypt_message(plaintext: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(plaintext.encode())

if __name__ == "__main__":
    key = load_key()
    if key is None:
        exit(1)

    message = input("\nEnter the secret message to encrypt: ")
    encrypted = encrypt_message(message, key)

    print("\n--- ENCRYPTION SUCCESSFUL ---")
    print(f"Original Message  : {message}")
    print(f"Encrypted Message : {encrypted.decode()}")
