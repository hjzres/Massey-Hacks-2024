from flask import Blueprint, render_template

from mh2024 import crud
from mh2024 import data

bp = Blueprint("plan", __name__, url_prefix="/plan")

@bp.route("/workout/<username>")
def workout(username):
    user = crud.get_user_by_username(username)
    return(render_template("workoutplans.html", user=user))

@bp.route("/workout/<day>/<username>")
def day(day, username):
    user = crud.get_user_by_username(username)
    workouts = data.get_day_info(user.username, day)
    return(render_template("day.html", user=user, day=day, workouts=workouts))

@bp.route("/workout/search")
def workout_search():
    return(render_template("workout-search.html"))