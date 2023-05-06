
import requests

class TestAPI:
    def test_login_code(self):
        response = requests.post( "https://qa-api.trado.co.il/api/admin-user/logincode")
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"

    def test_login(self):
        response = requests.post("https://qa-api.trado.co.il/api/admin-user/login")
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"

    def test_loguot(self):
        response = requests.post("https://qa-api.trado.co.il/api/admin-user/logout")
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"
    def test_change_language_in_page(self):
        response = requests.post("https://qa-api.trado.co.il/api/language/getLanguage" )
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"

    def test_test_change_page_to_orders(self):
        response = requests.post("https://qa-api.trado.co.il/api/order/filter")
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"

    def test_change_page_to_dashboard(self):
         response = requests.post("https://qa-api.trado.co.il/api/statistics/dashboard")
         assert response.status_code == 200 , f"POST request failed. Status Code: {response.status_code}"

    def test_change_page_to_delivery_table(self):
        response = requests.post("https://qa-api.trado.co.il/api/v1/deliveries/1950000007")
        assert response.status_code == 200, f"POST request failed. Status Code: {response.status_code}"