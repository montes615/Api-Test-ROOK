from app.db import engine
from sqlmodel import Session, select, desc
from app.db.schemas import BreedStats, BreedRequests
from .schemas import BreedStatsResponse
from typing import List


class DogsModel():
    
    def __init__(self) -> None:
        pass
    
    
    def set_breed_stats(self, breed_name: str) -> None:
        '''
        Adds 1 to the number of requests by breed name

        ### Params
            breed_name (str): Breed CEO naem
        '''
        with Session(engine) as session:
            statement = select(BreedStats).where(BreedStats.breed_name == breed_name)
            breed_stats = session.exec(statement).first()
            
            if breed_stats:
                breed_stats.requests += 1
                session.add(breed_stats)
                session.commit()
            else:
                breed_stats = BreedStats(breed_name=breed_name)
                session.add(breed_stats)
                session.commit()
                
                
    def set_breed_requets(self, breed_name: str, user_id: int, detail: str, request_url: str, cache: bool, request_status: int) -> None:
        '''
        Sets the breed ceo api request info

        ### Params
            breed_name (str): Breed CEO name
            user_id (int): ID of the user making the request
            detail (str): Message of the breed ceo api
            request_url (str): Url requested
            cache_use (bool): State of the used cache
            request_status (int): Request http status code
        '''
        with Session(engine) as session:
            breed_request = BreedRequests(breed_name=breed_name, user_id=user_id, detail=detail, request_url=request_url, cache=cache, request_status=request_status)
            session.add(breed_request)
            session.commit()
            
            
    def get_breed_stats(self) -> List[BreedStatsResponse]:
        '''Gets the 10 most requested breeds'''
        with Session(engine) as session:
            statement = select(BreedStats).order_by(desc(BreedStats.requests)).limit(10)
            breeds_stats = session.exec(statement).all()
            
            return [BreedStatsResponse(breed=breed_stats.breed_name, request_count=breed_stats.requests) for breed_stats in breeds_stats]