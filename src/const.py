from util import *


class Const:
    def __init__(self):
        pass

    # 获取根path
    def path(self):
        return './'

    # 图片资源path
    def publicPath(self):
        return self.path() + 'public/'

    # 临时path
    def tmpPath(self):
        return self.path() + 'tmp/'

    # 返回主页面
    def backMainProcess(self):
        if util.isFindPic(self.publicPath() + 'bmp/home.jpg', 0.8):
            x, y = util.findPic(self.publicPath() + 'bmp/home.jpg', 0.8)
            pyautogui.click(x, y)
            time.sleep(.500)
            x, y = util.findPic(self.publicPath() + 'bmp/home2.jpg')
            pyautogui.click(x, y)
            time.sleep(2.00)
        elif util.isFindPic(self.publicPath() + 'bmp/into.jpg'):
            return
        else:
            print('返回主页面失败')

        # 出击到结束的过程
    def anchorProcess(self):
        # 代理指挥
        if not util.isFindPic(const.publicPath() + 'bmp/is_agent.jpg'):
            x, y = util.findPicLoop(const.publicPath() + 'bmp/agent.jpg')
            pyautogui.click(x, y)
        x , y = util.findPicLoop(const.publicPath() + 'bmp/start.jpg')
        pyautogui.click(x, y)
        x , y = util.findPicLoop(const.publicPath() + 'bmp/operation_start.jpg')
        pyautogui.click(x, y)
        time.sleep(60.000)
        x , y = util.findPicLoop(const.publicPath() + 'bmp/end.jpg')
        time.sleep(3.000)
        pyautogui.click(x, y)
        util.findPicLoop(const.publicPath() + 'bmp/start.jpg')
        print('一把结束')

const = Const()
