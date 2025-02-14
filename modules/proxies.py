import config  
    
proxy_username = config.proxy_username

proxy_password = config.proxy_password

proxy_domain = config.proxy_domain

proxy_port = config.proxy_port

def get_proxy():
    proxy_address = f"{proxy_username}:{proxy_password}@{proxy_domain}:{proxy_port}"
    return proxy_address