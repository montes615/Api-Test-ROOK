import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
import os
from fastapi import HTTPException
from .model import AuthModel
from .schemas import RegisterUser, TokenData, TokenResponse

SUPER_SECRET_KEY = os.getenv('SUPER_SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

class AuthController():
    
    __pwd_context: CryptContext
    __model: AuthModel
    
    def __init__(self) -> None:
        self.__pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        self.__model = AuthModel()
    
    
    def hash_password(self, password: str) -> str:
        'Generate a password hash'
        return self.__pwd_context.hash(password)


    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        '''Verify the hash of the password'''
        return self.__pwd_context.verify(plain_password, hashed_password)
    
    
    def create_access_token(self, data: TokenData, expires_delta: timedelta = timedelta(minutes=15)) -> TokenResponse:
        '''Create a JWT'''
        to_encode = data.model_dump()
        to_encode['exp'] = datetime.now() + expires_delta
        return TokenResponse(access_token=jwt.encode(to_encode, SUPER_SECRET_KEY, algorithm=ALGORITHM), usage=data.usage)
    
    
    def decode_access_token(self, token: str) -> dict:
        '''Decode and validate the token'''
        try:
            return jwt.decode(token, SUPER_SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, 'Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(401, 'Unauthorized, invalid token')
        
        
    def register_user(self, registerUser: RegisterUser) -> str:
        hashed_password = self.hash_password(password=registerUser.password)
        self.__model.add_user(username=registerUser.username, hashed_password=hashed_password)