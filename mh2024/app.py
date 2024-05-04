from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def home():
        return render_template("home.html")

    return app

