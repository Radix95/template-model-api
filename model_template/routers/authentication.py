# contains the API method related to the login process

from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=["authentication"]
)


# in create_access_token function, an expiration timedelta can be passed in order to set an expiration to the token
# if not passed, it is set to 30min
@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email, "id": user.id}#, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}