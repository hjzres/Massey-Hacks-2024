from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_required, login_user, logout_user

from mh2024 import crud

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        remember = bool(request.form.get("remember", ""))

        u = crud.get_user_by_username(username)

        if u is None:
            flash("User does not exist!")
            return redirect("/auth/login")

        if password != u.password_hash:
            flash("Password incorrect!")
            return redirect("/auth/login")

        login_user(u, remember)
        flash("Logged in!")

    return render_template("login.html")


@bp.route("/logout")
@login_required
def user_logout():
    logout_user()
    flash("Logged out!")
    return redirect("/auth/login")
