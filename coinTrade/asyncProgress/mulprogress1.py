import os
import time
import random
from multiprocessing import Pool

def run(name):
    print('子进程id：%s,witn %s' % (os.getpid(), name))
    time.sleep((random.random()))
if __name__=='__main__':
    print('父进程id: %s' % os.getpid())
    p=Pool()                           #创建进程池，它将使用 Pool 类执行提交给它的任务
    for i in range(5):
    # 并没有启动5个子进程，而是只启动了2个子进程。因为这个进程池中的进程数量默认等于 CPU的数量
        p.apply_async(run,args=(i,))    #并发处理目标函数
    p.close()
    p.join()
    print('All done')
