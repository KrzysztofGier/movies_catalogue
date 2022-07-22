from main import app
from unittest.mock import Mock
import tmdb_client
import pytest

@pytest.mark.parametrize('list_type', (
    ('now_playing'),
    ('popular'),
    ('top_rated'),
    ('upcoming')
))

#@pytest.mark.parametrize('list_type', (
#    ('popular'),
#))

def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': [list_type]})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(f'movie/{list_type}')