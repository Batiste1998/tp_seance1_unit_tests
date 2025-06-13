import re

def is_valid_email(email):
    """Valide une adresse email."""
    if not isinstance(email, str):
        raise TypeError("L'email doit être une chaîne")

    # Vérifier qu'il y a exactement un @
    if email.count('@') != 1:
        return False
    
    # Séparer en partie locale et domaine
    local_part, domain_part = email.split('@')
    
    # Vérifier que les parties ne sont pas vides
    if not local_part or not domain_part:
        return False
    
    # Valider partie locale (regex: ^[a-zA-Z0-9._-]+$)
    local_pattern = r'^[a-zA-Z0-9._-]+$'
    if not re.match(local_pattern, local_part):
        return False
    
    # Valider domaine (regex: ^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$)
    domain_pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if not re.match(domain_pattern, domain_part):
        return False
    
    return True

def validate_password_strength(password):
    """Évalue la force d'un mot de passe."""
    if not isinstance(password, str):
        raise TypeError("Le mot de passe doit être une chaîne")

    result = {
        'is_valid': False,
        'score': 0,
        'missing_criteria': []
    }

    # Critères de validation du mot de passe
    criteria = [
        ('Au moins 8 caractères', len(password) >= 8),
        ('Au moins une minuscule', re.search(r'[a-z]', password) is not None),
        ('Au moins une majuscule', re.search(r'[A-Z]', password) is not None),
        ('Au moins un chiffre', re.search(r'\d', password) is not None),
        ('Au moins un caractère spécial', re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None)
    ]
    
    # Vérifier chaque critère et incrémenter score
    for criterion_name, is_met in criteria:
        if is_met:
            result['score'] += 1
        else:
            result['missing_criteria'].append(criterion_name)
    
    # is_valid = True si score >= 4
    result['is_valid'] = result['score'] >= 4

    return result