from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import random
import time
from selenium.common.exceptions import StaleElementReferenceException
import modules.delays as delays
import modules.phone as phone
import modules.fingerprint as fingerprint

driver = fingerprint.setup_driver()
driver.get("https://api64.ipify.org?format=json")
proxy_ip = driver.page_source
driver.get("https://accounts.google.com/signup")

def safe_click(select_object, retries=3, wait_time=0.5):
    for attempt in range(retries):
        try:
            driver.execute_script("arguments[0].click();",select_object)
            return True
        except StaleElementReferenceException:
            print(f"Stale element encountered, retrying... (attempt {attempt + 1} of {retries})")
            time.sleep(wait_time)
    raise Exception("Element remains stale after multiple attempts.")

def open_gmail_signup():
    WebDriverWait(driver,15).until(
        EC.element_to_be_clickable((By.NAME,'firstName'))
    )
    select_object = driver.find_element(By.NAME,'firstName')
    driver.execute_script("arguments[0].click();",select_object)
    select_object.send_keys("tech")
    WebDriverWait(driver,15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[jsname='LgbsSe']"))
    )
    select_object = driver.find_element(By.CSS_SELECTOR, "button[jsname='LgbsSe']")
    delays.human_like_delay()
    delays.human_like_move(550, 650, min_duration=1,max_duration=2)
    safe_click(select_object)
    time.sleep(1)
    WebDriverWait(driver,15).until(
        EC.visibility_of_element_located((By.CLASS_NAME,'gNnnTd'))
    )
    select_object = driver.find_elements(By.CLASS_NAME,'gNnnTd')
    select_1 = Select(select_object[0])
    select_1.select_by_value("1")
    
    select_2 = Select(select_object[1])
    select_2.select_by_value("1")

    WebDriverWait(driver,15).until(
        EC.visibility_of_element_located((By.CLASS_NAME,'whsOnd'))
    )
    select_object = driver.find_elements(By.CLASS_NAME,'whsOnd')
    select_object[0].send_keys('15')
    select_object[1].send_keys('1997')
    delays.human_like_delay()
    delays.human_like_move(550, 650, min_duration=1,max_duration=2)

    select_object = driver.find_element(By.CSS_SELECTOR, "button[jsname='LgbsSe']")
    safe_click(select_object)
    time.sleep(1)
    gmail_address = None
    try:   
        WebDriverWait(driver,1).until(
            EC.element_to_be_clickable((By.XPATH,
            "//div[@role='radio' and contains(., 'Create your own Gmail address')]"))
        )
        create_own_radio = driver.find_element(By.XPATH,
            "//div[@role='radio' and contains(., 'Create your own Gmail address')]")
        create_own_radio.click()
        WebDriverWait(driver,15).until(
            EC.element_to_be_clickable((By.CLASS_NAME,'whsOnd'))
            )
        select_object = driver.find_element(By.CLASS_NAME,'whsOnd')
        safe_click(select_object)
        select_object.send_keys('nuhjhfuiahndf')
        select_object = driver.find_element(By.CSS_SELECTOR, "button[jsname='LgbsSe']")
        safe_click(select_object)
        time.sleep(1)
        print(gmail_address)
    except TimeoutException:
        try:
            WebDriverWait(driver,15).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='radio']"))
            )
            select_object = driver.find_elements(By.XPATH, "//div[@role='radio']")
            num = random.randint(0,1)
            safe_click(select_object[num])
            WebDriverWait(driver,15).until(
                EC.element_to_be_clickable((By.CLASS_NAME,'dJVBl'))
            )
            select_object = driver.find_elements(By.CLASS_NAME,'dJVBl')
            num = random.randint(0,1)
            gmail_address = select_object[num].text
            select_object = driver.find_element(By.CSS_SELECTOR, "button[jsname='LgbsSe']")
            safe_click(select_object)
            time.sleep(1)
        except TimeoutException:
            print('Element not found')
            WebDriverWait(driver,15).until(
            EC.element_to_be_clickable((By.CLASS_NAME,'whsOnd'))
            )
            select_object = driver.find_element(By.CLASS_NAME,'whsOnd')
            safe_click(select_object)
            select_object.send_keys('nuhjhfuiahndf')
            select_object = driver.find_element(By.CSS_SELECTOR, "button[jsname='LgbsSe']")
            safe_click(select_object)
        print(gmail_address)
    delays.human_like_delay()
    delays.human_like_move(550, 650, min_duration=1,max_duration=2)
    WebDriverWait(driver,15).until(
        EC.element_to_be_clickable((By.NAME,'Passwd'))
    )
    select_object = driver.find_element(By.NAME,'Passwd')
    safe_click(select_object)
    select_object.send_keys('bshd f401210054')
    delays.human_like_delay()
    delays.human_like_move(55, 65, min_duration=1,max_duration=2)
    

    WebDriverWait(driver,15).until(
        EC.element_to_be_clickable((By.NAME,'PasswdAgain'))
    )
    select_object = driver.find_element(By.NAME,'PasswdAgain')
    safe_click(select_object)
    select_object.send_keys('bshd f401210054')
    delays.human_like_delay()
    delays.human_like_move(100, 250, min_duration=1,max_duration=2)
    try:
        WebDriverWait(driver,15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jscontroller='soHxf']"))
        )
        select_object = driver.find_element(By.CSS_SELECTOR, "button[jscontroller='soHxf']")
        safe_click(select_object)
    except TimeoutException:
        try:
            WebDriverWait(driver,15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jsname='LgbsSe']"))
            )
            select_object = driver.find_element(By.CSS_SELECTOR, "button[jsname='LgbsSe']")
            safe_click(select_object)
        except Exception as e:
            print(e)
            driver.quit()
    phone_no, request_id = None, None
    country_codes ={
        "UK": "gb",
        "US": "us",
        "NL": "nl"
    }

    for country,code in country_codes.items():
        phone_accepted = False 
        for attempt in range(1, 3):  
            try:
                phone_no, request_id = phone.get_phone_number(country)
                if not phone_no:
                    print(f"Empty phone number returned for {country} on attempt {attempt}.")
                    continue

                print(f"✅ Got phone number for {country} on attempt {attempt}: {phone_no}, Request ID: {request_id}")

                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.ID, "countryList"))
                )
                select_object = driver.find_element(By.ID, "countryList")
                safe_click(select_object)
                # WebDriverWait(driver, 15).until(
                #     EC.visibility_of_element_located((By.XPATH, f"//li[@data-value='{code}']"))
                # )
                print(code)
                select_object = driver.find_element(By.XPATH, f"//li[@data-value='{code}']")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_object)
                safe_click(select_object)

                WebDriverWait(driver, 15).until(
                    EC.visibility_of_element_located((By.ID, 'phoneNumberId'))
                )
                select_object = driver.find_element(By.ID, 'phoneNumberId')
                select_object.send_keys(phone_no)
                print("✅ Phone number entered successfully!")

                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jsname='LgbsSe']"))
                )
                select_object = driver.find_element(By.CSS_SELECTOR,"button[jsname='LgbsSe']")
                delays.human_like_delay()
                delays.human_like_move(300, 400, min_duration=1, max_duration=2)

                safe_click(select_object)

                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'whsOnd'))
                )
                select_object = driver.find_element(By.CLASS_NAME, 'whsOnd')
                safe_click(select_object)
                for _ in range(3):
                 try:
                    phone_otp = phone.fetch_sms_with_retry(request_id)
                    if not phone_otp:
                        raise Exception("OTP not received") 
                    select_object.send_keys(phone_otp)
                    phone.close_order(request_id)
                    print(phone_otp)
                    break
                 except Exception as e:
                    print("Error fetching the OTP")
                    select_object = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Get new code']]"))
                    )
                    safe_click(select_object)
                    time.sleep(1)
                    continue
                if not phone_otp:
                    phone.close_order(request_id)
                    driver.quit()
                    return
                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jsname='LgbsSe']"))
                )
                select_object = driver.find_element(By.CSS_SELECTOR, "button[jsname='LgbsSe']")
                safe_click(select_object)
                time.sleep(1)
                phone_accepted = True
                print(f"✅ Phone number process succeeded for {country} on attempt {attempt}.")
                phone.close_order(request_id)
                try:
                    select_object = WebDriverWait(driver, 15).until(
                                    EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Skip']]"))
                                )
                except  TimeoutException:
                    print('Skip not Present')
                select_object = WebDriverWait(driver, 15).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Next']]")))
                
                timestamp = datetime.now().timestamp()
                return gmail_address, phone_no, proxy_ip, timestamp
    

            except TimeoutException:
                print(f"⚠ Timeout: Could not locate a required element for {country} on attempt {attempt}.")
                try:
                    WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, 'VfPpkd-fmcmS-wGMbrd'))
                    )
                    select_object = driver.find_element(By.CLASS_NAME, 'VfPpkd-fmcmS-wGMbrd')
                    select_object.clear()
                    phone.close_order(request_id)
                    continue
                except Exception as clear_error:
                    driver.quit()
                    phone.close_order(request_id)
                    print(f"Error clearing input field: {clear_error}")
                    return

            except Exception as e:
                phone.close_order(request_id)
                print(f"❌ Failed to process for {country} on attempt {attempt}: {e}")

    print("Page Title:", driver.title)
    driver.quit() 


accounts_created = 0
accounts_needed = 10
MAX_RETRIES = 5
while accounts_created < accounts_needed:
    for attempt in range(MAX_RETRIES):
        try:
            print(f"🔄 Signup attempt {attempt + 1} for account {accounts_created + 1}")
            gmail_address, password, phone_no, proxy_ip, timestamp, = open_gmail_signup()
            break
        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed: {e}")
            time.sleep(random.uniform(10, 30))
    else:
        print("🚫 Failed to create account after maximum retries. Skipping...")
        continue

    # with open(csv_file_path, "a", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow([email, password])
    
    accounts_created += 1
    print(f"✅ Total accounts created: {accounts_created}/{accounts_needed}")

print("🚀 Completed generating Gmail accounts!")

