from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from core.config import settings
from tests.utils.prediction import create_random_prediction


def test_create_prediction(
    client: TestClient
) -> None:
    data = {"text": "Hey"}
    response = client.post(
        f"{settings.API_V1_STR}/predictions/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["text"] == data["texet"]
    assert "id" in content


def test_read_prediction(
    client: TestClient, db: Session
) -> None:
    pred = create_random_prediction(db)
    response = client.get(
        f"{settings.API_V1_STR}/predictions/{pred.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["text"] == pred.text
    assert content["id"] == pred.id