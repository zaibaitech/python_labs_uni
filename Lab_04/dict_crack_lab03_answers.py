""" Script: dict_crack.py
    Description: Cracks password hash using a dictionary of common passwords.
    Author: Petra L
    Modified: June 2021
    PEP8 Compliant
    Note: You will require this file for Lab 03, 04, and 05
    THIS DOES NOT WORK CORRECTLY BUT I DON'T KNOW WHY!!!!
"""

import hashlib
from typing import Union  # for function annotations

# list of common passwords
common = ["123", "1234", "12345", "123456", "1234567", "12345678",
          "password", "qwerty", "abc", "abcd", "abc123", "111111",
          "monkey", "arsenal", "letmein", "trustno1", "dragon",
          "baseball", "superman", "iloveyou", "starwars",
          "montypython", "cheese", "123123", "football", "batman"]


def dict_attack(passwd_hash: str) -> Union[str, None]:
    """Dictionary attack,
    checks password hash against a list of common passwords
    while using a for loop"""
    print(f"[*] Cracking hash: {passwd_hash}")
    passwd_found = None
    for word in common:
        hsh = hashlib.md5(word.encode())
        if hsh.hexdigest() == passwd_hash:
            passwd_found = word
            break
        else:
            word1 = word.upper()
            hsh1 = hashlib.md5(word1.encode())
            if hsh1.hexdigest() == passwd_hash:
                passwd_found = word1
                break
            else:
                word2 = word.capitalize()
                hsh2 = hashlib.md5(word2.encode())
                if hsh2.hexdigest() == passwd_hash:
                    passwd_found = word2
                    break

    if passwd_found:
        print(f"[+] Password recovered: {passwd_found}")
    else:
        print("[-] Password not recovered")
    return passwd_found


def main():
    """Test cases"""
    print("[dict_crack] Tests")
    passwd_hash = "44ec94bbfc520c644ce2748eb3bdef6d"
    dict_attack(passwd_hash)
    passwd_hash = "d8578edf8458ce06fbc5bb76a58c5ca4"
    dict_attack(passwd_hash)
    passwd_hash = "478bf2de70f915a6320a5451c3d7fdb9"
    dict_attack(passwd_hash)
    passwd_hash = "a67778b3dcc82bfaace0f8bc0061f20e"
    dict_attack(passwd_hash)
    passwd_hash = "4297f44b13955235245b2497399d7a92"
    dict_attack(passwd_hash)


if __name__ == "__main__":
    main()
