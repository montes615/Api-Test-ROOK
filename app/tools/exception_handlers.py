from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.logs import server_request_log
from datetime import datetime

async def http_exception_handler(request: Request, exc: HTTPException):
    '''
    Catch a HTTP exceptions

    ### Params
        request (Request): Request object
        exc (HTTPException): HTTP exception
    '''
    return JSONResponse(
        status_code=exc.status_code,
        content={'message': exc.detail, 'headers': exc.headers},
    )


async def global_exception_handler(request: Request, exc: Exception):
    '''
    Catch a general exceptions

    ### Params
        request (Request): Request object
        exc (HTTPException): HTTP exception
    '''
    return JSONResponse(
        status_code=500,
        content={'message': 'Unexpected Error', 'detail': str(exc), 'exception_type': type(exc).__name__},
    )
