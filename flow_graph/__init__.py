import os

from flask import Flask


def create_app(environ=None, start_response=None, test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'flow_graph.sqlite'),
    )
    app.config.from_object('flow_graph.default_settings')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import graph
    app.register_blueprint(graph.bp)
    app.add_url_rule('/', endpoint='index')

    return app