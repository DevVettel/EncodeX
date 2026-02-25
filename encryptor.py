from cryptography.fernet import Fernet

def generate_and_save_key():
    """
    Generates a new Fernet key and saves it to a file.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    
    print("[+] Key successfully generated and saved to 'secret.key'")
    return key

def encrypt_message(plaintext, key):
    """
    Encrypts a plaintext message using the provided key.
    """
    f = Fernet(key)
    # Fernet requires bytes, so we encode the string
    encrypted_data = f.encrypt(plaintext.encode()) 
    return encrypted_data

# --- Main Execution ---
if __name__ == "__main__":
    # 1. Generate the key
    current_key = generate_and_save_key()
    
    # 2. Get user input
    message = input("\nEnter the secret message to encrypt: ")
    
    # 3. Encrypt the message
    encrypted_message = encrypt_message(message, current_key)
    
    # 4. Display results
    print("\n--- ENCRYPTION SUCCESSFUL ---")
    print(f"Original Message  : {message}")
    print(f"Encrypted Message : {encrypted_message.decode()}")