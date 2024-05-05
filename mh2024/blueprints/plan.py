from flask import Blueprint, render_template

from mh2024 import crud

bp = Blueprint("plan", __name__, url_prefix="/plan")

@bp.route("/workout/<username>")
def workout(username):
    user = crud.get_user_by_username(username)
    return(render_template("workoutplans.html", user=user))

@bp.route("/workout/<day>/<username>")
def workout_create(day, username):
    user = crud.get_user_by_username(username)
    return(render_template("workout-create.html", user=user, day=day))

@bp.route("/workout/search")
def workout_search():
    return(render_template("workout-search.html"))