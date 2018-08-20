class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    
}
