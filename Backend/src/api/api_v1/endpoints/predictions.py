from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, schemas

from api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Prediction])
def read_predictions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve predictions.
    """
    preds = crud.prediction.get_multi(db, skip=skip, limit=limit)
    return preds


@router.post("/", response_model=schemas.Prediction)
def create_prediction(
    *,
    db: Session = Depends(deps.get_db),
    pred_in: schemas.PredictionCreate,
) -> Any:
    """
    Create new prediction.
    """
    pred = crud.prediction.create(db=db, obj_in=pred_in)
    return pred


@router.put("/{id}", response_model=schemas.Prediction)
def update_prediction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    pred_in: schemas.PredictionUpdate,
) -> Any:
    """
    Update a prediction.
    """
    pred = crud.prediction.get(db=db, id=id)
    if not pred:
        raise HTTPException(status_code=404, detail="Prediction not found")
    pred = crud.prediction.update(db=db, db_obj=pred, obj_in=pred_in)
    return pred


@router.get("/{id}", response_model=schemas.Prediction)
def read_prediction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get prediction by ID.
    """
    pred = crud.prediction.get(db=db, id=id)
    if not pred:
        raise HTTPException(status_code=404, detail="Prediction not found")

    return pred


@router.delete("/{id}", response_model=schemas.Prediction)
def delete_prediction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an prediction.
    """
    pred = crud.prediction.get(db=db, id=id)
    if not pred:
        raise HTTPException(status_code=404, detail="Prediction not found")
    pred = crud.prediction.remove(db=db, id=id)
    return pred