from fastapi import APIRouter, Depends, HTTPException
from .controller import HealtyController
from .schemas import HealtyResponse
from app.tools import bearer_auth, HTTPAuthorizationCredentials, decode_access_token


class HealtyRouter(APIRouter):
    
    __controller: HealtyController
    
    def __init__(self):
        super().__init__()
        
        self.__controller = HealtyController()
        
        self.add_api_route(
            '/healty', 
            self.healty, 
            methods=['GET'], 
            response_model=HealtyResponse, 
            status_code=200,
            dependencies=[Depends(bearer_auth)],
            responses={
                409: {'description': 'Auth error (token expired, invalid token)', 'model': HTTPException},
            },
            description='Valid the state of the thirt api service and the connection with the DB'
        )


    async def healty(self, credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)) -> HealtyResponse:
        token_info = decode_access_token(credentials=credentials)
        return HealtyResponse(
            db=self.__controller.check_db_healty(),
            breed_api=self.__controller.check_breed_api_healty()
        )


healtyRouter = HealtyRouter()