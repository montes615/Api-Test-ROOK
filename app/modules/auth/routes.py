from fastapi import APIRouter
from fastapi.responses import JSONResponse

class AuthRouter(APIRouter):

    def __init__(self):
        super().__init__()
        
        self.add_api_route('/login', self.login, methods=['POST'])


    async def login(self):
        return JSONResponse(content={'message': 'Hello World'}, status_code=200)


authRouter = AuthRouter()