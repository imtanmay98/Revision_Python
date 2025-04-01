import requests
import pytest
import allure


@allure.title("TC#1 - Create User (Mock API)")
@allure.description("TC#1 - Verify creating a user on a mock API")
@pytest.mark.crud
def test_create_user():
    URL = "https://reqres.in/api/users"
    headers = {"Content-Type": "application/json"}

    payload = {
        "name": "John Doe",
        "job": "QA Engineer"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    response_json = response.json()

    assert response.status_code == 201
    assert "id" in response_json  # Ensure user is created
    print("User Created:", response_json)
