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

    # Remove the navigator.webdriver flag to help avoid detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver



# # modules/phone.py
# import requests
# import time
# import re
# import config

# # Use the SMS API key from config
# SMS_API_KEY = config.sms_api_key

# def get_phone_number(country="US"):
#     """
#     Requests a phone number from JuicySMS.com.
#     Expected response format (example): "PREFIX_orderid_PHONE_someOtherData"
#     Adjust the parsing logic based on the actual format.
#     """
#     url = "https://juicysms.com/api/makeorder"
#     params = {
#         'key': SMS_API_KEY,         # Replace with your actual API key
#         'serviceId': '1',            # Replace with the correct service id for Google
#         'country': country                 # Use the provided country or "NL" if needed
#     }
    
#     response = requests.get(url, params=params)
#     raw_response = response.text.strip()
#     # Optionally clean the string from any non-printable characters:
#     raw_response = re.sub(r'[^\x20-\x7E]', '', raw_response)
#     print(f"Raw response for {country}: {raw_response}")
    
#     # Split the response by underscores (adjust the delimiter if needed)
#     data = raw_response.split("_")
#     print(f"Data split: {data} (length: {len(data)})")
    
#     # Check that we have the expected number of parts.
#     # For example, if we expect at least 5 parts: 
#     if len(data) < 5:
#         raise Exception(f"Unexpected response format: {raw_response}")
    
#     # Assuming that data[2] is the order id and data[4] is the phone number:
#     order_id = data[2]
#     phone_no = data[4]
#     print("Order ID:", order_id)
#     print("Number:", phone_no)
#     return phone_no, order_id

# def get_sms(order_id):
#     """
#     Retrieves the SMS message for the given order_id.
#     Expected response format (example): "STATUS_OK:OTP_CODE"
#     """
#     url = "https://juicysms.com/api/getsms"
#     params = {
#         'key': SMS_API_KEY,
#         'order_id': order_id
#     }
#     response = requests.get(url, params=params)
#     # Return the stripped text response
#     return response.text.strip()

# def fetch_sms_with_retry(order_id, max_retries=10, delay=5):
#     """
#     Polls the SMS endpoint until the OTP is available.
#     If the response is "waiting", it continues to retry.
#     """
#     retries = 0
#     while retries < max_retries:
#         sms_response = get_sms(order_id)
#         print(f"Attempt {retries + 1}: {sms_response}")
#         # Check if the response indicates that the SMS is ready.
#         # Adjust the condition according to the actual API response.
#         if not sms_response.lower() == "waiting":
#             return sms_response  # Return the OTP or full SMS content
#         print(f"Waiting for SMS... (Retry {retries + 1}/{max_retries})")
#         time.sleep(delay)
#         retries += 1
#     return "Failed to retrieve SMS after max retries."

# def close_order(id):
#     """
#     Cancels the order (if needed).
#     """
#     url = "https://juicysms.com/api/cancelorder"
#     params = {
#         'key': SMS_API_KEY,  # Replace with the correct service id if required
#         'orderId': id,
#     }
#     response = requests.get(url, params=params)
#     print("Cancel order response:", response.text)

# # def get_phone_number(country="ID"):
# #     """
# #     Request a phone number from SMSPVA.com for the specified country.
# #     Expected response format: "ACCESS_NUMBER:PHONE_NUMBER:REQUEST_ID"
# #     """
# #     url = "https://api.sms-pva.com/stubs/handler_api.php"  
# #     params = {
# #         "api_key": SMS_API_KEY,  
# #         "action": "getNumber",
# #         "service": "go",  
# #         "country": country,
# #     }
# #     response = requests.get(url, params=params)
    
# #     raw_response = response.text.strip()
# #     raw_response = response.sub(r'[^\x20-\x7E]', '', raw_response)
# #     print(f"Raw response for {country}: {raw_response}")
    
# #     data = raw_response.split(":")
# #     print(f"Data split: {data} (length: {len(data)})")
    
# #     if data[0] != "ACCESS_NUMBER":
# #         raise Exception(f"Failed to get phone number: {raw_response}")
# #     if len(data) < 3:
# #         raise Exception(f"Unexpected response format: {raw_response}")
    
# #     phone_number = data[1]
# #     request_id = data[2]
# #     return phone_number, request_id
# order_id = 5618422
# fetch_sms_with_retry(order_id)

# modules/phone.py
# import requests
# import time
# import config
# SMS_API_KEY = config.sms_api_key

# def get_phone_number(country="ID"):
#     response = requests.get("https://juicysms.com/api/makeorder?key=APIKEY&serviceId=SERVICEID&country=NL", params={
#         'api_key': SMS_API_KEY,
#         'action': 'getNumber',
#         'service': 'go', 
#         'country': country
#     })

#     response = response.split("_")
#     order_id = response[2]
#     phone_no = response[4]
#     print("Order ID:", order_id)
#     print("Number:", phone_no)
#     return phone_no, order_id
# def get_sms(id):
#     retries = 0
#     response = requests.get("https://juicysms.com/api/getsms",params={
#         'key': SMS_API_KEY,
#         'order_id': id
#     })
#     return response
    

# def close_order(orderId):  
#     response = requests.get("https://juicysms.com/api/cancelorder", params={
#         'key': SMS_API_KEY,
#         'orderId': orderId
#     })


# def fetch_sms_with_retry(order_id, max_retries=10, delay=5):
#     """
#     Fetches the SMS with retries until it's available.
#     """
#     retries = 0
#     while retries < max_retries:
#         response = get_sms(order_id)  
#         # if response != "waiting":
#         print(response)
#         #     return response  
#         print(f"Waiting for SMS... (Retry {retries + 1}/{max_retries})")
#         time.sleep(delay)  # Wait before retrying
#         retries += 1
#     return "Failed to retrieve SMS after max retries."


# # def get_phone_number(country="ID"):
# #     """
# #     Request a phone number from SMSPVA.com for the specified country.
# #     Expected response format: "ACCESS_NUMBER:PHONE_NUMBER:REQUEST_ID"
# #     """
# #     url = "https://api.sms-pva.com/stubs/handler_api.php"  
# #     params = {
# #         "api_key": SMS_API_KEY,  
# #         "action": "getNumber",
# #         "service": "go",  
# #         "country": country,
# #     }
# #     response = requests.get(url, params=params)
    
# #     raw_response = response.text.strip()
# #     raw_response = response.sub(r'[^\x20-\x7E]', '', raw_response)
# #     print(f"Raw response for {country}: {raw_response}")
    
# #     data = raw_response.split(":")
# #     print(f"Data split: {data} (length: {len(data)})")
    
# #     if data[0] != "ACCESS_NUMBER":
# #         raise Exception(f"Failed to get phone number: {raw_response}")
# #     if len(data) < 3:
# #         raise Exception(f"Unexpected response format: {raw_response}")
    
# #     phone_number = data[1]
# #     request_id = data[2]
# #     return phone_number, request_id
# request_id = 55619070
# fetch_sms_with_retry(request_id)
