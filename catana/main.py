"""Main module"""
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware

from catana.api.api import router
from catana.api.errors.error import http_error_handler
from catana.core.config import POSTGRESQL_CONNECTION_STRING, DEBUG


def get_app() -> FastAPI:
    """Initialize FastAPI modules and return initialized modules"""
    app_init = FastAPI(title="Catana", debug=bool(DEBUG), version="1")
    app_init.include_router(router, prefix="/api")

    app_init.add_exception_handler(HTTPException, http_error_handler)
    app_init.add_middleware(DBSessionMiddleware, db_url=POSTGRESQL_CONNECTION_STRING)

    return app_init


app = get_app()
