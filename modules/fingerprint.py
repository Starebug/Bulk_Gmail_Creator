from fake_useragent import UserAgent
import random
from seleniumwire import webdriver  #   
import modules.proxies as proxies
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_random_user_agent():
    """
    Returns a randomly generated User-Agent string.
    """
    ua = UserAgent()
    return ua.random

def get_fingerprint_options():
    options = webdriver.ChromeOptions()

    # Generate a random user-agent
    user_agent = get_random_user_agent()
    options.add_argument(f"user-agent={user_agent}")

    # Stealth mode to reduce automation detection
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors=yes")
    # Set a realistic random window size
    width = random.randint(1024, 1920)
    height = random.randint(720, 1080)
    options.add_argument(f"--window-size={width},{height}")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    return options

def setup_driver():
    proxy_address = proxies.get_proxy()

    seleniumwire_options = {
        'proxy': {
            'http': f'http://{proxy_address}',
            'https': f'https://{proxy_address}',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }

    chrome_options = get_fingerprint_options()

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service=service,
        options=chrome_options,
        seleniumwire_options=seleniumwire_options
    )

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver
