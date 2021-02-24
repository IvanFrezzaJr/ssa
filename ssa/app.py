from flask import Flask
from ssa.ext import site
from ssa.ext import toolbar
from ssa.ext import config

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app

