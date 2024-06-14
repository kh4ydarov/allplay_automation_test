import allure
import requests
from allure_commons.types import Severity
from jsonschema import validate
from allplay_tests.schemas.invalid_sign_in import invalid_sign_in


@allure.title('Authorization with invalid data')
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Authorization with invalid data')
@allure.story('Authorization')
def test_sign_in(base_api_url):
    with allure.step('Send request with invalid data'):
        response = requests.post(f'{base_api_url}/api/v1/login', data={'email': 'login',
                                                                       'password': 'password'})

    with allure.step('Status code=422'):
        assert response.status_code == 422
    with allure.step('Schema is validate'):
        validate(response.json(), invalid_sign_in)
