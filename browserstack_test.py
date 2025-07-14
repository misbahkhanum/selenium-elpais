"""
browserstack_test.py  – launch 5 sessions (Chrome, Firefox, Edge, Safari, iPhone)
Works with Selenium 4.14+  ✔
Edit USERNAME and ACCESS_KEY, then:  python browserstack_test.py
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # we’ll reuse ChromeOptions for every session
import time, json

USERNAME   = "misbahkhanum_76ruTj"        #  ← replace
ACCESS_KEY = "ycWaGBebKEphTpQmWEGX"      #  ← replace
URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# ── five target environments ────────────────────────────────────────────────────
caps_list = [
    # 1 Chrome on Windows 11
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "platformName": "Windows 11",
        "bstack:options": {"sessionName": "Chrome Win11", "buildName": "ElPais build"}
    },
    # 2 Firefox on Windows 10
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "platformName": "Windows 10",
        "bstack:options": {"sessionName": "Firefox Win10", "buildName": "ElPais build"}
    },
    # 3 Edge on Windows 11
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "platformName": "Windows 11",
        "bstack:options": {"sessionName": "Edge Win11", "buildName": "ElPais build"}
    },
    # 4 Safari on macOS Monterey
    {
       "browser": "Safari",
       "browser_version": "15.0",
       "bstack:options":{
           "os": "OS X",
           "osVersion": "Monterey",
           "sessionName": "Safari Monterey test",   #optional
           "buildName": "ElPais Assignment Build"   #optional
       }
    },
   
    # 5 Safari on iPhone 14 (real device)
    {
        "browserName": "Safari",
        "platformName": "iOS",
        "bstack:options": {
            "deviceName": "iPhone 14",
            "osVersion": "16",
            "realMobile": "true",
            "sessionName": "iPhone 14",
            "buildName": "ElPais build"
        }
    }
]

def make_options(cap_dict: dict) -> Options:
    """Return an Options object whose capabilities equal cap_dict"""
    opts = Options()
    # remove any existing keys so we can set our own cleanly
    for key in list(opts.capabilities.keys()):
        opts.capabilities.pop(key, None)
    # copy every key from cap_dict into the options object
    for k, v in cap_dict.items():
        opts.set_capability(k, v)
    return opts

def run_single_session(caps: dict):
    name = caps["bstack:options"]["sessionName"]
    print(f"🚀 Starting session → {name}")
    opts = make_options(caps)
    driver = webdriver.Remote(command_executor=URL, options=opts)
    try:
        driver.get("https://elpais.com/opinion/")
        time.sleep(4)
        assert "Opinión" in driver.page_source
        print(f"✅ {name} passed")
    except Exception as e:
        print(f"❌ {name} failed – {e}")
    finally:
        driver.quit()

# ── run all five sessions sequentially (safe & simple) ─────────────────────────
for caps in caps_list:
    run_single_session(caps)
