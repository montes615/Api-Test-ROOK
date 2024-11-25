from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

# HTTPException management
async def http_exception_handler(request: Request, exc: HTTPException):
    'Catch a HTTP exceptions'
    return JSONResponse(
        status_code=exc.status_code,
        content={'message': exc.detail, 'headers': exc.headers},
    )


# General exception management
async def global_exception_handler(request: Request, exc: Exception):
    'Catch a global exceptions'
    return JSONResponse(
        status_code=500,
        content={'message': 'Unexpected Error', 'detail': str(exc), 'exception_type': type(exc).__name__},
    )
