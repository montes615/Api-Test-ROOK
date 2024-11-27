from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from datetime import datetime
from app.logs import server_request_log
from typing import Tuple


class ServerRequestLog(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.now()

        method, url, client_host = await self.__set_init_log(start_time=start_time, request=request)

        response = await call_next(request)

        new_response = await self.__set_end_log(start_time=start_time, method=method, url=url, client_host=client_host, response=response)

        return new_response
    

    async def __set_init_log(self, start_time: datetime, request: Request) -> Tuple[str, str, int]:
        method = request.method
        url = str(request.url)
        client_host = request.client.host

        body_bytes = await request.body()
        body = body_bytes.decode("utf-8") if body_bytes else "Empty"
        
        server_request_log.info(
            f'{start_time.isoformat()} - {client_host} Start: {method} {url} '
            f'{body}'
        )

        return method, url, client_host
    

    async def __set_end_log(self, start_time: datetime, method: str, url: str, client_host: str, response: Response) -> Response:
        response_body = b''.join([chunk async for chunk in response.body_iterator])
        new_response = Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
        end_time = datetime.now()
        process_time = (end_time - start_time).total_seconds()

        server_request_log.info(
            f'{end_time.isoformat()} - {client_host} End: {method} {url} - {response.status_code} - Time: {process_time:.2f}s - '
            f'Response: {response_body.decode('utf-8') if response_body else 'Empty'}'
        )

        return new_response

