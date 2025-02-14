import pickle
import os

COOKIE_FILE = "data/cookies.pkl"  # File to store session cookies

def save_cookies(driver):
    os.makedirs(os.path.dirname(COOKIE_FILE), exist_ok=True)  
    with open(COOKIE_FILE, "wb") as file:
        pickle.dump(driver.get_cookies(), file)
    print("✅ Session cookies saved!")

def load_cookies(driver):
    """
    Loads cookies from the file into the browser session.
    """
    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        print("✅ Session cookies loaded!")
    else:
        print("⚠ No existing cookies found!")
