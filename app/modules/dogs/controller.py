from .model import DogsModel
import httpx
from .schemas import BreedResponse, BreedCache, StatsResponse
from fastapi import HTTPException, status
from .cache import cache
from datetime import datetime, timedelta


class DogsController():
    
    __model: DogsModel
    
    def __init__(self) -> None:
        self.__model = DogsModel()
        
        
    def get_ceo_breed(self, breed_name: str, user_id: int) -> BreedResponse:
        cache_use: bool = False
        request_status: int = None

        if breed_name in cache and cache[breed_name].expire >= datetime.now():
            cache_use, request_status = True, cache[breed_name].status_code
            cache[breed_name].expire = datetime.now() + timedelta(minutes=5)
        
        if not cache_use:
            request_url = f'https://dog.ceo/api/breed/{breed_name}/images/random'
            response = httpx.get(request_url)
            result: dict = response.json()
            request_status = response.status_code if 'status' in result else 503
        
        if request_status == 503:
            self.__set_breed_info(breed_name=breed_name, user_id=user_id, details='The api service are unavailable, try some later', request_url=request_url, cache_use=cache_use, request_status=response.status_code)
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail='The api service are unavailable, try some later')

        if not cache_use:
            cache[breed_name] = BreedCache(detail=result['message'], expire=datetime.now() + timedelta(minutes=5), request_url=request_url, status_code=request_status)

        self.__set_breed_info(
            breed_name=breed_name, 
            user_id=user_id,
            details=result['message'] if not cache_use else cache[breed_name].detail,
            request_url=request_url if not cache_use else cache[breed_name].request_url,
            cache_use=cache_use,
            request_status=request_status
        )

        if request_status == 404:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result['message'] if not cache_use else cache[breed_name].detail)
        
        return BreedResponse(breed_name=breed_name, image=result['message'] if not cache_use else cache[breed_name].detail)
    

    def __set_breed_info(self, breed_name: str, user_id: str, details: str, request_url: str, cache_use: bool, request_status: int) -> None:
        self.__model.set_breed_stats(breed_name=breed_name)
        self.__model.set_breed_requets(
            breed_name=breed_name,
            user_id=user_id,
            detail=details,
            request_url=request_url,
            cache=cache_use,
            request_status=request_status
        )
    
    
    def get_stats(self) -> StatsResponse:
        breeds_stats_response = self.__model.get_breed_stats()
        return StatsResponse(top_breeds=breeds_stats_response)