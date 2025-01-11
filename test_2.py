import pytest
from main import get_github_user

def test_get_github_user(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login' : 'nizavr',
        'id' : '345675',
        'name' : 'Nina'
    }

    user_data = get_github_user('nizavr')
    assert user_data == {
        'login' : 'nizavr',
        'id' : '345675',
        'name' : 'Nina'
    }


def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500

    user_data = get_github_user('nizavr')
    assert user_data == None