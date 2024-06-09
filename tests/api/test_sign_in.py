import os
import allure
import requests
from dotenv import load_dotenv
from jsonschema import validate
from schemas.sign_in import login_user


@allure.epic('Get info about cinema')
@allure.story('Get info about cinema')
@allure.feature('Cinema info')
@allure.tag('API')
@allure.label('Owner')
@allure.severity('High')
def test_sign_in(base_api_url):
    load_dotenv()

    login = os.getenv('user_api_email')
    password = os.getenv('user_api_password')

    with allure.step('Send request with valid data'):
        response = requests.post(f'{base_api_url}/api/v1/login', data={'email': login,
                                                                       'password': password})

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Schema is validate'):
        validate(response.json(), login_user)
