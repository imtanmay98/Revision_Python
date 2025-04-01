import pytest
import allure
import requests
@allure.title("To verify GET request-> booking API")
@allure.description("To verify it gives a success response.")
@allure.tag("regression", "p0", "smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Tanmay Rout")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TC#4")
@pytest.mark.smoke
def test_single_get_req_resp():
    url = "https://restful-booker.herokuapp.com/booking"
    response_data = requests.get(url)
    print(response_data.headers)
    assert response_data.status_code == 200