# EncodeX — CLI Crypto Tool 🔐

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A lightweight command-line cryptography tool built with Python. EncodeX lets you generate secure encryption keys, encrypt sensitive messages, and decrypt them using the **Fernet** symmetric encryption algorithm.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🔑 Key Generation | Generates a cryptographically secure, URL-safe base64-encoded key |
| 🔒 Encryption | Converts plaintext into unreadable ciphertext |
| 🔓 Decryption | Reverts ciphertext back to readable plaintext using the correct key |
| 🖥️ Interactive CLI | Easy-to-use menu-driven interface |

---

## 📋 Requirements

- Python 3.x
- `cryptography` library

---

## ⚙️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/DevVettel/EncodeX.git
cd EncodeX
```

**2. Install dependencies:**
```bash
pip install cryptography
```

---

## 💻 Usage

Run the main script to launch the interactive tool:
```bash
python crypto_tool.py
```

Follow the on-screen menu to:
- Generate a new encryption key
- Encrypt a message
- Decrypt a message

---

## 📁 Project Structure
```
EncodeX/
├── crypto_tool.py   # Main CLI application
└── secret.key       # Generated encryption key (auto-created)
```

---

## ⚠️ Security Disclaimer

> This tool is intended for **educational purposes** to demonstrate the basics of symmetric cryptography.

- 🔐 Keep your `secret.key` file **secure and private**
- ❌ If you lose the key, your encrypted messages **cannot be recovered**
- 👁️ Anyone with access to `secret.key` can decrypt your messages

---

<p align="center">Made with 🖤 by <a href="https://github.com/DevVettel">DevVettel</a></p>
