import config
import random
import time
import csv
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import modules.phone as phone
import modules.proxies as proxies
import modules.captcha as captcha
import modules.fingerprint as fingerprint
import modules.cookies as cookies
import modules.delays as delays

def open_gmail_signup():
    """
    Performs the entire Gmail signup process and returns the created email address and password.
    Raises an Exception if any step fails.
    """
    chrome_options = fingerprint.get_fingerprint_options()
    
    proxy_address = proxies.get_proxy() 
    chrome_options.add_argument(f'--proxy-server=http://{proxy_address}')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get("https://accounts.google.com/signup")
    delays.human_like_delay()
    
    driver.find_element(By.NAME, "firstName").send_keys("John")
    delays.human_like_delay()
    driver.find_element(By.NAME, "lastName").send_keys("Doe")
    delays.human_like_delay()
    username = f"john{random.randint(1000, 9999)}"
    driver.find_element(By.NAME, "Username").send_keys(username)
    delays.human_like_delay()
    password = "SecurePassword123!"  # Use a strong password generator in production
    driver.find_element(By.NAME, "Passwd").send_keys(password)
    delays.human_like_delay()
    driver.find_element(By.NAME, "ConfirmPasswd").send_keys(password)
    delays.human_like_delay()
    
    # 4. Click "Next" button using human-like mouse movement
    delays.human_like_move(500,600,min_duration=1,max_duration=2)
    delays.human_like_delay()
    
    country_codes = ["ID", "PH", "TH", "RU"]
    phone_number, request_id = None, None
    for country in country_codes:
        try:
            phone_number, request_id = phone.get_phone_number(country)
            print(f"✅ Successfully got phone number for {country}: {phone_number}, Request ID: {request_id}")
            break
        except Exception as e:
            print(f"❌ Failed to get phone number for {country}: {e}")
    if not phone_number:
        driver.quit()
        raise Exception("No available phone number from any country.")
    
    driver.find_element(By.NAME, "phoneNumberId").send_keys(phone_number)
    delays.human_like_delay()
    delays.human_like_move(550, 650, min_duration=1,max_duration=2)
    
    otp = phone.get_sms(request_id)
    driver.find_element(By.NAME, "code").send_keys(otp)
    delays.human_like_delay()
    driver.find_element(By.ID, "next").click()
    delays.human_like_delay(2, 4)
    
    # 8. Solve reCAPTCHA using 2Captcha API (if present)
    # Replace "6LfcU...(site key)" with the actual site key for the Gmail signup page.
    captcha_token = captcha.solve_captcha("6LfcU...(site key)", driver.current_url)
    driver.execute_script(
        f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_token}";'
    )
    delays.human_like_delay()
    driver.find_element(By.ID, "next").click()
    delays.human_like_delay()
    
    cookies.save_cookies(driver)
    
    email = username + "@gmail.com"
    print("✅ Gmail account created successfully:", email)
    
    driver.quit()
    return email, password, phone_number,

csv_file_path = "data/accounts.csv"
os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
if not os.path.exists(csv_file_path):
    with open(csv_file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Email", "Password"])

accounts_needed = 10
accounts_created = 0
MAX_RETRIES = 3

while accounts_created < accounts_needed:
    for attempt in range(MAX_RETRIES):
        try:
            print(f"🔄 Signup attempt {attempt + 1} for account {accounts_created + 1}")
            email, password = open_gmail_signup()
            break
        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed: {e}")
            time.sleep(random.uniform(10, 30))
    else:
        print("🚫 Failed to create account after maximum retries. Skipping...")
        continue

    with open(csv_file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([email, password])
    
    accounts_created += 1
    print(f"✅ Total accounts created: {accounts_created}/{accounts_needed}")

print("🚀 Completed generating Gmail accounts!")
