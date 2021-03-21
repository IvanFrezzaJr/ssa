from ssa.ext.db.commands import create_db, drop_db
from ssa.ext.auth.commands import add_user

def init_app(app):
    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command()(drop_db))
    app.cli.add_command(app.cli.command()(add_user))