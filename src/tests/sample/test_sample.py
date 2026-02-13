import pytest
import allure


@allure.title("verify that the framework is working")
def test_sample_pass():
    assert True == False

@allure.title("verify that the framework is working")
def test_sample_fail():
    assert True == True