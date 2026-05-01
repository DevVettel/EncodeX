import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

KEY_FILE = "secret.key"
_PBKDF2_ITERATIONS = 480_000


def generate_key() -> None:
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"\n[+] Success: New key generated and saved as '{KEY_FILE}'")


def load_key() -> bytes | None:
    if not os.path.exists(KEY_FILE):
        print(f"\n[!] Error: '{KEY_FILE}' not found. Please generate a key first.")
        return None
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def derive_key_from_password(password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    if salt is None:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=_PBKDF2_ITERATIONS,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return salt, key


def save_key_with_password(password: str) -> None:
    salt, key = derive_key_from_password(password)
    with open(KEY_FILE, "wb") as f:
        f.write(salt + b":" + key)
    print(f"\n[+] Success: Password-derived key saved as '{KEY_FILE}'")


def load_key_with_password(password: str) -> bytes | None:
    if not os.path.exists(KEY_FILE):
        print(f"\n[!] Error: '{KEY_FILE}' not found.")
        return None
    with open(KEY_FILE, "rb") as f:
        data = f.read()
    salt, _ = data.split(b":", 1)
    _, key = derive_key_from_password(password, salt)
    return key
