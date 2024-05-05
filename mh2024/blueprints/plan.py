from flask import Blueprint, render_template

from mh2024 import crud

bp = Blueprint("plan", __name__, url_prefix="/plan")

@bp.route("/workout")
def workout():
    return(render_template("workoutplans.html"))

@bp.route("/workout/create")
def workout_create():
    return(render_template("workout-create.html"))

@bp.route("/workout/search")
def workout_search():
    return(render_template("workout-search.html"))