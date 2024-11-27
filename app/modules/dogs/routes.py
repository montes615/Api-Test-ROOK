from fastapi import APIRouter, Depends
from .controller import DogsController
from fastapi.security import HTTPAuthorizationCredentials
from app.tools.auth import bearer_auth, decode_access_token
from .schemas import BreedResponse


class DogsRouter(APIRouter):
    
    __controller: DogsController
    
    def __init__(self):
        super().__init__()
        
        self.__controller = DogsController()
        
        self.add_api_route('/dog/breed/{breed_name}', self.breed, methods=['GET'], response_model=BreedResponse, dependencies=[Depends(bearer_auth)])
        
        
    async def breed(self, breed_name: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)) -> BreedResponse:
        decode_access_token(credentials=credentials)
        return self.__controller.get_ceo_breed(breed_name=breed_name)


dogsRouter = DogsRouter()