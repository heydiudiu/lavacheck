evm地址查询
wallet.csv
evm地址一行一个
nstproxy代理
不用代理的话 就把这一行
response = requests.post(url, json=data, proxies=proxies)
换成response = requests.post(url, json=data)
