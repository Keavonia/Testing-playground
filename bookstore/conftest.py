import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .pages.login_page import LoginPage
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")  # выбор браузера

    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, fr")  # выбор языка


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True, scope="function")
def setup(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()

    email = f'testuser{int(time.time())}@example.com'
    password = "qscrgnyjq"

    page.register_new_user(email, password)

    page.should_be_authorized_user()

    print(f'User registered and logged in: {email}')

    return browser