from app.db import engine
from sqlmodel import Session, select
from app.db.schemas import BreedStats, BreedRequests


class DogsModel():
    
    def __init__(self) -> None:
        pass
    
    
    def set_breed_stats(self, breed_name: str) -> None:
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
                
                
    def set_breed_requets(self, breed_name: str, detail: str, request_url: str, cache: bool, request_status: str) -> None:
        with Session(engine) as session:
            breed_request = BreedRequests(breed_name=breed_name, detail=detail, request_url=request_url, cache=cache, request_status=request_status)
            session.add(breed_request)
            session.commit()