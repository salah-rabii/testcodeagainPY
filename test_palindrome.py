# test_palindrome.py
import pytest
from palindrome import palindrome

@pytest.mark.parametrize("mot, attendu", [
    ("radar", True),
    ("kayak", True),
    ("Aba", True),  # Doit être un palindrome car insensible à la casse
    ("hello", False),
    (" ", True),  # Une chaîne vide ou un seul caractère est un palindrome
    ("race car", True),  # Doit être un palindrome car insensible aux espaces 
    ("palindrome", False),
    ("test",False),
    ("solyaman",False)
])

def test_palindrome(mot, attendu):

    resultat = palindrome(mot)
    assert resultat == attendu

    

