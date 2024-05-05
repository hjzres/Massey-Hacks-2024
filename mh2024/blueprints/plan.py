from flask import Blueprint

from mh2024 import crud

bp = Blueprint("user", __name__, url_prefix="/user")

bp.route("/workout")
def workout():
    pass