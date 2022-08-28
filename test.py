from selenium import webdriver


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--lang=de")
# firefox_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--lang=de")

chrome = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          options=chrome_options)

# firefox = webdriver.Remote(
#           command_executor='http://localhost:4444/wd/hub',
#           # options=firefox_options
# )

chrome.get('https://www.google.com')
print(chrome.title)

# firefox.get('https://www.google.com')
# print(firefox.title)

chrome.quit()
# firefox.quit()