from util import *
from const import const

def main():
    const.backMainProcess()
    print('按任意键结束程序')
    input()
    

if __name__ == '__main__':
    print('adb初始化开始')
    util.adb('kill-server')
    util.adb('connect 127.0.0.1:7555')
    main()
    
