from fastapi import APIRouter, Depends
from .controller import HealtyController
from .schemas import HealtyResponse
from app.tools.auth import bearer_auth, HTTPAuthorizationCredentials, decode_access_token


class HealtyRouter(APIRouter):
    
    __controller: HealtyController
    
    def __init__(self):
        super().__init__()
        
        self.__controller = HealtyController()
        
        self.add_api_route('/healty', self.healty, methods=['GET'], response_model=HealtyResponse, dependencies=[Depends(bearer_auth)])


    async def healty(self, credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)) -> HealtyResponse:
        token_info = decode_access_token(credentials=credentials)
        return HealtyResponse(
            db=self.__controller.check_db_healty(),
            breed_api=self.__controller.check_breed_api_healty()
        )


healtyRouter = HealtyRouter()