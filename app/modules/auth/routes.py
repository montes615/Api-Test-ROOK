from fastapi import APIRouter, HTTPException
from .controller import AuthController
from .schemas import RegisterUser, LoginUser, TokenResponse, TokenData


class AuthRouter(APIRouter):

    __controller: AuthController

    def __init__(self):
        super().__init__()
        
        self.__controller = AuthController()
        
        self.add_api_route(
            '/login', 
            self.login, methods=['POST'], 
            response_model=TokenResponse,
            status_code=200,
            responses={
                409: {'description': 'Invalid username or pasword', 'model': HTTPException}
            },
            description='Users with account can use this endpoint for get an api token'
        )
        self.add_api_route(
            '/register', 
            self.register, 
            methods=['POST'], 
            response_model=TokenResponse,
            status_code=201,
            responses={
                409: {'description': 'The username alredy exists', 'model': HTTPException}
            },
            description='Users without account can use this endpoint for register and get an api token'
        )


    async def register(self, registerUser: RegisterUser) -> TokenResponse:
        '''Endpoint to register users'''
        user = self.__controller.register_user(registerUser=registerUser)
        return self.__controller.create_access_token(TokenData(**user.model_dump()))


    async def login(self, loginUser: LoginUser) -> TokenResponse:
        '''Valid if the user are register'''
        user = self.__controller.valid_user(loginUser=loginUser)
        return self.__controller.create_access_token(TokenData(**user.model_dump()))


authRouter = AuthRouter()