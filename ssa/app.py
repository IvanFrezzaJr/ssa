from flask import Flask
from ssa.ext import site
from ssa.ext import toolbar
from ssa.ext import config
from ssa.ext import db
from ssa.ext import cli

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app

