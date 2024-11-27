from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.logs import server_request_log
from datetime import datetime

async def http_exception_handler(request: Request, exc: HTTPException):
    'Catch a HTTP exceptions'
    set_error_log(request=request, exc=exc)

    return JSONResponse(
        status_code=exc.status_code,
        content={'message': exc.detail, 'headers': exc.headers},
    )


async def global_exception_handler(request: Request, exc: Exception):
    set_error_log(request=request, exc=exc)

    return JSONResponse(
        status_code=500,
        content={'message': 'Unexpected Error', 'detail': str(exc), 'exception_type': type(exc).__name__},
    )


def set_error_log(request: Request, exc: Exception) -> None:
    server_request_log.error(
        f'{datetime.now().isoformat()} - Request Error: {request.method} {request.url} - '
        f'Status: {exc.status_code} - Details: {exc.detail}'
    )