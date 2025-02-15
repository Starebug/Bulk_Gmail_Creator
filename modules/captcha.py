import requests
import time
import config

API_KEY = config.captcha_api_key

def solve_captcha(site_key, url):
    response = requests.get("http://2captcha.com/in.php", params={
        'key': API_KEY,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': url
    })
    captcha_id = response.text.split('|')[1]
    
    for _ in range(20):
        time.sleep(5)
        res = requests.get("http://2captcha.com/res.php", params={
            'key': API_KEY,
            'action': 'get',
            'id': captcha_id
        })
        if "CAPCHA_NOT_READY" not in res.text:
            token = res.text.split('|')[1]
            return token
    raise Exception("CAPTCHA solving failed")
