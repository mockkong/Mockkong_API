from flask import Flask


def create_app(config_object="web.settings"):
    """Create application factory
    :param config_object: Thr configuration object to use"""
    print(__name__.split(".")[0])
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    return app
