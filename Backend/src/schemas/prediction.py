from typing import Optional

from pydantic import BaseModel

# Shared properties
class PredictionBase(BaseModel):
    text: Optional[str] = None
  
# Properties to receive via API on creation
class PredictionCreate(PredictionBase):
    text: str
    
# Properties to receive via API on update
class PredictionUpdate(PredictionBase):
    pass

class PredictionInDBBase(PredictionBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Additional properties to return via API

class Prediction(PredictionInDBBase):
    pass
  