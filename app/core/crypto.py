from cryptography.fernet import Fernet
from app.core.config import settings


def _get_fernet() -> Fernet:
    return Fernet(settings.FERNET_KEY.encode())


def encrypt_text(text: str) -> str:
    return _get_fernet().encrypt(text.encode()).decode()


def decrypt_text(token: str) -> str:
    return _get_fernet().decrypt(token.encode()).decode()
