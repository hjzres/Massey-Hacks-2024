from uuid import uuid4

from flask_login import UserMixin

from mh2024 import auth

db = {
    "1": {"username": "noah", "password_hash": "password"},
    "2": {"username": "bell", "password_hash": "password2"},
    "3": {"username": "Andrei", "password_hash": "password3"},
}


class User(UserMixin):
    uuid: str
    username: str
    password_hash: str

    def __init__(self, uuid: str, username: str, password_hash: str):
        self.uuid = uuid
        self.username = username
        self.password_hash = password_hash

    def get_id(self) -> str:
        return self.uuid


def create_user(username: str, password: str) -> User:
    uuid = str(uuid4())
    password_hash = auth.hash_password(password)
    db[uuid] = {"username": username, "password_hash": password_hash}
    return User(uuid, username, password)


def get_user_by_uuid(uuid: str) -> User | None:
    try:
        user = db[uuid]
        return User(uuid, user["username"], user["password_hash"])
    except KeyError:
        return None


def get_user_by_username(username: str) -> User | None:
    for uuid, user in db.items():
        if user["username"] == username:
            return User(uuid, user["username"], user["password_hash"])
    return None


def update_user_password_hash(user: User, password_hash: str) -> None:
    user.password_hash = password_hash
    db[user.uuid]["password_hash"] = password_hash
