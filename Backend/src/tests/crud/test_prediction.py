from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import crud
from schemas.prediction import PredictionCreate, PredictionUpdate
from tests.utils.utils import random_lower_string

def test_create_prediction(db: Session) -> None:
    text = random_lower_string()
    pred_in = PredictionCreate(text=text)
    pred = crud.prediction.create(db, obj_in=pred_in)
    assert pred.text == text
    assert hasattr(pred, "text")

def test_get_prediction(db: Session) -> None:
    text = random_lower_string()
    pred_in = PredictionCreate(text=text)
    pred = crud.prediction.create(db, obj_in=pred_in)
    pred_2 = crud.prediction.get(db, id=pred.id)
    assert pred_2
    assert pred.text == pred.text
    assert jsonable_encoder(pred) == jsonable_encoder(pred_2)

def test_update_prediction(db: Session) -> None:
    text = random_lower_string()
    pred_in = PredictionCreate(text=text)
    pred = crud.prediction.create(db, obj_in=pred_in)
    new_text = random_lower_string()
    pred_in_update = PredictionUpdate(text=new_text)
    crud.prediction.update(db, db_obj=pred, obj_in=pred_in_update)
    pred_2 = crud.prediction.get(db, id=pred.id)
    assert pred_2
    assert pred.email == pred_2.email