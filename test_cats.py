import pytest
from main import get_random_cat


def test_get_random_cat(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'url' : 'https://cdn2.thecatapi.com/images/MjA1OTc5OA.jpg'
    }

    random_cat_data = get_random_cat()

    assert random_cat_data == {
        'url' : 'https://cdn2.thecatapi.com/images/MjA1OTc5OA.jpg'
    }


def test_get_random_cat_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    random_cat_data = get_random_cat()
    assert random_cat_data == None