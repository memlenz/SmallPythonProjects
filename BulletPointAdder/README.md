# Bullet Point Adder

## Description
**Bullet Point Adder** est un utilitaire Python qui transforme automatiquement du texte brut en liste à puces. Cet outil récupère le texte depuis le presse-papier, le formate en ajoutant des puces au début de chaque ligne, puis replace le résultat dans le presse-papier pour une utilisation immédiate.

## Fonctionnalités
- Conversion automatique de texte en liste à puces
- Détection et suppression des numéros existants en début de ligne
- Préservation de la structure du texte, y compris les lignes vides
- Configuration personnalisable des symboles de puces

## Compétences Python mises en œuvre

### Manipulation avancée de chaînes de caractères
- Utilisation de `split()`, `strip()` et `join()` pour traiter efficacement le texte
- Formatage de chaînes avec f-strings pour une syntaxe plus lisible

### Expressions régulières
- Implémentation de motifs regex complexes pour détecter et transformer différents formats de liste
- Utilisation de `re.sub()` pour remplacer les motifs identifiés

### Gestion du presse-papier système
- Intégration de la bibliothèque `pyperclip` pour interagir avec le presse-papier
- Opérations de lecture/écriture entre Python et le système d'exploitation

### Programmation modulaire
- Organisation du code en fonctions distinctes avec responsabilités uniques
- Utilisation de docstrings pour documenter chaque fonction

### Configuration flexible
- Implémentation de constantes configurables pour personnaliser le comportement
- Paramétrage des expressions régulières et des symboles de puces

### Gestion des exceptions
- Implémentation de blocs try/except pour gérer les erreurs potentielles
- Feedback utilisateur clair en cas de problème

### Bonnes pratiques de codage
- Respect des conventions PEP 8 pour la lisibilité du code
- Typages des retours de fonction avec les annotations Python 3
- Organisation claire du script avec séparation de la logique métier et du point d'entrée

## Installation et prérequis
1. Python 3.6 ou supérieur
2. Module pyperclip (installation via pip: `pip install pyperclip`)

## Utilisation
1. Copiez votre texte dans le presse-papier
2. Exécutez le script: `python bulletPointAdder.py`
3. Le texte formaté avec des puces est maintenant disponible dans votre presse-papier
4. Collez le résultat où vous le souhaitez

## Personnalisation
Vous pouvez facilement modifier les constantes en tête de script pour changer:
- Le symbole de puce (BULLET): '•', '-', '*', '→', etc.
- Le motif de détection des préfixes (REGEX): adaptez l'expression régulière selon vos besoins

## Auteur
ADEBI Châ-Fine Ayédoun - achafine@gmail.com
