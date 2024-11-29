from fastapi import APIRouter, Depends, HTTPException
from .controller import DogsController
from app.tools import bearer_auth, decode_access_token, HTTPAuthorizationCredentials
from .schemas import BreedResponse, StatsResponse


class DogsRouter(APIRouter):
    
    __controller: DogsController
    
    def __init__(self):
        super().__init__()
        
        self.__controller = DogsController()
        
        self.add_api_route(
            '/dog/breed/{breed_name}', 
            self.breed, 
            methods=['GET'], 
            response_model=BreedResponse,
            status_code=200,
            dependencies=[Depends(bearer_auth)],
            responses={
                409: {'description': 'Auth error (token expired, invalid token)', 'model': HTTPException},
                404: {'description': 'The requested breed do not exists in the api service', 'model': HTTPException},
                503: {'description': 'Third party service are unavailable', 'model': HTTPException}
            },
            description='Can you get an image for the requested breed'
        )
        self.add_api_route(
            '/stats', 
            self.stats, 
            methods=['GET'], 
            response_model=StatsResponse,
            status_code=200,
            dependencies=[Depends(bearer_auth)],
            responses={
                409: {'description': 'Auth error (token expired, invalid token)', 'model': HTTPException},
            },
            description='Gets the 10 most requested breeds'
        )
        
        
    async def breed(self, breed_name: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)) -> BreedResponse:
        token_info = decode_access_token(credentials=credentials)
        return self.__controller.get_ceo_breed(breed_name=breed_name, user_id=token_info['id'])
    
    async def stats(self, credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)) -> StatsResponse:
        token_info = decode_access_token(credentials=credentials)
        return self.__controller.get_stats()


dogsRouter = DogsRouter()