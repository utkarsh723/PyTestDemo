import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType
import allure
import os, subprocess


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if request.param == "firefox":
        web_driver = webdriver.Firefox(GeckoDriverManager().install())
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call ,report):
    if report.failed:
        allure.attach(node.nodeid,node.instance.driver.get_screenshot_as_png(), "Attachment", AttachmentType.PNG)


# Run allure report generation
def pytest_sessionfinish(session):
    # os.system('allure serve allure-reports')
    os.system('allure generate allure-reports/json -o allure-reports/html --clean')
