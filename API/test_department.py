import requests
from src.utils.setup import WebDriverSetup
from faker import Faker


class TestTORADO(WebDriverSetup):
    def test_1_add_new_department(self, setUp):
        fake = Faker()
        random_name = fake.name()
        response = requests.post('https://qa-api.trado.co.il/api/department/create', data={'name': random_name})
# Check if the response status code is 200 using an assertion
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"
# If the assertion passes, print a success message
        print("POST request was successful. Status Code: 200")
