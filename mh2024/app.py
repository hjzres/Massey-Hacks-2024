from os import environ

from flask import Flask, render_template

from .auth import login_manager

import pathlib
from . import data

data_folder = pathlib.Path("./data/")
data_folder.mkdir(exist_ok=True, parents=True)
if not (data_folder / "cache.json").is_file():
    data.post_file({})

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def home():
        return render_template("home.html")

    app.config["SECRET_KEY"] = environ["SECRET_KEY"]

    login_manager.init_app(app)

    with app.app_context():
        from .blueprints import auth, user, plan

        app.register_blueprint(auth.bp)
        app.register_blueprint(user.bp)
        app.register_blueprint(plan.bp)

    return app
