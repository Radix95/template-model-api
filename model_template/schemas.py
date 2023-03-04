# contains the pydantic classes used in the APIs


from typing import Optional, List
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


# classes with prefix "Show" are used as ResponseModel, which returns 
# only a subset of the available information
# e.g. if an API returns the list of the Users, only the name and the email are returned
class ShowUser(BaseModel):   
    id: int     
    name: str
    email: str

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class FeaturesVector(BaseModel):
    feat1: List[float]
    feat2: List[float]
    feat3: List[float]


class Prediction(BaseModel):
    prediction: float 
    
    class Config:
        orm_mode = True