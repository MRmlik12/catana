"""Configuration file"""
import os

POSTGRESQL_CONNECTION_STRING = os.environ.get(
    "POSTGRESQL_CONNECTION_STRING", "postgresql://test:123@localhost:5432/catana_db"
)
REDIS_CONNECTION_STRING = os.environ.get(
    "REDIS_CONNECTION_STRING", "redis://localhost:6379"
)
JWT_SECRET_KEY = os.environ.get(
    "JWT_SECRET_KEY",
    "OPdNtRVFv/lJ+sPQyvy/UDoPe4w3cE4Ld8DKWXK1hLGOoKzfyWkDVdqmwuGT2dbwyrSp5i9HOifgoKpRDpV5kg==",
)
EMAIL_HOST = os.environ.get("EMAIL_HOST", "0.0.0.0")
EMIAL_HOST_PORT = os.environ.get("EMAIL_HOST_PORT", "433")
EMAIL = os.environ.get("EMAIL", "example@example.com")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "")
DEBUG = os.environ.get("DEBUG", True)
