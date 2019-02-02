import time
n = 5
while n > 0:
    strtime = '{0[3]:0>2}:{0[4]:0>2}:{0[5]:0>2}'.format(list(time.localtime()))
    print(strtime, end=" \r")
    time.sleep(1)
    n = n - 1
