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


# def get_phone_number(country="ID"):
#     """
#     Request a phone number from SMSPVA.com for the specified country.
#     Expected response format: "ACCESS_NUMBER:PHONE_NUMBER:REQUEST_ID"
#     """
#     url = "https://api.sms-pva.com/stubs/handler_api.php"  
#     params = {
#         "api_key": SMS_API_KEY,  
#         "action": "getNumber",
#         "service": "go",  
#         "country": country,
#     }
#     response = requests.get(url, params=params)
    
#     raw_response = response.text.strip()
#     raw_response = response.sub(r'[^\x20-\x7E]', '', raw_response)
#     print(f"Raw response for {country}: {raw_response}")
    
#     data = raw_response.split(":")
#     print(f"Data split: {data} (length: {len(data)})")
    
#     if data[0] != "ACCESS_NUMBER":
#         raise Exception(f"Failed to get phone number: {raw_response}")
#     if len(data) < 3:
#         raise Exception(f"Unexpected response format: {raw_response}")
    
#     phone_number = data[1]
#     request_id = data[2]
#     return phone_number, request_id