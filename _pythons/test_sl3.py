import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

@pytest.mark.smoke
def test_verify_sum():
    assert 2 + 1 == 3

@pytest.mark.smoke
def test_verify_sub():
    assert 2-1==1
@pytest.mark.reg
def test_verify_sum1():
    assert 2 + 4 == 3

@pytest.mark.skip(reason="Not compleated yet, Skip it!")
def test_verify_sub1():
    assert 6-1==1