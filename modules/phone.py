# modules/phone.py
import requests
import time
import config
SMS_API_KEY = config.sms_api_key

def get_phone_number(country="US"):
    response = requests.get("https://juicysms.com/api/makeorder", params={
        'key': SMS_API_KEY,
        'serviceId': '1',
        'country': country
    })
    response = response.text.strip()
    print(response)
    response = response.split("_")
    order_id = response[2]
    phone_no = response[4]
    print("Order ID:", order_id)
    print("Number:", phone_no)
    return phone_no, order_id
def get_sms(id):
    retries = 0
    response = requests.get("https://juicysms.com/api/getsms",params={
        'key': SMS_API_KEY,
        'orderId': id
    })
    otp = response.text.strip()
    return otp
    

def close_order(orderId):  
    response = requests.get("https://juicysms.com/api/cancelorder", params={
        'key': SMS_API_KEY,
        'orderId': orderId
    })
    


def fetch_sms_with_retry(order_id, max_retries=10, delay=5):
    """
    Fetches the SMS with retries until it's available.
    """
    retries = 0
    prefix = "SUCCESS_G-"
    while retries < max_retries:
        response = get_sms(order_id)  
        print(response)
        if response.startswith(prefix):
            otp = response[len(prefix):].split()[0]
            print("Extracted OTP:", otp)
            return otp
        else:
            print("OTP not found.") 
            print(f"Waiting for SMS... (Retry {retries + 1}/{max_retries})")
            time.sleep(delay)  # Wait before retrying
        retries += 1
    return None

