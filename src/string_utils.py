def capitalize_words(text):
    """Met en majuscule la première lettre de chaque mot."""
    if not isinstance(text, str):
        raise TypeError("L'argument doit être une chaîne")
    return text.title()

def count_words(text):
    """Compte le nombre de mots."""
    if not isinstance(text, str):
        raise TypeError("L'argument doit être une chaîne")
    if not text.strip():
        return 0
    return len(text.split())

def remove_vowels(text):
    """Supprime toutes les voyelles."""
    if not isinstance(text, str):
        raise TypeError("L'argument doit être une chaîne")
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)