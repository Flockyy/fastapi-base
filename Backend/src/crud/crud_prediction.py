from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.prediction import Prediction
from schemas.prediction import PredictionCreate, PredictionUpdate


class CRUDPrediction(CRUDBase[Prediction, PredictionCreate, PredictionUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Optional[Prediction]:
        return db.query(Prediction).filter(Prediction.id == id).first()
      
    def get_multi_by_owner(
      self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Prediction]:
      return (
        db.query(self.model)
        .filter(Prediction.owner_id == owner_id)
        .offset(skip)
        .limit(limit)
        .all()
      )
    
    def create(self, db: Session, *, obj_in: PredictionCreate) -> Prediction:
        db_obj = Prediction(
            text=obj_in.text,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Prediction, obj_in: Union[PredictionUpdate, Dict[str, Any]]
    ) -> Prediction:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

prediction = CRUDPrediction(Prediction)