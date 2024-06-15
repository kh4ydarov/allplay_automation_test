import allure
import requests
from allure_commons.types import Severity
from jsonschema import validate
from allplay_tests.schemas.search_cinema import search_movie


@allure.title('Search cinema by name API')
@allure.epic('Search cinema with API')
@allure.story('Get cinema')
@allure.feature('Searching cinema with API')
@allure.tag('API')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
def test_search(base_api_url):
    with allure.step('Send request with valid data'):
        response = requests.get(f'{base_api_url}/api/v1/movies',
                                data={"search": "Не с первой попытки", "per_page": "1"})

    with allure.step('Status code=200'):
        assert response.status_code == 200

        response_json = response.json()
    with allure.step('Checking whether the movie name matches the request'):
        assert response_json['data'][0]['title'] == 'Не с первой попытки'
    with allure.step('Schema is validate'):
        validate(response.json(), search_movie)
