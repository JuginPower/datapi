import pytest
from unittest.mock import patch, Mock
from app import app


def test_get_data_with_mocked_data():
    """
    Tests data retrieval.

    :return: 200, len(response.data) > 0
    """

    with app.test_client() as client:
        response = client.get('/stock')
        assert response.status_code == 200
        assert len(response.data) > 0
        response = client.post('/stock')
        assert response.status_code == 200
        assert len(response.data) > 0


def test_handling_missing_file():
    """
    Tests whether after a one-time get and delete request of the data, this data is no longer available when the same
    requests are repeated.

    :return: 200, 200, 404, 404
    """
    mock = Mock(side_effect=[200, 200, 404, 404])

    with app.test_client() as client:
        response = client.get('/stock')
        assert response.status_code == mock()
        response = client.delete('/stock')
        assert response.status_code == mock()
        response = client.get('/stock')
        assert response.status_code == mock()
        response = client.delete('/stock')
        assert response.status_code == mock()

