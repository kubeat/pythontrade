import asyncio
import pandas as  pd
import grequests
import time
import shelve
from DataModel.SQLManager import Database

dbManger = Database(host="127.0.0.1", port=3306, user='root', password='123456', db='klinedata', charset='utf8mb4')

req_list = [];

def initli(contex):
    passs

def hanle_data():
    pass

if __name__ == '__main__':
    while True:
        time.sleep(1)
        print('test')