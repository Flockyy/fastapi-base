# Import all the models, so that Base has them before being
# imported by Alembic
from src.db.base_class import Base  # noqa
from src.models.prediction import Prediction  # noqa