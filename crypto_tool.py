import getpass

from cryptography.fernet import InvalidToken
from core import generate_key, load_key, save_key_with_password, load_key_with_password
from encryptor import encrypt_message
from decryptor import decrypt_message


def encrypt_text() -> None:
    key = load_key()
    if key is None:
        return
    message = input("\n[>] Enter the text to encrypt: ")
    encrypted = encrypt_message(message, key)
    print("\n--- ENCRYPTION RESULT ---")
    print(f"Encrypted Text: {encrypted.decode()}")
    print("-------------------------")


def decrypt_text() -> None:
    key = load_key()
    if key is None:
        return
    encrypted_input = input("\n[>] Enter the encrypted text to decrypt: ").encode()
    try:
        decrypted = decrypt_message(encrypted_input, key)
        print("\n--- DECRYPTION RESULT ---")
        print(f"Decrypted Text: {decrypted}")
        print("-------------------------")
    except InvalidToken:
        print("\n[!] Error: Invalid key or corrupted encrypted text.")


def generate_key_from_password() -> None:
    password = getpass.getpass("\n[>] Enter password (hidden): ")
    confirm = getpass.getpass("[>] Confirm password (hidden): ")
    if password != confirm:
        print("\n[!] Error: Passwords do not match.")
        return
    save_key_with_password(password)


def encrypt_text_with_password() -> None:
    password = getpass.getpass("\n[>] Enter password (hidden): ")
    key = load_key_with_password(password)
    if key is None:
        return
    message = input("[>] Enter the text to encrypt: ")
    try:
        encrypted = encrypt_message(message, key)
        print("\n--- ENCRYPTION RESULT ---")
        print(f"Encrypted Text: {encrypted.decode()}")
        print("-------------------------")
    except Exception:
        print("\n[!] Error: Wrong password or corrupted key file.")


def decrypt_text_with_password() -> None:
    password = getpass.getpass("\n[>] Enter password (hidden): ")
    key = load_key_with_password(password)
    if key is None:
        return
    encrypted_input = input("[>] Enter the encrypted text to decrypt: ").encode()
    try:
        decrypted = decrypt_message(encrypted_input, key)
        print("\n--- DECRYPTION RESULT ---")
        print(f"Decrypted Text: {decrypted}")
        print("-------------------------")
    except InvalidToken:
        print("\n[!] Error: Wrong password or corrupted encrypted text.")


def display_menu() -> None:
    print("""
          ____            __     __   _   _       _
         |  _ \  _____   _\ \   / /__| |_| |_ ___| |
         | | | |/ _ \ \ / /\ \ / / _ \ __| __/ _ \ |
         | |_| |  __/\ V /  \ V /  __/ |_| ||  __/ |
         |____/ \___| \_/    \_/ \___|\__|\__\___|_|
    """)
    print("=" * 42)
    print("   EncodeX by DevVettel - CLI TOOL")
    print("=" * 42)
    print("  -- Random Key Mode --")
    print("  1. Generate New Key")
    print("  2. Encrypt a Message")
    print("  3. Decrypt a Message")
    print("  -- Password Key Mode --")
    print("  4. Generate Key from Password")
    print("  5. Encrypt with Password")
    print("  6. Decrypt with Password")
    print("  7. Exit")
    print("=" * 42)


if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("[?] Select an option (1-7): ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            encrypt_text()
        elif choice == '3':
            decrypt_text()
        elif choice == '4':
            generate_key_from_password()
        elif choice == '5':
            encrypt_text_with_password()
        elif choice == '6':
            decrypt_text_with_password()
        elif choice == '7':
            print("\nExiting the tool.\n")
            break
        else:
            print("\n[!] Invalid choice. Please try again.")
