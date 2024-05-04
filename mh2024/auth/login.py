from flask_login import LoginManager

from mh2024 import crud

from .auth import pw_ctx

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str) -> crud.User | None:
    return crud.get_user_by_uuid(user_id)


def authenticate_user(user: crud.User, password: str) -> bool:
    verified, replacement_hash = pw_ctx.verify_and_update(password, user.password_hash)
    if verified:
        if replacement_hash:
            crud.update_user_password_hash(user, replacement_hash)
        return True
    return False
