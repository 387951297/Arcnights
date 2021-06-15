from util import *

class Const:
    def __init__(self):
        pass
        
    #获取根path
    def path(self):
        return './'

    #图片资源path
    def publicPath(self):
        return self.path() + 'public/'

    #临时path
    def tmpPath(self):
        return self.path() + 'tmp/'

    #返回主页面
    def backMainProcess(self):
        util.logOut(__file__,'backMainProcess 返回主页面开始')
        if util.isFindPic(self.publicPath() + 'bmp/home.jpg'):
            x, y = self.picLoop(self.publicPath() + 'bmp/home.jpg')
            util.click(x, y)
            x, y = self.picLoop(self.publicPath() + 'bmp/home2.jpg')
            util.click(x, y)
            self.picLoop(self.publicPath() + 'bmp/into.jpg')
        elif util.isFindPic(self.publicPath() + 'bmp/into.jpg'):
            util.logOut(__file__,'backMainProcess 返回主页面结束')
            return
        else:
            util.logOut(__file__,'backMainProcess 返回主页面结束 失败')

    # 重启
    def restartProcess(self):
        util.logOut(__file__,'restartProcess 重启脚本开始')
        util.adb('shell am force-stop com.hypergryph.arknights')
        util.adb('shell am start -n com.hypergryph.arknights/com.u8.sdk.U8UnityContext')

        util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/start_login.jpg')
        while True:
            x, y = util.findPic(self.publicPath() + 'bmp/start_login.jpg')
            if x != -1 and y != -1:
                util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/start_login.jpg')
                break
        util.click(x, y)

        util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/login.jpg')
        while True:
            x, y = util.findPic(self.publicPath() + 'bmp/login.jpg')
            if x != -1 and y != -1:
                util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/login.jpg')
                break
        util.click(x, y)

        cnt = 0
        util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/into.jpg')
        util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/is_broadcast.jpg')
        util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/close.jpg')
        while True:
            x, y = util.findPic(self.publicPath() + 'bmp/into.jpg')
            if x != -1 and y != -1:
                if cnt != 5:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/into.jpg')
                    cnt = cnt + 1
                    continue
                else:
                    util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/into.jpg')
                    break

            x, y = util.findPic(self.publicPath() + 'bmp/is_broadcast.jpg')
            if x != -1 and y != -1:
                util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/is_broadcast.jpg')

                util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/close.jpg')
                while True:
                    x, y = util.findPic(self.publicPath() + 'bmp/close.jpg')
                    if x != -1 and y != -1:
                        util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/close.jpg')
                        break
                util.click(x, y)
                
                util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/daily_check.jpg')
                while True:
                    x, y = util.findPic(self.publicPath() + 'bmp/daily_check.jpg')
                    if x != -1 and y != -1:
                        util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/daily_check.jpg')
                        break
                util.click(x, y)

                util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/is_daily_check.jpg')
                while True:
                    x, y = util.findPic(self.publicPath() + 'bmp/is_daily_check.jpg')
                    if x != -1 and y != -1:
                        util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/is_daily_check.jpg')
                        break
                util.logOut(__file__,'findPicLoop 循环找图开始 '+self.publicPath() + 'bmp/close.jpg')
                while True:
                    x, y = util.findPic(self.publicPath() + 'bmp/close.jpg')
                    if x != -1 and y != -1:
                        util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/close.jpg')
                        break
                util.click(x, y)

                continue

            x, y = util.findPic(self.publicPath() + 'bmp/close.jpg')
            if x != -1 and y != -1:
                util.logOut(__file__,'findPicLoop 循环找图结束 '+self.publicPath() + 'bmp/close.jpg')
                util.click(x, y)
                continue

        util.logOut(__file__,'restartProcess 重启脚本结束')

    # 带重启的找图
    def picLoop(self, url, threshold=0.8, size=(0, 0, 0, 0)):
        x,y = util.findPicLoop(url, threshold=threshold, size=size)
        if x==-2 and y==-2:
            util.logOut(__file__,'picLoop没找到图 需要重启脚本！！！！！！')
            self.restartProcess()
            raise ValueError('restart')
        return (x,y)

    # 出击到结束的过程
    def anchorProcess(self):
        util.logOut(__file__, '----------一把开始----------')
        self.picLoop(const.publicPath() + 'bmp/start.jpg')
        # 代理指挥
        if not util.isFindPic(const.publicPath() + 'bmp/is_agent.jpg'):
            x, y = self.picLoop(const.publicPath() + 'bmp/agent.jpg')
            util.click(x, y)
        x , y = self.picLoop(const.publicPath() + 'bmp/start.jpg')
        util.click(x, y)
        x , y = self.picLoop(const.publicPath() + 'bmp/operation_start.jpg')
        util.click(x, y)
        time.sleep(60.000)
        x , y = self.picLoop(const.publicPath() + 'bmp/end.jpg')
        time.sleep(3.000)
        util.click(x, y)
        self.picLoop(const.publicPath() + 'bmp/start.jpg')
        util.logOut(__file__, '----------一把结束----------')
    
const = Const()