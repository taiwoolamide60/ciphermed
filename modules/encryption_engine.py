
"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module Name : encryption_engine.py

Purpose:
    Provides all encryption and decryption services used by CipherMed.

Responsibilities:
    • Caesar Cipher
    • Additive Cipher
    • Vigenère Cipher
    • Encryption
    • Decryption
    • Cipher selection

Author:
    TAIWO OLAMIDE AKINBOBOLA
===============================================================================
"""

import string


class EncryptionEngine:
    """
    CipherMed Encryption Engine.
    Implements all classical ciphers used by the system.
    """

    def __init__(self):
        self.alphabet = string.ascii_uppercase

    def encrypt(self, algorithm, plaintext, key):
        if algorithm == "Caesar Cipher":
            return self.caesar_encrypt(
                plaintext,
                int(key)
            )

        elif algorithm == "Additive Cipher":
            return self.additive_encrypt(
                plaintext,
                int(key)
            )

        elif algorithm == "Vigenère Cipher":
            return self.vigenere_encrypt(
                plaintext,
                key.upper()
            )

        return plaintext

    def decrypt(self, algorithm, ciphertext, key):
        if algorithm == "Caesar Cipher":
            return self.caesar_decrypt(
                ciphertext,
                int(key)
            )

        elif algorithm == "Additive Cipher":
            return self.additive_decrypt(
                ciphertext,
                int(key)
            )

        elif algorithm == "Vigenère Cipher":
            return self.vigenere_decrypt(
                ciphertext,
                key.upper()
            )

        return ciphertext

    def caesar_encrypt(self, text, shift):
        result = ""

        for character in text:
            if character in string.ascii_uppercase:
                offset = ord("A")

                encrypted = chr(
                    ((ord(character) - offset + shift) % 26)
                    + offset
                )

                result += encrypted

            elif character in string.ascii_lowercase:
                offset = ord("a")

                encrypted = chr(
                    ((ord(character) - offset + shift) % 26)
                    + offset
                )

                result += encrypted

            else:
                # Preserve spaces, punctuation, digits, and other characters.
                result += character

        return result

    def caesar_decrypt(self, text, shift):
        return self.caesar_encrypt(
            text,
            -shift
        )

    def additive_encrypt(self, text, key):
        return self.caesar_encrypt(
            text,
            key
        )

    def additive_decrypt(self, text, key):
        return self.caesar_decrypt(
            text,
            key
        )

    def vigenere_encrypt(self, plaintext, keyword):
        encrypted = ""
        key_index = 0

        keyword = keyword.upper()

        if not keyword or not all(
            character in string.ascii_uppercase
            for character in keyword
        ):
            raise ValueError(
                "The Vigenère key must contain at least one letter "
                "from A to Z only."
            )

        for character in plaintext:
            if character in string.ascii_uppercase:
                shift = ord(
                    keyword[key_index % len(keyword)]
                ) - ord("A")

                encrypted += chr(
                    (
                        ord(character)
                        - ord("A")
                        + shift
                    ) % 26
                    + ord("A")
                )

                key_index += 1

            elif character in string.ascii_lowercase:
                shift = ord(
                    keyword[key_index % len(keyword)]
                ) - ord("A")

                encrypted += chr(
                    (
                        ord(character)
                        - ord("a")
                        + shift
                    ) % 26
                    + ord("a")
                )

                key_index += 1

            else:
                # Preserve spaces, punctuation, digits, and line breaks.
                # These characters do not advance the Vigenère key.
                encrypted += character

        return encrypted

    def vigenere_decrypt(self, ciphertext, keyword):
        decrypted = ""
        key_index = 0

        keyword = keyword.upper()

        if not keyword or not all(
            character in string.ascii_uppercase
            for character in keyword
        ):
            raise ValueError(
                "The Vigenère key must contain at least one letter "
                "from A to Z only."
            )

        for character in ciphertext:
            if character in string.ascii_uppercase:
                shift = ord(
                    keyword[key_index % len(keyword)]
                ) - ord("A")

                decrypted += chr(
                    (
                        ord(character)
                        - ord("A")
                        - shift
                    ) % 26
                    + ord("A")
                )

                key_index += 1

            elif character in string.ascii_lowercase:
                shift = ord(
                    keyword[key_index % len(keyword)]
                ) - ord("A")

                decrypted += chr(
                    (
                        ord(character)
                        - ord("a")
                        - shift
                    ) % 26
                    + ord("a")
                )

                key_index += 1

            else:
                # Preserve spaces, punctuation, digits, and line breaks.
                # These characters do not advance the Vigenère key.
                decrypted += character

        return decrypted
