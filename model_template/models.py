# contains the entities of the tables used in the db


from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    predictions = relationship("Prediction", back_populates="caller")

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    details = Column(String)
    prediction_date = Column(DateTime)
    prediction = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    caller = relationship("User", back_populates="predictions")
    features = relationship("Features", back_populates="predictor")

class Features(Base):
    __tablename__ = "features"
    
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
    feature_idx = Column(Integer)

    prediction_id = Column(Integer, ForeignKey("predictions.id"))

    predictor = relationship("Prediction", back_populates="features")