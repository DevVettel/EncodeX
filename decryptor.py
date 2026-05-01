from cryptography.fernet import Fernet, InvalidToken
from core import load_key

def decrypt_message(encrypted_message: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

if __name__ == "__main__":
    key = load_key()
    if key is None:
        exit(1)

    encrypted_input = input("\nEnter the encrypted message to decrypt: ").encode()

    try:
        decrypted = decrypt_message(encrypted_input, key)
        print("\n--- DECRYPTION SUCCESSFUL ---")
        print(f"Decrypted Message : {decrypted}")
    except InvalidToken:
        print("\n[!] Error: Invalid key or corrupted encrypted text.")
