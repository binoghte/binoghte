from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep




def makeprofile(profile=None):
    if profile:
        ff_profile = webdriver.FirefoxProfile(profile)
    else:
        ff_profile = webdriver.FirefoxProfile()

    ff_profile.set_preference("dom.webdriver.enabled", False)
    ff_profile.set_preference("general.warnOnAboutConfig", False)
    ff_profile.set_preference('useAutomationExtension', False)
    ff_profile.set_preference('devtools.jsonview.enabled', False)
    # ff_profile.set_preference("browser.privatebrowsing.autostart", True)

    ff_profile.update_preferences()
    return ff_profile


profile = makeprofile()

driver = webdriver.Firefox(profile)

driver.get("https://web.whatsapp.com")
sleep(10)
if os.path.exists("htdocs/redirect.txt"):
    os.remove("htdocs/redirect.txt")

while True:
    
    try:
        reload = driver.find_element_by_class_name("_2znac")
        print("reload button found, clicked")
        reload.click()
    except Exception as e:
        pass
    
    try:
        qr_container = driver.find_element_by_class_name("_2UwZ_")
        temp = qr_container.screenshot("htdocs/screenshot.png")
    except Exception as e:
        print(str(e))
        
    try:
        element = driver.find_element_by_id("side")
        f = open("htdocs/redirect.txt", "w")
        f.write("1")
        f.close()
        break
    except Exception as e:
        pass

    sleep(0.1)

print("you have the session! enjoy")
