# Password Manager CLI - Gestionnaire de Mots de Passe en Ligne de Commande

## Description
**Password Manager CLI** est un outil simple et sécurisé développé en Python pour la gestion de mots de passe via une interface en ligne de commande. Le programme permet de générer des mots de passe robustes, de les sauvegarder dans un fichier JSON, de les récupérer, de les supprimer et de lister tous les comptes enregistrés. Ce projet démontre efficacement des compétences en programmation, gestion des fichiers, manipulation des exceptions et sécurité.

## Fonctionnalités
- **Génération de mots de passe sécurisés**  
  Utilisation du module `secrets` pour créer des mots de passe robustes combinant lettres, chiffres et caractères spéciaux.
- **Sauvegarde et chargement dans un fichier JSON**  
  Enregistrement des mots de passe avec gestion des erreurs (fichier inexistant, JSON corrompu).
- **Récupération de mot de passe**  
  Possibilité de copier le mot de passe dans le presse-papiers grâce à `pyperclip`.
- **Suppression et listage des comptes**  
  Commandes pour supprimer un mot de passe ou lister tous les comptes enregistrés.
- **Interface CLI conviviale**  
  Utilisation du module `argparse` pour une interaction simplifiée et intuitive via la ligne de commande.

## Mécanisme d'utilisation
- **Sauvegarde d'un mot de passe personnalisé**  
  L'utilisateur peut enregistrer un mot de passe existant pour un compte donné.
- **Génération automatique**  
  Un mot de passe sécurisé est généré automatiquement et sauvegardé pour un compte spécifique.
- **Récupération et copie dans le presse-papiers**  
  Lors de la commande de récupération, le mot de passe est directement copié dans le presse-papiers pour une utilisation rapide.
- **Gestion interactive via sous-commandes**  
  Les commandes `save`, `get`, `del`, `gen` et `list` offrent une gestion complète et intuitive des mots de passe.

## Compétences Python mises en œuvre

### Programmation modulaire et procédurale
- Organisation du code en fonctions distinctes avec des responsabilités précises (génération, sauvegarde, chargement, suppression).
- Utilisation de la fonction `main()` comme point d'entrée pour orchestrer les différentes fonctionnalités.

### Gestion des exceptions et des erreurs
- Mise en place de blocs `try-except` pour gérer spécifiquement les erreurs liées à la lecture du fichier JSON (`json.JSONDecodeError`) et d'autres exceptions inattendues.
- Assurance de la robustesse de l'application grâce à des messages d'erreur explicites.

### Manipulation de fichiers et sérialisation JSON
- Lecture et écriture dans un fichier JSON pour la persistance des données.
- Utilisation de la bibliothèque `json` pour la sérialisation et la désérialisation des données.

### Interface utilisateur en ligne de commande
- Conception d'une interface CLI conviviale à l'aide du module `argparse`.
- Gestion des sous-commandes pour exécuter des opérations spécifiques (sauvegarde, récupération, suppression, génération et listage).

### Sécurité et gestion de la génération de mots de passe
- Utilisation du module `secrets` pour générer des mots de passe à la fois sécurisés et aléatoires.
- Prise en compte des différents types de caractères (lettres, chiffres, caractères spéciaux) pour garantir la robustesse des mots de passe.

### Bonnes pratiques de développement
- Respect des conventions de nommage et de la structure recommandée par PEP 8.
- Documentation via des docstrings et commentaires pour faciliter la compréhension et la maintenance du code.
- Utilisation de constantes pour centraliser la configuration (longueur du mot de passe, chemins de fichier, etc.).

## Installation et prérequis
- **Prérequis :**  
  Python 3.6 ou supérieur.
- **Dépendances :**  
  Ce projet utilise la bibliothèque externe `pyperclip`. Installez-la via pip :
  ```bash
  pip install pyperclip
  ```
- **Installation :**
  1. Clonez le dépôt :
     ```bash
     git clone https://github.com/votre-utilisateur/password-manager-cli.git
     cd password-manager-cli
     ```
  2. Rendez le script exécutable (optionnel) :
     ```bash
     chmod +x passwordManager.py
     ```

## Utilisation
Exécutez le script depuis votre terminal en spécifiant la commande désirée :

- **Sauvegarder un mot de passe personnalisé :**
  ```bash
  ./passwordManager.py save monCompte monMotDePasse
  ```

- **Récupérer le mot de passe d'un compte (copie dans le presse-papiers) :**
  ```bash
  ./passwordManager.py get monCompte
  ```

- **Supprimer un mot de passe :**
  ```bash
  ./passwordManager.py del monCompte
  ```

- **Générer et sauvegarder un mot de passe sécurisé :**
  ```bash
  ./passwordManager.py gen monCompte
  ```

- **Lister tous les comptes sauvegardés :**
  ```bash
  ./passwordManager.py list
  ```

## Personnalisation
- **Configuration des constantes :**  
  Modifiez les constantes situées en haut du script pour personnaliser :
  - La longueur du mot de passe (`PASSWORD_LENGTH`)
  - Les types de caractères à inclure (`NEED_STRING`, `NEED_DIGITS`, `NEED_SPECIAL_CHARACTERS`)
  - Le chemin du fichier de sauvegarde (`FILE_PATH`)
  - L’indentation du fichier JSON (`DEFAULT_INDENT`)

## Auteur
ADEBI Châ-Fine Ayédoun achafine@gmail.com
