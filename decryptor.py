from cryptography.fernet import Fernet

def load_key():
    """
    Loads the previously generated key from 'secret.key'.
    """
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def decrypt_message(encrypted_message, key):
    """
    Decrypts an encrypted message using the provided key.
    """
    f = Fernet(key)
    # Decrypts the message and decodes the bytes back to a string
    decrypted_data = f.decrypt(encrypted_message).decode()
    return decrypted_data


if __name__ == "__main__":
    # 1. Load the existing key
    current_key = load_key()
    
    # 2. Get user input
    encrypted_input = input("\nEnter the encrypted message to decrypt: ").encode()
    
    # 3. Decrypt the message with error handling
    try:
        decrypted_message = decrypt_message(encrypted_input, current_key)
        
        # 4. Display results
        print("\n--- DECRYPTION SUCCESSFUL ---")
        print(f"Decrypted Message : {decrypted_message}")
        
    except Exception as e:
        print("\n[!] Error during decryption. Please check the encrypted string or ensure the correct 'secret.key' is present.")