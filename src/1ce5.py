from util import *
from const import const

# 进入ce5界面
def intoCe5():
    # 返回主页面
    const.backMainProcess()
    # 进入ce5界面
    x, y = const.picLoop(const.publicPath() + 'bmp/into.jpg')
    util.click(x, y)
    x, y = const.picLoop(const.publicPath() + 'bmp/collection.jpg')
    util.click(x, y)
    x, y = const.picLoop(const.publicPath() + 'bmp/ce.jpg')
    util.click(x, y)

def main():
    time.sleep(2)
    print('ce5脚本开始')

    # 进入ce5界面
    intoCe5()

    # 点击ce5
    x, y = const.picLoop(const.publicPath() + 'bmp/ce5.jpg')
    util.click(x, y)

    while True:
        const.anchorProcess()
