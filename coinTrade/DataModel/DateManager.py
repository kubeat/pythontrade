import time
class MyDate(object):

    def __init__(self):
        pass
    #获取当前时间的毫秒
    def getCurMillSecond(self):
        curMillSecond = int(time.time() * 1000)
        return curMillSecond
    #获取当前时间对应的整点时间戳,addSecond,矫正时间,>0表示加多少秒，<0表示减去多少秒,默认是1小时
    def getWholeTimeBarMillSecond(self,timeBar,addSecond = 0):
        timeBarLower = timeBar.lower()
        afterAddMillSecond = self.getCurMillSecond()+addSecond*1000
        subMillSecond = afterAddMillSecond%(60*60*1000)
        if timeBarLower == '4h':
            subMillSecond = afterAddMillSecond%(240*60*1000)
        elif timeBarLower == '2h':
            subMillSecond = afterAddMillSecond%(120*60*1000)
        elif timeBarLower == '30m':
            subMillSecond = afterAddMillSecond % (30 * 60 * 1000)
        elif timeBarLower == '15m':
            subMillSecond = afterAddMillSecond % (15 * 60 * 1000)
        return (afterAddMillSecond-subMillSecond)

    def getDateStringByMillSecond(self,millSecond):
       return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(millSecond/1000))