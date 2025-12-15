from typing import Any
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from .app_exception import AppException

def generate_error_response(status_code: int, error_code: int, message: str, error: Any = None):
    return JSONResponse(
        status_code=status_code,
        content={
            "status_code": error_code,
            "message": message,
            "error": error
        }
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    return generate_error_response(
        status_code=exc.status_code,
        error_code=exc.status_code,
        message="HTTP Exception",
        error=exc.detail
    )

async def app_exception_handler(request: Request, exc: AppException):
    return generate_error_response(
        status_code=exc.status_code,
        error_code=exc.error_code,
        message=exc.error_message,
        error=exc.error
    )

async def generic_exception_handler(request: Request, exc: Exception):
    return generate_error_response(
        status_code=500,
        error_code=500,
        message="Internal Server Error",
        error=str(exc)
    )

# https://medium.com/@geetansh2k1/the-best-way-to-handle-exceptions-in-a-fastapi-application-37596995355c
def register_exception_handler(app: FastAPI):
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)
