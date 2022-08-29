from selenium.webdriver import DesiredCapabilities
from seleniumwire import webdriver
import logging
import time

logging.basicConfig(level=logging.DEBUG)
HOST = '127.0.0.1'

options = {
    'auto_config': False,
    'addr': HOST,
    'port': 9922,
}

chrome_capabilities = {
    "browserName": "chrome",
    "selenoid:options": {
        "enableVNC": True
    },
    'goog:chromeOptions': {'extensions': [],
                           'args': ['--proxy-server=host.docker.internal:9922',
                                    '--ignore-certificate-errors', '--force-dark-mode']
                           }
}

firefox_capabilities = {
    "browserName": "firefox",
    "marionette": False,
    "selenoid:options": {
        "enableVNC": True
    },
    'moz:firefoxOptions': {'args': ['--proxy-server=host.docker.internal:9922',
                                    '--ignore-certificate-errors',
                                    '--force-dark-mode', ]}
}


def test_firefox():
    print("Firefox starting test ...")
    firefox = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                               desired_capabilities=firefox_capabilities,
                               seleniumwire_options=options)
    firefox.get('https://www.github.com')
    print('Firefox', firefox.title)
    print(firefox.requests)
    for request in firefox.requests:
        if request.response:
            print(
                request.path,
                request.response.status_code,
                request.response.headers['Content-Type']
            )
    time.sleep(100)
    firefox.quit()


def test_chrome():
    print("Chrome starting test ...")
    chrome = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                              desired_capabilities=chrome_capabilities,
                              seleniumwire_options=options)
    chrome.get('https://www.github.com')
    print('chrome', chrome.title)
    for request in chrome.requests:
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )
    time.sleep(15)
    chrome.quit()


if __name__ == "__main__":
    test_chrome()
    # test_firefox()
