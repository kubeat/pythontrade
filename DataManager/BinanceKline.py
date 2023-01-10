import time
import asyncio
import ccxt.async_support as ccxt
import os
import ccxt

binance = ccxt.binance()
result = binance.describe()
print(result)
# binance.proxies
# for name, value in os.environ.items():
#      print(name+':',value)

# proxys = {}
# for name, value in os.environ.items():
#     name = name.lower()
#     if value and name[-6:].lower() == '_proxy':
#         proxys[name[:-6]] = value
#
# binance.proxies = proxys

    # binance.proxies = {'http': 'http://127.0.0.1:33210', 'https': 'http://127.0.0.1:33210'}
    # if value and name[-6:].lower() == '_proxy':
    #     print(name+':'+value)
# for symbol in dir(binance):
#     print(symbol)

# 获取交易对
# exchangeInfo = binance.fapiPublicGetExchangeInfo()
# tradesymbols = exchangeInfo['symbols']
# listSymbol = []
# for item in tradesymbols:
#     value = item.get('symbol', None)
#     valuelast4 = value[-4:]
#     if valuelast4 == 'USDT':
#         listSymbol.append(value)

'''
symbol:要下载的k线标识
from_time:开始时间
end_time:结束时间
time_bar:时间粒度（1h,2h,4h,1D,1W,1M,1Y）
'''


# def download_kline(symbol, from_time, end_time, time_bar):
#     while True:
#         print('当前正在下载' + symbol + ':');
#         list_data = binance.fetch_ohlcv(symbol,'1h',None,3)
#         if list_data:
#             return list_data
#         time.sleep(1)
#
#
# for symbol_index in listSymbol:
#     if symbol_index:
#        list_data =  download_kline(symbol_index, 0, 0, '1h')
#        if list_data:
#            ll_time = int(list_data[len(list_data)-1][0])
#            tre_timeArray = time.localtime(ll_time / 1000)
#            tre_otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", tre_timeArray)
#            print('tre_otherStyleTime', tre_otherStyleTime)
#        print(list_data)


# def omit(d, *args):
#     if isinstance(d, dict):
#         result = d.copy()
#         for arg in args:
#             if type(arg) is list:
#                 for key in arg:
#                     if key in result:
#                         del result[key]
#             else:
#                 if arg in result:
#                     del result[arg]
#         return result
#     return d
#
# omit({'key1':'value1','key2':'value2'},'key1')