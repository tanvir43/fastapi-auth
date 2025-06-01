# securefastapi_auth/token.py

from datetime import datetime, timedelta
from jose import jwt
from securefastapi_auth import config

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, config.JWT_SECRET_KEY, algorithm=config.ALGORITHM)

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, config.JWT_REFRESH_SECRET_KEY, algorithm=config.ALGORITHM)

def decode_access_token(token: str):
    return jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM])

def decode_refresh_token(token: str):
    return jwt.decode(token, config.JWT_REFRESH_SECRET_KEY, algorithms=[config.ALGORITHM])
