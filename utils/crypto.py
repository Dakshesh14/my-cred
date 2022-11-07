from django.conf import settings

from cryptography.fernet import Fernet

key = settings.EN_KEY


def encrypt(input: str) -> str:
    """This function returns an encrypted string to be saved in the database."""
    fernet = Fernet(key)
    return fernet.encrypt(input.encode()).decode()


def decrypt(input: str) -> str:
    """This function returns an decrypted string to be saved in the database."""
    fernet = Fernet(key)
    return fernet.decrypt(input.encode()).decode()
