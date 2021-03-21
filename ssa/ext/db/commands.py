from ssa.ext.db import db
from ssa.ext.db import models  # noqa

def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()
