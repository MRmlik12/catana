import os

from starlette import config
from starlette.config import Config

conf = Config(".env")
POSTGRESQL_CONNECTION_STRING = os.getenv("POSTGRESQL_CONNECTION_STRING")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
