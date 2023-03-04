# contains the API method related to the mdi resources


from fastapi import APIRouter, Depends, status, Response, Header
from .. import schemas, database
from typing import List
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",             # each api path in this file is preeceded by this prefix
    tags=['users']
)

get_db = database.get_db


@router.post('', response_model=schemas.ShowUser, include_in_schema=False)
def create_user(request: schemas.User, db: Session = Depends(get_db), MDIuser: str = Header(default=None)):
    return user.create(request, db, MDIuser)
    

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, include_in_schema=False)
def get_user(id: int, db: Session = Depends(get_db), MDIuser: str = Header(default=None)):
    return user.show(id, db, MDIuser)


@router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser], include_in_schema=False)
def get_all_user(db: Session = Depends(get_db), MDIuser: str = Header(default=None)):
    return user.show_all(db, MDIuser)


@router.delete('/{id}', status_code=status.HTTP_200_OK, include_in_schema=False)
def destroy(id, db: Session = Depends(get_db), MDIuser: str = Header(default=None)):
    return user.destroy(id, db, MDIuser)