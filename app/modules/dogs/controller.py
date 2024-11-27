from .model import DogsModel
import httpx
from .schemas import BreedResponse, BreedCache
from fastapi import HTTPException, status
from .cache import cache
from datetime import datetime, timedelta


class DogsController():
    
    __model: DogsModel
    
    def __init__(self) -> None:
        self.__model = DogsModel()
        
        
    def get_ceo_breed(self, breed_name: str) -> BreedResponse:
        cache_use = False
        if breed_name in cache and cache[breed_name].expire >= datetime.now():
            cache_use = True
            cache[breed_name].expire = datetime.now() + timedelta(minutes=5)
        
        if not cache_use:
            request_url = f'https://dog.ceo/api/breed/{breed_name}/images/random'
            response = httpx.get(request_url)
            result: dict = response.json()
            
        
        self.__model.set_breed_stats(breed_name=breed_name)
        self.__model.set_breed_requets(
            breed_name=breed_name, 
            detail=result['message'] if not cache_use else cache[breed_name].image,
            request_url=request_url if not cache_use else cache[breed_name].request_url,
            cache=cache_use,
            request_status=result['status'] if not cache_use else cache[breed_name].status
        )
        
        if not cache_use and response.status_code != 200:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail='Third party api failed')

        if not cache_use:
            cache[breed_name] = BreedCache(image=result['message'], expire=datetime.now() + timedelta(minutes=5), request_url=request_url, status=result['status'])
        
        return BreedResponse(breed_name=breed_name, image=result['message'] if not cache_use else cache[breed_name].image)