import csv
import requests
from web3 import Web3
from concurrent.futures import ThreadPoolExecutor
import random
import string

# 生成随机的session ID
session = ''.join(random.choices(string.digits + string.ascii_letters, k=10))

# 读取钱包地址
with open('wallet.csv', 'r') as file:
    reader = csv.reader(file)
    wallets = [row[0] for row in reader]

# NST Proxy信息
nstproxy_Channel = "87448EEA"
nstproxy_Password = "GS8"
nstproxy = f"http://{nstproxy_Channel}-residential-country_ANY-r_5m-s_{session}:{nstproxy_Password}@gw-us.nstproxy.com:24125"

# 代理设置
proxies = {
    "http": nstproxy,
    "https": nstproxy
}

# 请求的URL
url = 'https://claims-api.lavanet.xyz/check-eligibility'

def check_eligibility(wallet_address):
    try:
        # 请求数据
        data = {
            "ethAddress": wallet_address
        }

        # 发送POST请求
        response = requests.post(url, json=data, proxies=proxies)
        result = response.json()

        # 实时打印结果
        print(f"Address: {wallet_address}, Response: {result}")
        return result
    except Exception as e:
        print(f"Error processing wallet address {wallet_address}: {e}")
        return None

# 使用并行处理
with ThreadPoolExecutor(max_workers=10) as executor:
    list(executor.map(check_eligibility, wallets))
