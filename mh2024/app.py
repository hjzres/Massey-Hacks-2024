from os import environ

from flask import Flask

from .auth import login_manager


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = environ["SECRET_KEY"]

    login_manager.init_app(app)

    with app.app_context():
        from .blueprints import auth, user

        app.register_blueprint(auth.bp)
        app.register_blueprint(user.bp)

    return app
