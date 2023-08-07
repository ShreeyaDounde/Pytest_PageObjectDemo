import pytest
from selenium import webdriver
#from selenium.webdriver.common

#add arg --browser this is for the command liner

def pytest_addoption(parser):
    parser.addoption("--browser")

#passing the value to the browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#here we are passing the actual value to --browser

@pytest.fixture()
def setup(browser):
    if browser== 'Chrome':
        driver=webdriver.Chrome()
        print("launching the chrome ")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("launching the firefox")
    elif browser=='edge':
        driver=webdriver.Edge()
        print("luanching the edge")
    else:
        print("headlessmode")
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver=webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    return driver

#pytest metadata

def pytest_metadata(metadata):
    #to add
    metadata["Class"]="credence"
    metadata["batch"]="CT15"
    metadata["URL"]="https://automation.credence.in"
    #to remove
    metadata.pop("Platform",None)

#use parameter when u have small summary
@pytest.fixture(params=[
    ("Credencetest@test.com", "Credence@123"),
    ("Credencetest@test.com1", "Credence@123"),
    ("Credencetest@test.com", "Credence@1231"),
    ("Credencetest@test.com1", "Credence@1231")
])
def getDataforLogin(request):
    return request.param