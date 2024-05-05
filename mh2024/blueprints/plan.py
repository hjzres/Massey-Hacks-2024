from flask import Blueprint, render_template, request

from mh2024 import crud
from mh2024 import data

bp = Blueprint("plan", __name__, url_prefix="/plan")

@bp.route("/workout/<username>")
def workout(username):
    user = crud.get_user_by_username(username)
    return(render_template("workoutplans.html", user=user))

@bp.route("/workout/<day>/<username>", methods=["GET", "POST"])
def day(day, username):
    user = crud.get_user_by_username(username)
    workouts = data.get_day_info(username, day)
    if request.method == "POST":
        if request.form.get('_method') == 'DELETE':
            data.reset_day(user.username, day)
        else:
            workout = request.form["workout"]
            sets = [request.form["set1"], request.form["set2"], request.form["set3"]]
            data.add_workout(user.username, day, workout, sets)
    return(render_template("day.html", user=user, day=day, workouts=workouts))

@bp.route("/workout/search")
def workout_search():
    return(render_template("workout-search.html"))

@bp.route("/workout/search/<username>")
def workout_searched(username):
    user = crud.get_user_by_username(username)
    return(render_template("workoutplans.html", user=user))