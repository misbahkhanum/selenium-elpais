from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from threading import Thread
import time

USERNAME = "misbahkhanum_76ruTj"
ACCESS_KEY = "ycWaGBebKEphTpQmWEGX"

capabilities_list = [
    {
        "os": "Windows",
        "osVersion": "10",
        "browserName": "Chrome",
        "browserVersion": "latest"
    },
    {
        "os": "OS X",
        "osVersion": "Ventura",
        "browserName": "Safari",
        "browserVersion": "latest"
    },
    {
        "os": "Windows",
        "osVersion": "11",
        "browserName": "Firefox",
        "browserVersion": "latest"
    },
    {
        "deviceName": "Samsung Galaxy S22",
        "osVersion": "12.0",
        "browserName": "Chrome",
        "realMobile": "true"
    },
    {
        "deviceName": "iPhone 14",
        "osVersion": "16",
        "browserName": "Safari",
        "realMobile": "true"
    }
]

def run_browserstack_test(cap):
    try:
        caps = {
            "bstack:options": {
                "os": cap.get("os"),
                "osVersion": cap.get("osVersion"),
                "deviceName": cap.get("deviceName"),
                "realMobile": cap.get("realMobile"),
                "userName": USERNAME,
                "accessKey": ACCESS_KEY,
                "projectName": "ElPais Scraper",
                "buildName": "Assignment",
                "sessionName": cap.get("browserName")
            },
            "browserName": cap.get("browserName"),
            "browserVersion": cap.get("browserVersion")
        }

        driver = webdriver.Remote(
            command_executor="https://hub-cloud.browserstack.com/wd/hub",
            options=webdriver.ChromeOptions().set_capability("bstack:options", caps["bstack:options"])
        )

        driver.get("https://elpais.com/opinion/")
        time.sleep(2)
        print(f"[{cap.get('browserName')}] Title → {driver.title}")

        driver.quit()
    except Exception as e:
        print(f"❌ Error on {cap.get('browserName')}: {e}")

if __name__ == "__main__":
    threads = []
    for cap in capabilities_list:
        thread = Thread(target=run_browserstack_test, args=(cap,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("\n✅  All BrowserStack sessions finished.")
