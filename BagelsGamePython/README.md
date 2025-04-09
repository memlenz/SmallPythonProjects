# Bagels - Jeu de déduction logique

## Description
**Bagels** est un jeu de déduction logique en Python où le joueur doit deviner un nombre secret à trois chiffres. Le programme fournit des indices après chaque tentative pour guider le joueur vers la solution. C'est un excellent exemple de jeu simple mais engageant qui démontre plusieurs concepts fondamentaux de programmation.

## Fonctionnalités
- Génération aléatoire d'un nombre secret à trois chiffres
- Système d'indices pour guider le joueur (Pico, Fermi, Bagels)
- Validation des entrées utilisateur
- 10 tentatives pour trouver le nombre correct
- Option pour rejouer une partie

## Règles du jeu
- Le programme génère un nombre secret à trois chiffres
- Vous avez 10 chances pour deviner ce nombre
- Après chaque tentative, vous recevez un indice:
  - **Pico**: Un chiffre est correct mais à la mauvaise position
  - **Fermi**: Un chiffre est correct et à la bonne position
  - **Bagels**: Aucun chiffre n'est correct

## Compétences Python mises en œuvre

### Programmation procédurale
- Organisation du code en fonctions bien définies avec des responsabilités spécifiques
- Utilisation d'une fonction `main()` comme point d'entrée principal du programme

### Structures de contrôle avancées
- Utilisation de boucles imbriquées pour gérer le flux du jeu et les saisies utilisateur
- Utilisation de la structure `for/else` pour détecter la fin des tentatives
- Implémentation de la validation d'entrée avec boucles `while` conditionnelles

### Manipulation de listes et chaînes de caractères
- Conversion entre types numériques et chaînes de caractères
- Manipulation de listes pour générer et vérifier les nombres
- Utilisation de méthodes de chaînes comme `strip()`, `isdigit()` et `lower()`

### Génération de nombres aléatoires
- Utilisation du module `random` pour générer des nombres aléatoires
- Implémentation de l'algorithme Fisher-Yates (via `random.shuffle()`) pour mélanger une liste

### Logique conditionnelle
- Conception d'un algorithme de comparaison pour générer les indices appropriés
- Utilisation de structures if/elif/else pour gérer différentes conditions de jeu

### Interface utilisateur en console
- Création d'une interface textuelle interactive et conviviale
- Affichage clair des instructions et des retours d'information

### Documentation et lisibilité
- Utilisation de docstrings pour documenter chaque fonction
- En-tête de script détaillé expliquant le but et les règles du jeu
- Commentaires explicatifs pour faciliter la compréhension du code

### Bonnes pratiques de développement
- Utilisation de constantes pour les paramètres configurables du jeu
- Séparation claire de la logique métier et de l'interface utilisateur
- Respect des conventions de nommage Python (PEP 8)

## Installation et prérequis
- Python 3.6 ou supérieur
- Aucune bibliothèque externe requise

## Utilisation
1. Exécutez le script: `python bagels.py`
2. Lisez les instructions qui s'affichent à l'écran
3. Entrez un nombre à trois chiffres à chaque tentative
4. Utilisez les indices pour affiner vos prochaines tentatives
5. Choisissez de rejouer ou non à la fin de chaque partie

## Personnalisation
Vous pouvez modifier les constantes en haut du script pour:
- Changer le nombre de tentatives disponibles (GUESSES)
- Modifier la longueur du nombre secret (DIGIT_LEN)

## Auteur
ADEBI Ayedoun Châ-Fine - achafine@gmail.com
