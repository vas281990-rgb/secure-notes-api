import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

FERNET_KEY = os.getenv("FERNET_KEY")
ENV_PATH = ".env"


def _generate_key() -> str:
    return Fernet.generate_key().decode()


def _save_key_to_env(key: str):
    with open(ENV_PATH, "a") as f:
        f.write(f"\nFERNET_KEY={key}")


def _get_fernet() -> Fernet:
    global FERNET_KEY

    if not FERNET_KEY:
        FERNET_KEY = _generate_key()
        _save_key_to_env(FERNET_KEY)

    return Fernet(FERNET_KEY.encode())


def encrypt_text(text: str) -> str:
    fernet = _get_fernet()
    return fernet.encrypt(text.encode()).decode()


def decrypt_text(token: str) -> str:
    fernet = _get_fernet()
    return fernet.decrypt(token.encode()).decode()