import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  """Base configuration"""
  pass

class ProductionConfig(Config):
  """Production configuration"""
  pass


class DevelopmentConfig(Config):
  """Development configuration"""
  pass

class TestingConfig(Config):
  """Testing configuration"""
  TESTING = True