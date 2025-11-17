import requests
import socket

async def get_ip_async(api_url:str="http://ip-api.com/json"):
    r = requests.get(api_url)
    j = r.json()
    print(j)
    return j["query"], j['country']
 
async def get_lan_ip_async():
    lan_ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        lan_ip = s.getsockname()[0]
    finally:
        s.close()
    return lan_ip