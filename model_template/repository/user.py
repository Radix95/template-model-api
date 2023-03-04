# contains the actions triggered by the api calls of the User resources
# these functions are called from the APIs in their relative router

from fastapi import Depends, status, HTTPException
from .. import models
from sqlalchemy.orm import Session
from ..hashing import Hash
import os
from dotenv import load_dotenv

load_dotenv()

CREATE_USER_KEY = os.environ['CREATE_USER_KEY']

def create(request, db: Session, MDIuser):

    if (MDIuser!=CREATE_USER_KEY):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized - Minerva Digital Intelligence")

    new_user = models.User(name=request.name, email=request.email, password= Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def show(id, db: Session, MDIuser):
    
    if (MDIuser!=CREATE_USER_KEY):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized - Minerva Digital Intelligence")

    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} not found - Minerva Digital Intelligence")

    return user


def show_all(db: Session, MDIuser):
    
    if (MDIuser!=CREATE_USER_KEY):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized - Minerva Digital Intelligence")

    user = db.query(models.User).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found - Minerva Digital Intelligence")

    return user


def destroy(id, db: Session, MDIuser):

    if (MDIuser!=CREATE_USER_KEY):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized - Minerva Digital Intelligence")

    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    db.delete(user)
    db.commit()

    return {'data': f"User with the id {id} deleted"}