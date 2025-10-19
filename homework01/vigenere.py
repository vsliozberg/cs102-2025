"""
This module implements the Vigenere cipher for encryption and decryption.
It provides two main functions:
1. encrypt_vigenere: Encrypts a given plaintext using the Vigenere cipher.
2. decrypt_vigenere: Decrypts a given ciphertext using the Vigenere cipher.
"""

from math import ceil


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    keyword = keyword * ceil(len(plaintext) / len(keyword))
    for i in range(len(plaintext)):
        shift = ord(keyword[i]) - ord("A")
        if "A" <= plaintext[i] <= "Z":  # Заглавные буквы
            ciphertext += chr((ord(plaintext[i]) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= plaintext[i] <= "z":  # Строчные буквы
            ciphertext += chr((ord(plaintext[i]) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += plaintext[i]  # Остальные символы не меняем
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    keyword = keyword * ceil(len(ciphertext) / len(keyword))
    for i in range(len(ciphertext)):
        shift = ord(keyword[i]) - ord("A")
        if "A" <= ciphertext[i] <= "Z":  # Заглавные буквы
            plaintext += chr((ord(ciphertext[i]) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= ciphertext[i] <= "z":  # Строчные буквы
            plaintext += chr((ord(ciphertext[i]) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += ciphertext[i]  # Остальные символы не меняем
    return plaintext
