import jwt
import os
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SUPER_SECRET_KEY = os.getenv('SUPER_SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

bearer_auth = HTTPBearer()

def decode_access_token(credentials: HTTPAuthorizationCredentials) -> dict:
    '''Decode and validate the token'''
    try:
        token = credentials.credentials
        return jwt.decode(token, SUPER_SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Expired token', headers={'WWW-Authenticate': 'Bearer'})
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized, invalid token', headers={'WWW-Authenticate': 'Bearer'})