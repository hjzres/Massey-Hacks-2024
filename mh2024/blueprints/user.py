import re

from flask import Blueprint, abort, flash, redirect, render_template, request
from flask_login import login_user

from mh2024 import crud

bp = Blueprint("user", __name__, url_prefix="/user")

username_regex = re.compile(r"^[a-zA-Z0-9_]+$")


@bp.route("/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if username_regex.fullmatch(username) is None:
            flash("Username can only contain alphanumeric characters or underscores!")
            return redirect("/user/create")

        if len(username) > 36:
            flash("Username can't be longer than 36 characters!")
            return redirect("/user/create")

        if crud.get_user_by_username(username) is not None:
            flash("Username already in use!")
            return redirect("/user/create")

        user = crud.create_user(username, password, email)

        login_user(user)
        flash("Logged in!")

    return render_template("user_create.html")


@bp.route("/<username>", methods=["GET", "POST"])
def user_profile(username):
    user = crud.get_user_by_username(username)

    if user is None:
        abort(404)

    return render_template("user_profile.html", user=user)
