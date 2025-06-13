# TP Séance 1 - Tests Unitaires

Ce projet est un exercice pratique sur les tests unitaires en Python. Il contient plusieurs modules avec leurs tests correspondants pour illustrer les bonnes pratiques de développement piloté par les tests (TDD).

## Structure du projet

```
tp_seance1_unit_tests/
├── src/                    # Code source
│   ├── __init__.py
│   ├── calculator.py       # Fonctions de calcul mathématique
│   ├── validator.py        # Fonctions de validation (email, mot de passe)
│   └── string_utils.py     # Utilitaires de manipulation de chaînes
├── tests/                  # Tests unitaires
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_validator.py
│   └── test_string_utils.py
├── venv_tests/            # Environnement virtuel Python
├── .gitignore
└── README.md
```

## Modules disponibles

### 📊 Calculator (`src/calculator.py`)

Module contenant des fonctions de calcul mathématique avec gestion d'erreurs :

- **`add(a, b)`** : Addition de deux nombres
- **`divide(a, b)`** : Division avec gestion de la division par zéro
- **`power(base, exponent)`** : Calcul de puissance avec gestion des cas limites

### ✅ Validator (`src/validator.py`)

Module de validation avec expressions régulières :

- **`is_valid_email(email)`** : Validation d'adresses email
- **`validate_password_strength(password)`** : Évaluation de la force d'un mot de passe

### 🔤 String Utils (`src/string_utils.py`)

Utilitaires de manipulation de chaînes de caractères :

- **`capitalize_words(text)`** : Met en majuscule la première lettre de chaque mot
- **`count_words(text)`** : Compte le nombre de mots dans un texte
- **`remove_vowels(text)`** : Supprime toutes les voyelles d'un texte

## Installation et configuration

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

1. Clonez le repository :
```bash
git clone <url-du-repository>
cd tp_seance1_unit_tests
```

2. Créez et activez l'environnement virtuel :
```bash
python -m venv venv_tests
source venv_tests/bin/activate  # Sur Linux/Mac
# ou
venv_tests\Scripts\activate     # Sur Windows
```

3. Installez les dépendances (si nécessaire) :
```bash
pip install pytest  # Pour les tests plus avancés (optionnel)
```

## Exécution des tests

### Avec unittest (module standard Python)

Exécuter tous les tests :
```bash
python -m unittest discover tests/
```

Exécuter un module de test spécifique :
```bash
python -m unittest tests.test_calculator
python -m unittest tests.test_validator
python -m unittest tests.test_string_utils
```

Exécuter un test spécifique :
```bash
python -m unittest tests.test_calculator.TestCalculator.test_add_valid_numbers
```

### Avec pytest (optionnel)

Si vous avez installé pytest :
```bash
pytest tests/
pytest tests/test_calculator.py -v
```

## Exemples d'utilisation

### Calculator

```python
from src.calculator import add, divide, power

# Addition
result = add(5, 3)  # 8

# Division
result = divide(10, 2)  # 5.0

# Puissance
result = power(2, 3)  # 8
```

### Validator

```python
from src.validator import is_valid_email, validate_password_strength

# Validation email
is_valid = is_valid_email("user@example.com")  # True

# Validation mot de passe
strength = validate_password_strength("MyP@ssw0rd")
# {'is_valid': True, 'score': 5, 'missing_criteria': []}
```

### String Utils

```python
from src.string_utils import capitalize_words, count_words, remove_vowels

# Capitalisation
text = capitalize_words("hello world")  # "Hello World"

# Comptage de mots
count = count_words("Hello world")  # 2

# Suppression des voyelles
text = remove_vowels("Hello World")  # "Hll Wrld"
```

## Fonctionnalités des tests

Les tests couvrent :

- ✅ **Cas nominaux** : Fonctionnement normal des fonctions
- ✅ **Gestion d'erreurs** : Validation des exceptions levées
- ✅ **Cas limites** : Division par zéro, chaînes vides, etc.
- ✅ **Validation de types** : Vérification des types d'arguments
- ✅ **Tests de régression** : Prévention des régressions

## Objectifs pédagogiques

Ce projet illustre :

1. **Test-Driven Development (TDD)** : Écriture des tests avant le code
2. **Couverture de tests** : Tests exhaustifs des fonctionnalités
3. **Gestion d'exceptions** : Tests des cas d'erreur
4. **Organisation du code** : Séparation claire entre code source et tests
5. **Documentation** : Docstrings et commentaires explicatifs

## Contribution

Pour contribuer au projet :

1. Forkez le repository
2. Créez une branche pour votre fonctionnalité
3. Écrivez les tests pour votre nouvelle fonctionnalité
4. Implémentez la fonctionnalité
5. Vérifiez que tous les tests passent
6. Soumettez une pull request

## Licence

Ce projet est à des fins éducatives dans le cadre d'un TP sur les tests unitaires.