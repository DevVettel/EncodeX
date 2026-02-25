from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("\n[+] Success: New key generated and saved as 'secret.key'")

def load_key():
    if not os.path.exists("secret.key"):
        print("\n[!] Error: 'secret.key' not found. Please generate a key first.")
        return None
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_text():
    key = load_key()
    if key is None: return

    f = Fernet(key)
    message = input("\n[>] Enter the text to encrypt: ")
    encrypted_message = f.encrypt(message.encode())
    
    print("\n--- ENCRYPTION RESULT ---")
    print(f"Encrypted Text: {encrypted_message.decode()}")
    print("-------------------------")

def decrypt_text():
    key = load_key()
    if key is None: return

    f = Fernet(key)
    encrypted_message = input("\n[>] Enter the encrypted text to decrypt: ").encode()
    
    try:
        decrypted_message = f.decrypt(encrypted_message).decode()
        print("\n--- DECRYPTION RESULT ---")
        print(f"Decrypted Text: {decrypted_message}")
        print("-------------------------")
    except Exception as e:
        print("\n[!] Error: Invalid key or corrupted encrypted text.")

def display_menu():
    print("\n" )
    print("""
          


              ____            __     __   _   _       _ 
             |  _ \  _____   _\ \   / /__| |_| |_ ___| |
             | | | |/ _ \ \ / /\ \ / / _ \ __| __/ _ \ |
             | |_| |  __/\ V /  \ V /  __/ |_| ||  __/ |
             |____/ \___| \_/    \_/ \___|\__|\__\___|_|
           
          




          
          
          
          
          
          
          
          
          """)
    print("\n" + "="*30)
    print("   EncodeX by DevVettel - CLI TOOL   ")
    print("="*30)
    print("1. Generate New Key")
    print("2. Encrypt a Message")
    print("3. Decrypt a Message")
    print("4. Exit")
    print("="*30)
    print("""    






""")

# --- Main Application Loop ---
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("[?] Select an option (1-4): ")
        
        if choice == '1':
            generate_key()
        elif choice == '2':
            encrypt_text()
        elif choice == '3':
            decrypt_text()
        elif choice == '4':
            print("\nExiting the tool.\n")
            break
        else:
            print("\n[!] Invalid choice. Please try again.")