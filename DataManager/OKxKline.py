import  requests
import pymysql
from threading import Timer
import time
from  DataModel.DateManager import MyDate
import pymysql
from DataModel.SQLManager import Database
import pandas as pd


#计时器类
class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)

def postRun():
     #获取行情
     path = './test.csv'
     # 读取csv文件
     df1 = pd.read_csv(path)
     dateTime = df1.iloc[0][0]
     strTime = MyDate().getDateStringByMillSecond(dateTime)

     httpUrl = "https://fapi.binance.com/fapi/v1/continuousKlines?pair=BTCUSDT&contractType=PERPETUAL&interval=1h&limit=1500"
     if dateTime > 0:
         httpUrl = httpUrl+"&endTime="+str(dateTime)


     proxy = {'http': 'http://127.0.0.1:33210', 'https': 'http://127.0.0.1:33210'}
    # klineGet = requests.get("https://www.okx.com/api/v5/market/candles?instId=BTC-USDT-SWAP&bar=1H",proxies=proxy)
     klineGet = requests.get("https://fapi.binance.com/fapi/v1/continuousKlines?pair=BTCUSDT&contractType=PERPETUAL&interval=1h&limit=1500", proxies=proxy)
     df = pd.read_json(klineGet.text)
     #df.to_csv(path,mode='a',index=None,columns=None,header=None)


t = RepeatingTimer(3.0, postRun)
t.start()

# proxy = {'http': 'http://127.0.0.1:33210', 'https': 'http://127.0.0.1:33210'}
# base_return = requests.get("https://www.okx.com/api/v5/public/instruments?instType=SWAP",proxies=proxy)
# print(base_return.text)

if __name__ == '__main__':
    pass