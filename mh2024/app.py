from os import environ

from flask import Flask, g

from .auth import login_manager


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = environ["SECRET_KEY"]

    login_manager.init_app(app)

    with app.app_context():
        from .blueprints import auth, user

        app.register_blueprint(auth.bp)
        app.register_blueprint(user.bp)

        @app.teardown_appcontext
        def close_connection(exception):
            db = getattr(g, '_database', None)
            if db is not None:
                db.close()


    return app
