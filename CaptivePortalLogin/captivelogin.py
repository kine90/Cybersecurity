import time
import os
from datetime import datetime
from xmlrpc.client import Boolean
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def set_chrome() -> Options:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.accept_insecure_certs = True
        chrome_options.add_argument('--allow-insecure-localhost')
        chrome_options.add_argument("--ssl-protocol=any")
        chrome_options.add_argument("--window-size=1920,1080")
#        chrome_options.add_argument("enable-automation")
#        chrome_options.add_argument("--disable-extensions")
#        chrome_options.add_argument("--dns-prefetch-disable")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return chrome_options

def check_connectivity(hostname = "8.8.8.8") -> Boolean:
#    print("Checking Internet connectivity: ", end = " ")
    response = os.system("ping -c 1 " + hostname + " > /dev/null")
    connected = False
    #give ping time to complete
    time.sleep(5)
    #and then check the response...
    if response == 0:
#        print("Internet is be available!")
        connected = True
    else:
#        print("Ping fails, Internet is down.")
        connected = False
    return connected



def captive_login():
    # datetime object containing current date and time
    testpage = "https://www.google.com/"
    hostname = "8.8.8.8" #example

    if not (check_connectivity(hostname)):
        print("Internet down, proceeding...")

        driver = webdriver.Chrome(options=set_chrome())
#        print("driver loaded")

        driver.get(testpage)
        time.sleep(10)
#        print("landed in...")
#        print(driver.title)
        found = False
#        print("Entering loop")
        for window_handle in driver.window_handles:
            driver.switch_to.window(window_handle)
            print(driver.title)
            if driver.title == "Hotspot portal":
                found = True
                try:
                    driver.find_element(By.ID,'tos').click()
                    driver.find_element(By.CLASS_NAME,'unifiPortalMainButton').click()
                    print("Captive Login Done!")
                except:
                    print("Error - interacting with the Portal")
                break
        if not (found): print("Error - Can´t find Captive Portal window")
        driver.close()
    return

if __name__ == "__main__":
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n\nSelenium Login on ", dt_string)
    captive_login()
    exit()