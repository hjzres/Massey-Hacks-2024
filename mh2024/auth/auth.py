from passlib.context import CryptContext

pw_ctx = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(pw: str) -> str:
    return pw_ctx.hash(pw)
