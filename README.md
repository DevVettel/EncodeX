<div align="center">

```
       _____                     _     __  __
      | ____|_ __   ___ ___   __| | ___\ \/ /
      |  _| | '_ \ / __/ _ \ / _` |/ _ \\  / 
      | |___| | | | (_| (_) | (_| |  __//  \ 
      |_____|_| |_|\___\___/ \__,_|\___/_/\_\
```

**A command-line cryptography toolkit built with Python.**

[![Tests](https://github.com/DevVettel/EncodeX/actions/workflows/test.yml/badge.svg)](https://github.com/DevVettel/EncodeX/actions/workflows/test.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## Overview

EncodeX is a lightweight CLI tool for symmetric encryption using the **Fernet** algorithm (AES-128-CBC + HMAC-SHA256). It supports both random key generation and **password-based key derivation** via PBKDF2-SHA256, making encrypted messages both portable and human-memorable.

---

## Features

| | Feature | Description |
|---|---|---|
| 🔑 | Random Key Generation | Cryptographically secure, URL-safe base64-encoded key |
| 🔒 | Encryption | Converts plaintext into authenticated ciphertext |
| 🔓 | Decryption | Reverts ciphertext to plaintext with key verification |
| 🔐 | Password Mode | Derives a key from a password using PBKDF2-SHA256 (480k iterations) |
| 🧪 | Test Suite | 15 unit tests via Python's built-in `unittest` |
| ⚙️ | CI Pipeline | Automated testing on every push via GitHub Actions |

---

## Installation

```bash
git clone https://github.com/DevVettel/EncodeX.git
cd EncodeX
pip install -r requirements.txt
```

---

## Usage

```bash
python crypto_tool.py
```

```
       ____            __     __   _   _       _ 
      |  _ \  _____   _\ \   / /__| |_| |_ ___| |
      | | | |/ _ \ \ / /\ \ / / _ \ __| __/ _ \ |
      | |_| |  __/\ V /  \ V /  __/ |_| ||  __/ |
      |____/ \___| \_/    \_/ \___|\__|\__\___|_|

==========================================
   EncodeX by DevVettel - CLI TOOL
==========================================
  -- Random Key Mode --
  1. Generate New Key
  2. Encrypt a Message
  3. Decrypt a Message
  -- Password Key Mode --
  4. Generate Key from Password
  5. Encrypt with Password
  6. Decrypt with Password
  7. Exit
==========================================
```

### Random Key Mode
Generate a key once, then use it to encrypt and decrypt messages. The key is saved to `secret.key` — keep this file secure.

### Password Mode
No key file needed. A key is derived from your password using PBKDF2-SHA256 with a random salt. The salt is stored alongside the derived key so the same password always produces the same key.

You can also use the standalone modules directly:

```bash
python encryptor.py   # encrypt a message using the saved key
python decryptor.py   # decrypt a message using the saved key
```

---

## Project Structure

```
EncodeX/
├── core.py              # Shared key management and PBKDF2 logic
├── crypto_tool.py       # Interactive CLI (main entry point)
├── encryptor.py         # Standalone encryption module
├── decryptor.py         # Standalone decryption module
├── tests/
│   └── test_encodex.py  # 15 unit tests (unittest)
├── .github/
│   └── workflows/
│       └── test.yml     # GitHub Actions CI pipeline
├── requirements.txt
└── requirements-dev.txt
```

---

## Running Tests

No extra dependencies needed — uses Python's built-in `unittest`:

```bash
python -m unittest discover tests/ -v
```

---

## Security Notes

> EncodeX is built for **educational purposes** to demonstrate symmetric cryptography fundamentals. Do not use it to protect production or sensitive data.

- `secret.key` is excluded from version control via `.gitignore` — never commit it
- Losing the key makes encrypted messages **unrecoverable**
- Anyone with access to the key file can decrypt all messages encrypted with it
- Password-based keys are only as strong as the password itself

---

<div align="center">
  Made with 🖤 by <a href="https://github.com/DevVettel">DevVettel</a>
</div>
