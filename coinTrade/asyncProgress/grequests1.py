import grequests
import requests



import grequests

req_list = []
proxy = {'http': 'http://127.0.0.1:33210', 'https': 'http://127.0.0.1:33210'}

def initial



grequests
req_list.append(grequests.get('https://fapi.binance.com/fapi/v1/continuousKlines?pair=BTCUSDT&contractTyp=PERPETUAL&interval=1h&limit=1500', proxies=proxy))
req_list.append(grequests.get('https://fapi.binance.com/fapi/v1/continuousKlines?pair=BTCUSDT&contractType=PERPETUAL&interval=1h&limit=1500', proxies=proxy))
req_list.append(grequests.get('https://fapi.binance.com/fapi/v1/continuousKlines?pair=BTCUSDT&contractType=PERPETUAL&interval=1h&limit=1500', proxies=proxy))

res_list = grequests.map(req_list)    # 并行发送，等最后一个运行完后返回
print(res_list[2].text)  # 打印第一个请求的响应文本


if __name__ == '__main__':
        pass