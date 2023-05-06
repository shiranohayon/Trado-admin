import requests
from src.utils.setup import WebDriverSetup
from src.utils.db import get_random_product, get_product_by_id


class TestTrado(WebDriverSetup):

    def test_edit_product_description(self, setUp):
        product = get_random_product(self.db)
        id = product["id"]
        new_description = "bhjgj"
        url = "https://qa-api.trado.co.il/api/product/update"
        headers = {
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI0anA1N3dwbGdldmdwMnIiLCJpYXQiOjE2ODIwODExNDcsImV4cCI6MTY4NDY3MzE0N30.cuGPTCGMvLJa27UzRA0N3JrPVjUZbxZ5Zqusck4r-nE",
        }
        data = {
            "id": id,
            "description": new_description
        }
        response = requests.post(url, headers=headers, json=data)
        assert response.status_code == 200
        after_update_product = get_product_by_id(self.db, id)
        assert after_update_product["description"] == new_description


    def test_search_valid_product(self, setUp):
        product_name_to_search = self.products_page.get_product_name_to_search(self.db)
        url = "https://qa-api.trado.co.il/api/product/filter"
        headers = {
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI0anA1N3dwbGdldmdwMnIiLCJpYXQiOjE2ODIwODExNDcsImV4cCI6MTY4NDY3MzE0N30.cuGPTCGMvLJa27UzRA0N3JrPVjUZbxZ5Zqusck4r-nE",
        }
        data = {
            "search": product_name_to_search
        }
        response = requests.post(url, headers=headers, json=data)
        assert response.status_code == 200
        product_name_from_api_response = response.json()['payload']['data'][0]['name']
        assert product_name_to_search == product_name_from_api_response


    def test_login_with_phone_not_existing(self, setUp):
        url = "https://qa-api.trado.co.il/api/admin-user/logincode"
        phone_not_in_db = '1950000022'
        data = {
            'phone': phone_not_in_db
        }
        response = requests.post(url, json=data)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["status"] == 400
        assert response_json["err"] == "no such user"





