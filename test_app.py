import pytest
import json
from app import app  # Importiere deine Flask-App

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test für GET-Anfrage
def test_get_data(client, monkeypatch):
    # Dummy-Inhalt für data.jsonl erstellen
    test_data = [{"name": "test1", "value": 10}, {"name": "test2", "value": 20}]
    monkeypatch.setattr("builtins.open", lambda f, mode: iter([json.dumps(item) for item in test_data]))

    response = client.get('/stock')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data == test_data

# Test für DELETE-Anfrage
def test_delete_data(client, monkeypatch):
    def mock_remove(path):
        # Mock-Funktion zum Löschen
        pass

    monkeypatch.setattr("os.remove", mock_remove)
    response = client.delete('/stock')
    assert response.status_code == 200
    assert response.json == {"response": "Succeed"}

# Test für GET-Anfrage, wenn die Datei nicht vorhanden ist
def test_get_data_file_not_found(client, monkeypatch):
    def mock_open(path, mode):
        raise FileNotFoundError

    monkeypatch.setattr("builtins.open", mock_open)
    response = client.get('/stock')
    assert response.status_code == 404
    assert response.json == {"response": "No Data"}

# Test für DELETE-Anfrage, wenn die Datei nicht vorhanden ist
def test_delete_data_file_not_found(client, monkeypatch):
    def mock_remove(path):
        raise FileNotFoundError

    monkeypatch.setattr("os.remove", mock_remove)
    response = client.delete('/stock')
    assert response.status_code == 404
    assert response.json == {"response": "No Data"}
