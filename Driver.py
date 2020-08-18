from selenium import webdriver

Instance = None

def Initialize():
    global Instance
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    Instance = webdriver.Chrome(chrome_options=chrome_options)
    return Instance

def CloseDriver():
    global Instance
    Instance.quit()