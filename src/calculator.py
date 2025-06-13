def add(a, b):
    """
    Additionne deux nombres.

    Raises:
    TypeError: Si un argument n'est pas un nombre
    """
    # Valider les types avec isinstance(a, (int, float))
    if not isinstance(a, (int, float)):
        raise TypeError(f"Le premier argument doit être un nombre, reçu {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Le second argument doit être un nombre, reçu {type(b).__name__}")
    
    # Retourner a + b
    return a + b

def divide(a, b):
    """
    Divise a par b.

    Returns:
    float: Quotient (toujours en float)

    Raises:
    TypeError: Si un argument n'est pas un nombre
    ZeroDivisionError: Si b est égal à 0
    """
    # Valider les types
    if not isinstance(a, (int, float)):
        raise TypeError(f"Le premier argument doit être un nombre, reçu {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Le second argument doit être un nombre, reçu {type(b).__name__}")
    
    # Vérifier b != 0, lever ZeroDivisionError
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    
    # Retourner float(a / b)
    return float(a / b)

def power(base, exponent):
    """
    Calcule base^exponent.

    Raises:
    ValueError: Si base=0 et exponent<0
    """
    # Valider les types
    if not isinstance(base, (int, float)):
        raise TypeError(f"La base doit être un nombre, reçu {type(base).__name__}")
    if not isinstance(exponent, (int, float)):
        raise TypeError(f"L'exposant doit être un nombre, reçu {type(exponent).__name__}")
    
    # Gérer cas 0^(négatif) -> ValueError
    if base == 0 and exponent < 0:
        raise ValueError("0 ne peut pas être élevé à une puissance négative")
    
    # Retourner base ** exponent
    return base ** exponent