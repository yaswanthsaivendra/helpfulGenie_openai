from .config import Config


class ProductionConfig(Config):
    DEBUG = False
    # Add production-specific configuration options here
