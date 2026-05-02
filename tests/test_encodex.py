import os
import tempfile
import unittest
from cryptography.fernet import Fernet, InvalidToken

import core
from encryptor import encrypt_message
from decryptor import decrypt_message


class TestCore(unittest.TestCase):
    def setUp(self):
        self._orig_dir = os.getcwd()
        self._tmpdir = tempfile.TemporaryDirectory()
        os.chdir(self._tmpdir.name)

    def tearDown(self):
        os.chdir(self._orig_dir)
        self._tmpdir.cleanup()

    def test_generate_key_creates_file(self):
        core.generate_key()
        self.assertTrue(os.path.exists(core.KEY_FILE))

    def test_generate_key_produces_valid_fernet_key(self):
        core.generate_key()
        with open(core.KEY_FILE, "rb") as f:
            key = f.read()
        Fernet(key)  # raises ValueError if key is invalid

    def test_load_key_returns_bytes(self):
        core.generate_key()
        self.assertIsInstance(core.load_key(), bytes)

    def test_load_key_matches_saved_key(self):
        core.generate_key()
        with open(core.KEY_FILE, "rb") as f:
            raw = f.read()
        self.assertEqual(core.load_key(), raw)

    def test_load_key_missing_file_returns_none(self):
        self.assertIsNone(core.load_key())

    def test_each_generate_produces_unique_key(self):
        core.generate_key()
        key1 = core.load_key()
        core.generate_key()
        key2 = core.load_key()
        self.assertNotEqual(key1, key2)


class TestEncryptor(unittest.TestCase):
    def test_returns_bytes(self):
        key = Fernet.generate_key()
        self.assertIsInstance(encrypt_message("hello", key), bytes)

    def test_output_differs_from_plaintext(self):
        key = Fernet.generate_key()
        self.assertNotEqual(encrypt_message("hello", key), b"hello")

    def test_is_nondeterministic(self):
        key = Fernet.generate_key()
        self.assertNotEqual(encrypt_message("hello", key), encrypt_message("hello", key))

    def test_empty_string(self):
        key = Fernet.generate_key()
        result = encrypt_message("", key)
        self.assertIsInstance(result, bytes)
        self.assertGreater(len(result), 0)

    def test_unicode_input(self):
        key = Fernet.generate_key()
        result = encrypt_message("merhaba dünya 🔐", key)
        self.assertIsInstance(result, bytes)


class TestDecryptor(unittest.TestCase):
    def test_roundtrip(self):
        key = Fernet.generate_key()
        encrypted = encrypt_message("test message", key)
        self.assertEqual(decrypt_message(encrypted, key), "test message")

    def test_roundtrip_unicode(self):
        key = Fernet.generate_key()
        text = "şifreleme testi 🔑"
        self.assertEqual(decrypt_message(encrypt_message(text, key), key), text)

    def test_roundtrip_empty_string(self):
        key = Fernet.generate_key()
        self.assertEqual(decrypt_message(encrypt_message("", key), key), "")

    def test_wrong_key_raises_invalid_token(self):
        key1 = Fernet.generate_key()
        key2 = Fernet.generate_key()
        encrypted = encrypt_message("secret", key1)
        with self.assertRaises(InvalidToken):
            decrypt_message(encrypted, key2)

    def test_corrupted_data_raises_invalid_token(self):
        key = Fernet.generate_key()
        with self.assertRaises(InvalidToken):
            decrypt_message(b"this-is-not-valid-ciphertext", key)

    def test_empty_bytes_raises_invalid_token(self):
        key = Fernet.generate_key()
        with self.assertRaises(InvalidToken):
            decrypt_message(b"", key)


if __name__ == "__main__":
    unittest.main()
