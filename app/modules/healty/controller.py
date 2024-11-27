from .model import HealtyModel
from time import time
from .schemas import HealtyObject
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import httpx


class HealtyController():

    __model: HealtyModel

    def __init__(self):
        self.__model = HealtyModel()


    def check_db_healty(self) -> HealtyObject:
        start_time = time()
        try:
            status, message = 'ok', f'All fine!'
            user = self.__model.get_user_by_id(1)
        except IntegrityError as e:
            status, message = 'failed', f'Integrity error: {str(e)}'
        except SQLAlchemyError as e:
            status, message = 'failed', f'SQLAlchemy error: {str(e)}'
        except Exception as e:
            status, message = 'failed', f'General exception: {str(e)}'
        finally:
            end_time = time()
            return HealtyObject(status=status, message=message, task_time=((start_time - end_time) * 1000))
        

    def check_breed_api_healty(self) -> HealtyObject:
        start_time = time()
        try:
            status, message = 'ok', f'All fine!'
            request_url = f'https://dog.ceo/api/breed/husky/images/random'
            response = httpx.get(request_url)
            result: dict = response.json()
            
            if 'status' not in result:
                status, message = 'failed', 'The api request failed'

        except Exception as e:
            status, message = 'failed', f'General exception: {str(e)}'
        finally:
            end_time = time()
            return HealtyObject(status=status, message=message, task_time=((start_time - end_time) * 1000))