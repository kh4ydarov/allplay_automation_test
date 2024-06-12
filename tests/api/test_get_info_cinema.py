import allure
import requests
from allure_commons.types import Severity
from jsonschema import validate
from allplay_tests.schemas.open_cinemas_cart import click_cinema


@allure.title('Get cinema Info')
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Getting cinema info with API')
@allure.story('Get cinema')
def test_get_cinema_info(base_api_url):
    cinema_id = 3673
    with allure.step('Send request with valid data'):
        response = requests.get(f'{base_api_url}/api/v1/movie/{cinema_id}')

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Schema is validate'):
        validate(response.json(), click_cinema)
