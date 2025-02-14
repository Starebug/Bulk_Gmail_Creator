from dotenv import load_dotenv
import os

load_dotenv()

captcha_api_key = os.getenv("2CAPTCHA_API_KEY")
sms_api_key = os.getenv("SMS_ACTIVATE_KEY")
proxy_username = os.getenv("PROXY_USERNAME")
proxy_password = os.getenv("PROXY_PASSWORD")
proxy_domain = os.getenv("PROXY_DOMAIN")
proxy_port = os.getenv("PROXY_PORT")

print("2Captcha API Key:", captcha_api_key)
print("SMS Activate API Key:", sms_api_key)
print(f"Proxy: {proxy_username}:{proxy_password}@{proxy_domain}:{proxy_port}")
