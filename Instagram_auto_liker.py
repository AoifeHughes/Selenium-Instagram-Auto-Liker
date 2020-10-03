from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():

    id = '{your_instagram_ID}'
    passd = '{your_instagram_password}'
    browser_locale = 'en'
    try:
        url = 'https://www.instagram.com/'
        targetURL = url+'{target_instagram_ID}'
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_argument("--lang={}".format(browser_locale))
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)

        # resize browser window to maximize_window
        driver.maximize_window()

        username = driver.find_element_by_name('username')
        username.send_keys(id)
        password = driver.find_element_by_name('password')
        password.send_keys(passd)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.get(targetURL)
        time.sleep(2)
        first_picture(driver)
        like_pic(driver)
        continue_liking(driver)
        # Close the tab/browser when done
    except BaseException:
        print("Driver error")


def first_picture(driver):
    time.sleep(0.5)
    pic = driver.find_element_by_class_name("_9AhH0")
    time.sleep(0.5)
    pic.click()   # clicks on the first picture


def next_picture(driver):
    time.sleep(0.5)
    nex = driver.find_element_by_xpath(
        '//a[@class=" _65Bje  coreSpriteRightPaginationArrow"]')
    return nex


def like_pic(driver):
    time.sleep(1)
    like = driver.find_element_by_xpath(
        '//div[@class="QBdPU "]/*[name()="span"]/*[name()="svg"][@aria-label="Like"]')
    time.sleep(1)
    # clicking the like button
    like.click()


def continue_liking(driver):
    while True:
        next_el = next_picture(driver)

        # if next button is there then
        if next_el != False:

            # click the next button
            next_el.click()
            time.sleep(1)

            # like the picture
            like_pic(driver)
        else:
            print("not found")
            break


main()
