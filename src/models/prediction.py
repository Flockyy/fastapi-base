from sqlalchemy import Column, Integer, String

from db.base_class import Base

class Prediction(Base):
  id= Column(Integer, primary_key=True, index=True)
  text= Column(String, index=True)