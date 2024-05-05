from uuid import uuid4

from flask_login import UserMixin

from mh2024 import auth

import sqlite3

from dataclasses import dataclass

from .database import get_db


@dataclass
class User(UserMixin):
    uuid: str
    username: str
    password_hash: str
    email: str

    def get_id(self) -> str:
        return self.uuid


def create_user(username: str, password: str, email: str) -> User:
    uuid = str(uuid4())
    password_hash = auth.hash_password(password)
    row_data = (uuid, username, password_hash, email)
    cursor = get_db().cursor()
    cursor.execute("""
        INSERT INTO Users (UserId, Username, PasswordHash, Email) VALUES
            (?, ?, ?, ?)
    """, row_data)
    get_db().commit()
    return User(uuid, username, password_hash, email)


def get_user_by_uuid(uuid: str) -> User | None:
    cursor = get_db().cursor()
    user = cursor.execute("""
        SELECT 
            Username,
            PasswordHash,
            Email
        FROM
            Users
        WHERE
            UserId = ?
    """, (uuid,)).fetchone()
    if user is None:
        return None
    username, password_hash, email = user
    return User(uuid, username, password_hash, email)
    


def get_user_by_username(username: str) -> User | None:
    cursor = get_db().cursor()
    user = cursor.execute("""
        SELECT
            UserId,
            PasswordHash,
            Email
        FROM
            Users
        WHERE
            Username = ?
    """, (username,)).fetchone()
    if user is None:
        return None
    uuid, password_hash, email = user
    return User(uuid, username, password_hash, email)
    


def update_user_password_hash(user: User, password_hash: str) -> None:
    user.password_hash = password_hash
    cursor = get_db().cursor()
    cursor.execute("""
        UPDATE 
            Users
        SET
            PasswordHash = ?
        WHERE
            UserId = ?
    """, (password_hash, user.uuid))
    get_db().commit()
