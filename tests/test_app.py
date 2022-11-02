import pytest
from app.main import create_app


@pytest.fixture
def client():
    app = create_app("TESTING")
    client = app.test_client()
    yield client


def test_info(client):
    app = create_app("TESTING")
    # main.app.config['TESTING'] = True
    client = app.test_client()
    response = client.get('api/v1/')
    print(response)

    result = response.get_json()
    assert result is not None
    assert "message" in result
    assert result["message"] == "Sojern Math library"


def test_average(client):
    values = [5, 3, 4, 1, 10, 15, -10, -20]
    request_payload = {"values": values}
    response = client.post("api/v1/average", json=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert 'average' in result
    assert result['average'] == 1.0


def test_minimum(client):
    values = [5, 3, 4, 1, 10, 15, -10, -20]
    request_payload = {"values": values, "quantifier": 3}
    response = client.post("api/v1/min", json=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert 'min' in result
    assert result['min'] == [-20, -10, 1]


def test_maximum(client):
    values = [5, 3, 4, 1, 10, 15, -10, -20]
    request_payload = {"values": values, "quantifier": 3}
    response = client.post("api/v1/max", json=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert 'max' in result
    assert result['max'] == [15, 10, 5]


def test_median(client):
    values = [5, 3, 4, 1, 10, 15, -10, -20]
    request_payload = {"values": values}
    response = client.post("api/v1/median", json=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert 'median' in result
    assert result['median'] == 3.5


def test_percentile(client):
    values = [5, 3, 4, 1, 10, 15, -10, -20, 5, 10, 12]
    request_payload = {"values": values, "quantifier": 90}
    response = client.post("api/v1/percentile", json=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert 'percentile' in result
    assert result['percentile'] == 12
