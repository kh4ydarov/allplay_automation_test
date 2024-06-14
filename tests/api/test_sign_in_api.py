import os
import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate
from allplay_tests.schemas.sign_in import login_user


@allure.title('Authorization with API')
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Authorization with API')
@allure.story('Getting token')
def test_sign_in(base_api_url):
    load_dotenv()

    login = os.getenv('user_api_email')
    password = os.getenv('user_api_password')

    with allure.step('Send request with valid data'):
        response = requests.post(f'{base_api_url}/api/v1/login', data={'email': login,
                                                                       'password': password})

    with allure.step('Status code=200'):
        assert response.status_code == 200
        response_json = response.json()
    with allure.step('Checking whether the response contains api_token'):
        assert 'api_token' in response_json, "'api_token' not found in the response body"
        assert response_json['api_token'] is not None, "'api_token' is None"
    with allure.step('Schema is validate'):
        validate(response.json(), login_user)
