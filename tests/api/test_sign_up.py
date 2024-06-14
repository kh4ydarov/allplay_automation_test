import os
import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate
from allplay_tests.schemas.sign_up import sign_up_api


@allure.title('Sign up with API')
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Sign up with API')
@allure.story('Sign up')
def test_sign_in(base_api_url):
    load_dotenv()

    name = 'Humoyun'
    login = os.getenv('new_user_email')
    password = os.getenv('new_user_password')

    with allure.step('Send request with valid data'):
        response = requests.post(f'{base_api_url}/api/v1/register', data={'name': name,
                                                                          'email': login,
                                                                          'password': password})

    with allure.step('Status code=200'):
        assert response.status_code == 200
        response_json = response.json()
    with allure.step('Checking whether the movie name matches the request'):
        assert response_json['result'] == 'ok'
    with allure.step('Schema is validate'):
        validate(response.json(), sign_up_api)
