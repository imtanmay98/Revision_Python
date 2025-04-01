import allure
import pytest
import requests

@allure.title("TC#1 - Create booking CRUD Positive")
@allure.description("TC#1 - verify Create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers,json=payload)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["bookingdates"]["totalprice"]["lastname"]
