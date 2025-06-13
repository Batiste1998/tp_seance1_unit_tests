import pytest
from src.validator import is_valid_email, validate_password_strength

class TestEmailValidation:
    def test_emails_valides(self):
        valides = ["user@example.com", "test.email@domain.org"]
        for email in valides:
            assert is_valid_email(email) == True

    def test_emails_invalides(self):
        invalides = ["user", "user@", "@domain.com", "user@domain", "user@domain.", "user@.com", "user@domain.c"]
        for email in invalides:
            assert is_valid_email(email) == False
    
    def test_emails_invalides_caracteres_speciaux(self):
        # Test pour couvrir la ligne 22 - caractères invalides dans la partie locale
        invalides_locaux = ["user@#@domain.com", "user space@domain.com", "user+@domain.com"]
        for email in invalides_locaux:
            assert is_valid_email(email) == False

    def test_type_invalide(self):
        with pytest.raises(TypeError):
            is_valid_email(123)

class TestPasswordStrength:
    def test_password_fort(self):
        result = validate_password_strength("MyStrong123!")
        assert result['is_valid'] == True
        assert result['score'] >= 4

    def test_password_faible(self):
        result = validate_password_strength("weak")
        assert result['is_valid'] == False
        assert len(result['missing_criteria']) > 0
    
    def test_password_type_invalide(self):
        with pytest.raises(TypeError):
            validate_password_strength(123)