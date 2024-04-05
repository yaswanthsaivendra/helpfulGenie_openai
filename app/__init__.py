from flask import Flask
from .main.routes import main_bp

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    # Initialize extensions, database, etc. here if needed

    # Register blueprints
    app.register_blueprint(main_bp)

    return app


