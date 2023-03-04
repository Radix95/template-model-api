# main file of the project


from fastapi import FastAPI
from . import models
from .database import engine
from . routers import user, authentication, modelML

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(modelML.router)



