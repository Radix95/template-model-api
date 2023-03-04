from fastapi import APIRouter, Depends, status, Response, Header, Request
from .. import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import modelML


router = APIRouter(
    prefix="/modelml",             # each api path in this file is preeceded by this prefix
    tags=['models']
)


get_db = database.get_db


@router.post('', response_model=List[schemas.Prediction])
def predict(request: schemas.FeaturesVector, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.current_active_user), Authorization: str = Header(default=None)):
    return modelML.predict(request, db, save_predictions=True, save_features=True, limit=5, access_token=Authorization)

@router.get('')
def get_info(request: Request, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.current_active_user)):
    return modelML.info(request, db)

