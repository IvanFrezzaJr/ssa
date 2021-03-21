def init_app(app):
    app.config['SECRET_KEY'] = "0l4rTudoBe1n?"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ssa.db"
    

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True