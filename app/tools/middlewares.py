from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from datetime import datetime
from app.logs import server_request_log
from typing import Tuple


class ServerRequestLog(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        '''
        Middleware for implement log messages in all endpoins

        ### Params
            request (Request): Request object
            call_next (RequestResponseEndpoint): Calls the next step of the request
        '''
        start_time = datetime.now()
        
        method, url, client_host = await self.__set_init_log(start_time=start_time, request=request)

        response = await call_next(request)

        new_response = await self.__set_end_log(start_time=start_time, method=method, url=url, client_host=client_host, response=response)

        return new_response
    

    async def __set_init_log(self, start_time: datetime, request: Request) -> Tuple[str, str, int]:
        '''
        Set the init request log

        ### Params
            start_time (datetime): Init time of the request
            request (Request): Request object
        '''
        method = request.method
        url = str(request.url)
        client_host = request.client.host

        body_bytes = await request.body()
        body = body_bytes.decode('utf-8') if body_bytes else 'Empty'
        
        server_request_log.info(
            f'{client_host} Start: {method} {url} '
            f'REQUEST: {body}'
        )

        return method, url, client_host
    

    async def __set_end_log(self, start_time: datetime, method: str, url: str, client_host: str, response: Response) -> Response:
        '''
        Set the request end log

        ### Params
            start_time (datetime): Init time of the request
            method (str): Request method
            url (str): Request url
            client_host (str): Request client host
            response (Response): Response object
        '''
        response_body = b''.join([chunk async for chunk in response.body_iterator])
        new_response = Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
        end_time = datetime.now()
        process_time = (end_time - start_time).total_seconds()

        if response.status_code >= 400:
            server_request_log.error(
                f"{client_host} End: {method} {url} - {response.status_code} - Time: {process_time:.2f}s - "
                f"Response: {response_body.decode('utf-8') if response_body else 'Empty'}"
            )
        else:
            server_request_log.info(
                f"{client_host} End: {method} {url} - {response.status_code} - Time: {process_time:.2f}s - "
                f"RESPOSNSE: {response_body.decode('utf-8') if response_body else 'Empty'}"
            )

        return new_response

