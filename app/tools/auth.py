import jwt
import os
from fastapi import HTTPException

SUPER_SECRET_KEY = os.getenv('SUPER_SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

def decode_access_token(token: str) -> dict:
    '''Decode and validate the token'''
    try:
        return jwt.decode(token, SUPER_SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, 'Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(401, 'Unauthorized, invalid token')