import os
from multiprocessing import Process

class SubProcess(Process):
    def __init__(self, name):
        super(SubProcess, self).__init__()
        self.name = name
    def run(self):
      print ('子进程id: %s, with %s' % (os.getpid(), self.name))
if __name__=='__main__':
    print('父进程id: %s' % os.getpid())
    p = SubProcess('test')
    p.start()
