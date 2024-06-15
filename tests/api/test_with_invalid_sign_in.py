import allure
from allure_commons.types import Severity
from jsonschema import validate
from allplay_tests.schemas.invalid_sign_in import invalid_sign_in
from allplay_tests.utils.api_helper import api_request


@allure.title('Authorization with invalid data')
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Authorization with invalid data')
@allure.story('Authorization')
def test_sign_in(base_api_url):
    with allure.step('Send request with invalid data'):
        response = api_request(base_api_url, '/api/v1/login', 'POST',
                               {"email": 'login', "password": 'password'})

    with allure.step('Status code=422'):
        assert response.status_code == 422
        response_json = response.json()
    with allure.step('Checking whether the movie name matches the request'):
        assert response_json['errors']['email'] == ['Имя пользователя и пароль не совпадают.']
    with allure.step('Schema is validate'):
        validate(response.json(), invalid_sign_in)
