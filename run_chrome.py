from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep


chrome_data_dir_path = "F:\\python lab\\selenium\\chrome_profiles\\Default"
def makeprofile_ch(data_dir = None):
    
    options = webdriver.ChromeOptions()
    capabilities = webdriver.DesiredCapabilities.CHROME

    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')

    options.add_argument('--no-sandbox')

    if data_dir:
        options.add_argument("user-data-dir={}".format(data_dir))

    
    return options, capabilities


options, desired = makeprofile_ch(chrome_data_dir_path)
driver = webdriver.Chrome(options=options, desired_capabilities=desired)


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
        pass
    
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
