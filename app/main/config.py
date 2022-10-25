import os
from dotenv import load_dotenv

load_dotenv()

"""
the importance of a venv is that we do not want to be passing
some important details into our application as it could  get leaked
With the env variable you can actually hide these secrets and
And anytime our app  need to read it, it reads it  from
our  env variable
Never push ur env variable to git hub or any CI/CD pipeline.

Here we create env variables that we will
use to connect to the database we will be creating.

Postgres  sql db
"""

postgres_local_base = os.getenv("DATABASE_URI")
db_name = os.getenv("RDS_DB_NAME", None)
rds_username = os.getenv("RDS_USERNAME", None)
rds_password = os.getenv("RDS_PASSWORD", None)
rds_port = os.getenv("RDS_PORT", None)
rds_host_name = os.getenv("RDS_HOSTNAME", None)
basedir = os.path.abspath(os.path.dirname(__file__))

prod_database_uri = f"postgresql://{rds_username}:{rds_password}@{rds_host_name}:{rds_port}/{db_name}"


# for our case we will be using sql lite 3. A light weight database.


# we will be creating our main config class
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', "hjlskklddlkklfkdldfkakkla")
    DEBUG = False
    ERROR_PATH = os.getenv('ERROR_PATH', None)


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'database.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment this line below to use postgres
    SQLALCHEMY_DATABASE_URI = prod_database_uri


config_by_name = dict(
    development=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
    )


SECRET_KEY = Config.SECRET_KEY
SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
