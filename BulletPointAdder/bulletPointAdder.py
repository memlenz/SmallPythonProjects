#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Nom du fichier : bulletPointAdder.py
    Description : Formate du texte pour obtenir une liste à puce
    Auteur : ADEBI Châ-Fine Ayédoun achafine@gmail.com
    Date : 2025-04-08
"""


import re
import pyperclip


# Constantes
BULLET = '.'  # Vos nouvelles lignes peuvent commencer par: '•', '-', '*', '→'
REGEX = r'^[\d\.\)\s\-_]+'  # Vous pouvez changer le la logique des lignes


def paste_from_clipboard() -> str:
    """On récupère le contenu du clipboard"""
    return pyperclip.paste()


def bullet_point_adder() -> str:
    """On modifie chaque ligne pour en faire des listes à puces"""
    content = paste_from_clipboard().strip()
    # On convertis le contenu en liste
    list_content = content.split('\n')
    # Formatage des lignes
    formated_lines = []
    for line in list_content:
        line = line.strip()
        # Gestion des lignes vides
        if not line:
            formated_lines.append(line)
            continue
        # Gestion des lignes qui commencent par des chiffres
        line = re.sub(REGEX, '', line)
        # Ajout des puces
        if not line.startswith(BULLET):
            line = f'{BULLET} {line}'
        formated_lines.append(line)
    return '\n'.join(formated_lines)


def paste_to_clipboard() -> None:
    """On copie le contenu dans le clipboard"""
    pyperclip.copy(bullet_point_adder())


if __name__ == "__main__":
    welcome = "Welcome to the Bullet Point Adder"
    print(welcome.center(len(welcome) + 5, '*'))
    try:
        print("Processing".ljust(len(welcome)+5, '.'))
        paste_to_clipboard()
        print("successfully paste".center(len(welcome) + 5, '*'))
    except Exception as e:
        print(f"Erreur : {str(e)}")
