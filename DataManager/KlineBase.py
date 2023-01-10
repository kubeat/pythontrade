class KlineRequestBase(object):
    def __init__(self):
        pass

    """
    要下载的k线，from_time,开始时间,end_time，结束时间，time_frame时间粒度
    """

    def download_kline(self, symbol, from_time, end_time, time_frame):
        pass


# if __name__ == '__main__':
#     second: int = 0
#     while True:
#         second += 1
#         time.sleep(1)
#         print(second)
if __name__ == '__main__':
    test_int = 7
    test_Chu = 4
    test_c = test_int//test_Chu
    test_yu = test_int-test_c*test_Chu
    print('({0},{1})整除：'.format(test_int,test_Chu)+str(test_c)+' 结果:'+str(test_yu))

    test_int = 7
    test_Chu = -4
    test_c = test_int//test_Chu
    test_yu = test_int-test_c*test_Chu
    print('({0},{1})整除：'.format(test_int,test_Chu)+str(test_c)+' 结果:'+str(test_yu))


    test_int = -7
    test_Chu = 4
    test_c = test_int//test_Chu
    test_yu = test_int-test_c*test_Chu
    print('({0},{1})整除：'.format(test_int,test_Chu)+str(test_c)+' 结果:'+str(test_yu))

    test_int = -7
    test_Chu = -4
    test_c = test_int//test_Chu
    test_yu = test_int-test_c*test_Chu
    print('({0},{1})整除：'.format(test_int,test_Chu)+str(test_c)+' 结果:'+str(test_yu))