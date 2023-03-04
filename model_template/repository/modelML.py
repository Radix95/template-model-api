from fastapi import Depends, status, HTTPException
from .. import models, token
from sqlalchemy.orm import Session
from ..hashing import Hash
import pickle
import numpy as np
from datetime import datetime


# if taken out of the scope of the function the model is loaded only once 
# at the startup of the application
def import_model():
    model = pickle.load(open("./artifacts/model.pkl", 'rb'))

    return model

def preprocess(feat):
    return feat+2

def predict(request, db: Session, save_predictions: bool = False, save_features: bool = False, limit: int = 5, access_token: str = None): 

    feat1 = np.asarray(request.feat1)
    feat2 = np.asarray(request.feat2)
    feat3 = np.asarray(request.feat3)

    if (len(feat1)>limit) | (len(feat2)>limit) | (len(feat3)>limit):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Max length of features vectors must be less than {limit} - Minerva Digital Intelligence")

    if (len(feat1)!=len(feat2))|(len(feat1)!=len(feat3)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Malformed input features - Minerva Digital Intelligence")

    feat1 = preprocess(feat=feat1)   

    feats = np.asarray([feat1, feat2, feat3]).T
    
    model = import_model()
    preds =  model.predict(feats).tolist()

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    new_preds_list = [models.Prediction(details="test pred", prediction_date=datetime.now(), prediction= str(x), user_id=token.get_current_id(access_token, credentials_exception)) for x in preds]

    if save_predictions:

        db.add_all(new_preds_list)
        db.commit()

    if save_features:
        [db.refresh(p) for p in new_preds_list]

        feat_list = []

        for idx1, p in enumerate(new_preds_list):      
            feat = feats[idx1]      
            for idx2, f in enumerate(feat):
                new_feat = models.Features(value=str(f), feature_idx=idx2, prediction_id=p.id)
                feat_list.append(new_feat)  

        db.add_all(feat_list)
        db.commit()

    return new_preds_list 


def info(request, db: Session):
    return {'data': "This method returns model's info - Minerva Digital Intelligence"} 