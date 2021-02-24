from flask import render_template
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/saints")
def saints():
    return render_template("saints.html")
