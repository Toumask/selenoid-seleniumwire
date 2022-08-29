from seleniumwire import webdriver
import logging
import time

# logging.basicConfig(level=logging.DEBUG)

HOST = '127.0.0.1'

options = {
    'auto_config': False,
    'addr': HOST,
    'port': 9922
}

chrome_capabilities = {
    "browserName": "chrome",
    "selenoid:options": {
        "enableVNC": True
    },
    'goog:chromeOptions': {'extensions': [],
                           'args': ['--proxy-server=host.docker.internal:9922',
                                    '--ignore-certificate-errors']
                           }
}

opera_capabilities = {
    "browserName": "opera",
    "selenoid:options": {
        "enableVNC": True
    },
    'OperaOptions': {'extensions': [],
                           'args': ['--proxy-server=host.docker.internal:9922',
                                    '--ignore-certificate-errors']
                           }
}

firefox_capabilities = {
    "browserName": "firefox",
    "selenoid:options": {
        "enableVNC": True
    },
    "alwaysMatch": {
        'moz:firefoxOptions': {'extensions': [],
                               'args': ['--proxy-server=host.docker.internal:9922',
                                        '--ignore-certificate-errors',
                                        '--headless']
                               }
    }
}


def test_firefox():
    print("Firefox starting test ...")
    firefox = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                               desired_capabilities=firefox_capabilities,
                               seleniumwire_options=options)
    firefox.get('https://www.google.com')
    print('Firefox', firefox.title)
    for request in firefox.requests:
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )
    time.sleep(15)
    firefox.quit()


def test_chrome():
    print("Chrome starting test ...")
    chrome = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                              desired_capabilities=chrome_capabilities,
                              seleniumwire_options=options)
    chrome.get('https://www.google.com')
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

def test_opera():
    print("Opera starting test ...")
    opera = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),
                              desired_capabilities=opera_capabilities,
                              seleniumwire_options=options)
    opera.get('https://www.google.com')
    print('opera', opera.title)
    for request in opera.requests:
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )
    time.sleep(15)
    opera.quit()


if __name__ == "__main__":
    # test_chrome()
    # test_firefox()
    test_opera()
