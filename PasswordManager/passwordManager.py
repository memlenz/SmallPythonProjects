# !/usr/bin/env python3
# -*- coding : utf-8 -*-


"""
    Nom du fichier : bulletPointAdder.py
    Description : Formate du texte pour obtenir une liste à puce
    Auteur : ADEBI Châ-Fine Ayédoun achafine@gmail.com
    Date : 2025-04-12
"""


import string
import json
import os
import argparse
import secrets
import pyperclip


# Constantes
PASSWORD_LENGTH = 12  # Vous pouvez choisir la taille que vous voulez
# Mettez à False si vous ne voulez pas abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
NEED_STRING = True
NEED_DIGITS = True  # Mettez à False si vous ne voulez pas 0123456789
# Mettez à False si vous ne voulez pas !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
NEED_SPECIAL_CHARACTERS = True
FILE_PATH = "password.json"  # Le chemin par défaut du mot de passe
DEFAULT_INDENT = 4  # L'indentation par default


def generate_password():
    """Générer un mot de passe"""
    characters = ''
    if NEED_STRING:
        characters += string.ascii_letters
    if NEED_DIGITS:
        characters += string.digits
    if NEED_SPECIAL_CHARACTERS:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(PASSWORD_LENGTH))


def save_password(account, password, file_path=FILE_PATH):
    """Sauvegarder un mot de passe"""
    passwords = load_passwords()
    passwords[account] = password
    with open(file_path, 'w') as file:
        json.dump(passwords, file, indent=DEFAULT_INDENT)
        print("Password saved successfully !")


def load_passwords(file_path=FILE_PATH):
    """On charge les mots de passe"""
    if not os.path.exists(file_path):
        print(f"Error: Path '{file_path}' doesn't exist !")
        return {}
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, dict):
                print("Error: The Json content is not a dictionary !")
                return {}
        return data
    except json.JSONDecodeError:
        print("Error: Json file is empty or corrupted !")
        return {}
    except Exception as e:
        print(f"Error: An unexpected error occured : {e} !")
        return {}


def get_password(account):
    """Obtenir le mot de passe d'un compte"""
    passwords = load_passwords()
    password = passwords.get(account, None)
    if not passwords:
        print("The json file is empty !")
        return ''
    if not password:
        print(f"Error: There is no password matching the account {account} !")
        return ''
    return password


def delete_password(account, file_path=FILE_PATH):
    passwords = load_passwords()
    if passwords.get(account) is None:
        print(f"Error: the account {account} doesn't exist !")
        return False
    del passwords[account]
    with open(file_path, 'w') as file:
        json.dump(passwords, file, indent=DEFAULT_INDENT)
    print("Password deleted successfully !")
    return True


def setup_cli():
    parser = argparse.ArgumentParser(description="A simple password manager")
    subparsers = parser.add_subparsers(dest='command')

    # command add
    delete_parser = subparsers.add_parser(
        'del', help='Delete a password')
    delete_parser.add_argument('account', help="Account's name")

    # command get
    get_parser = subparsers.add_parser('get', help='Get the password')
    get_parser.add_argument('account', help="Account's name")

    # command save
    save_parser = subparsers.add_parser(
        'save', help='Save a password')
    save_parser.add_argument('account', help="Account's name")
    save_parser.add_argument('password', help='The password')

    # command gen
    generate_parser = subparsers.add_parser('gen', help='Generate a password')
    generate_parser.add_argument('account', help="Account't name")

    # command list
    subparsers.add_parser('list', help='List all saved accounts')

    return parser.parse_args()


def main():
    args = setup_cli()
    if args.command == 'save':
        save_password(args.account, args.password)
    elif args.command == 'get':
        pyperclip.copy(get_password(args.account))
        print("Password copy to clipboard.")
    elif args.command == 'del':
        delete_password(args.account)
    elif args.command == 'gen':
        password = generate_password()
        save_password(args.account, password)
        print(f"Generated password for '{args.account}': {password}")
    elif args.command == 'list':
        passwords = load_passwords()
        if passwords:
            for acc in passwords:
                print(f" - {acc}")
        else:
            print("No password saved !")
    else:
        print('Error: Unknown command !')


if __name__ == "__main__":
    main()
