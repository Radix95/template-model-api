# contains the utils functions related to the management of the token


from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt 
from . import schemas
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']   # environment variables set in .env file
ALGORITHM = os.environ['ALGORITHM']     # environment variables set in .env file
ACCESS_TOKEN_EXPIRE_MINUTES = 30        # default expiration timedelta


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception

def get_current_id(token: str, credentials_exception):
    try:
        payload = jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        if id is None:
            raise credentials_exception
        
        return id
        
    except JWTError:
        raise credentials_exception
