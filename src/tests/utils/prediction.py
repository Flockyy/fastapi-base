from sqlalchemy.orm import Session

import crud
import models

from src.schemas.prediction import PredictionCreate

from src.tests.utils.utils import random_lower_string


def create_random_prediction(db: Session) -> models.Prediction:

    text = random_lower_string()
    pred_in = PredictionCreate(text=text)
    return crud.prediction.create(db=db, obj_in=pred_in)