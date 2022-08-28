from seleniumwire import webdriver

HOST = '127.0.0.1'

options = {
    'addr': HOST
}
def test_firefox():
    firefox = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST), seleniumwire_options=options)
    firefox.get('https://www.google.com')
    print('Firefox', firefox.title)
    for request in firefox.requests:
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )
    firefox.quit()


def test_chrome():
    chrome = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST), seleniumwire_options=options)
    chrome.get('https://www.google.com')
    print('chrome', chrome.title)
    for request in chrome.requests:
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )
    chrome.quit()


if __name__ == "__main__":
    test_firefox()
    test_chrome()
