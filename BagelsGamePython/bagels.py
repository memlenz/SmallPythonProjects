#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Nom du fichier : bagels.py
    Description : Un jeu de déduction logique pour
    deviner un nombre secret à trois chiffres.
    Vous avez 10 chances pour deviner le nombre.
    - Pico -> Un chiffre correct, mauvaise position.
    - Fermi -> Un chiffre correct, bonne position.
    - Bagels -> Aucun chiffre correct.

    Auteur : ADEBI Châ-Fine Ayédoun achafine@gmail.com
    Date : 03/16/2025
"""

import random

# Constante
GUESSES = 10  # NOMBRE DE CHANCES
DIGIT_LEN = 3  # NOMBRE DE CHIFFRES DU NOMBRE
MENU = """
    Bagels, a deductive logic game.
    By ADEBI Ayedoun Châ-Fine achafine@gmail.com

    Je suis en train de penser à un nombre à 3 chiffres.
    Essais de deviner lequel.
    Voici quelques indices :
    Quand je dis:       Voici ce à quoi je pense:
        Pico            Un chiffre est correct mais à la mauvaise position
        Fermi           Un chiffre est correct et à la bonne position
        Bagels          Aucun des chiffres n'est correct
    Vous avez 10 essais :
"""


def generer_nombre_secret():
    """ Générer un nombre secret unique à trois chiffres
    sous forme de liste.
    """
    chiffres = list(range(1, 10))
    random.shuffle(chiffres)
    return [str(chiffres[i]) for i in range(DIGIT_LEN)]


def obtenir_indices(input_list, guess_number):
    """Comparer l'entrée utilisateur avec le nombre secret
    et retourne des indices.
    """
    result = []
    for i in range(len(input_list)):
        if input_list[i] == guess_number[i]:
            result.append("Fermi")
        elif input_list[i] in guess_number:
            result.append("Pico")
    return " ".join(result) if result else "Bagels"


def valide_saisie():
    """Gère l'entrée utilisateur, l'utilisateur doit entrer
    un nombre à trois chiffres"""
    while True:
        saisie = input("> ").strip()
        if len(saisie) == DIGIT_LEN and saisie.isdigit():
            return list(saisie)
        print("Entrée invalide, vous devez entrer un nombre à trois chiffres")


def main():
    """Boucle principale du jeu"""
    rejouer = ""
    while True:
        guess_number = generer_nombre_secret()
        for i in range(GUESSES):
            print("Devine #", i+1)
            input_nbre = valide_saisie()
            if input_nbre == guess_number:
                print("Vous l'avez trouvé")
                break
            else:
                print(obtenir_indices(input_nbre, guess_number))
        else:
            print("Game Over!")
        print("Voulez-vous encore jouer ?? (oui ou non)")
        while True:
            rejouer = input("> ").strip().lower()
            if rejouer in ["oui", "non"]:
                break
            else:
                print("Vous devez répondre par 'oui' ou 'non' ")
        if rejouer == "non":
            print("Merci d'avoir joué")
            break


if __name__ == "__main__":
    print(MENU)
    main()
