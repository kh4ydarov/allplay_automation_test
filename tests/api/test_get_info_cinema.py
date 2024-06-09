import allure
import requests
from jsonschema import validate
from schemas.open_cinemas_cart import click_cinema


@allure.epic('Get info about cinema')
@allure.story('Get info about cinema')
@allure.feature('Cinema info')
@allure.tag('API')
@allure.label('Owner')
@allure.severity('High')
def test_get_cinema_info(base_api_url):
    cinema_id = 3673
    with allure.step('Send request with valid data'):
        response = requests.get(f'{base_api_url}/api/v1/movie/{cinema_id}')

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Schema is validate'):
        validate(response.json(), click_cinema)
