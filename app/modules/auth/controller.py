import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import os
from .model import AuthModel
from .schemas import RegisterUser, TokenData, TokenResponse, LoginUser
from app.db.schemas import User
from fastapi import HTTPException, status

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
    
    
    def create_access_token(self, data: TokenData, expires_delta: timedelta = timedelta(minutes=60)) -> TokenResponse:
        '''Create a JWT'''
        to_encode = data.model_dump()
        to_encode['exp'] = datetime.now(timezone.utc) + expires_delta
        token = jwt.encode(to_encode, SUPER_SECRET_KEY, algorithm=ALGORITHM)
        return TokenResponse(access_token=token, usage=data.usage)
        
        
    def register_user(self, registerUser: RegisterUser) -> str:
        '''Hash an user password and save the user in the DB'''
        hashed_password = self.hash_password(password=registerUser.password)
        self.__model.add_user(username=registerUser.username, hashed_password=hashed_password, usage=registerUser.usage)


    def valid_user(self, loginUser: LoginUser) -> User:
        '''Valid if the user exists and verify his password'''
        user = self.__model.get_user(username=loginUser.username)
        if not user or not self.verify_password(plain_password=loginUser.password, hashed_password=user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong username or password', headers={'WWW-Authenticate': 'Bearer'})
        
        return user
