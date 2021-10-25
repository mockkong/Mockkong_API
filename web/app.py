from flask import Flask


def create_app(config_object="web.settings"):
    """Create application factory
    :param config_object: Thr configuration object to use"""
