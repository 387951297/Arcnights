from util import *
from const import const

# 进入ce5界面
def intoCe5():
    # 判断是否在ce5界面
    if util.isFindPic(const.publicPath() + 'ce5/ce5.jpg'):
        return
    # 返回主页面
    const.backMainProcess()
    # 进入ce5界面
    x, y = util.findPicLoop(const.publicPath() + 'bmp/into.jpg')
    pyautogui.click(x, y)
    x, y = util.findPicLoop(const.publicPath() + 'ce5/wuzi.jpg')
    pyautogui.click(x, y)
    x, y = util.findPicLoop(const.publicPath() + 'ce5/ce.jpg')
    pyautogui.click(x, y)

def main():
    time.sleep(2)
    print('ce5脚本开始')

    # 进入ce5界面
    intoCe5()

    # 点击ce5
    x, y = util.findPicLoop(const.publicPath() + 'ce5/ce5.jpg')
    pyautogui.click(x, y)
    time.sleep(.800)

    while True:
        const.anchorProcess()

if __name__ == '__main__':
    main()