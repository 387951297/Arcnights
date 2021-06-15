import importlib
import sys
import os
import ctypes
import traceback
import time
import subprocess
sys.path.append(os.getcwd().replace('\\', '/')+'/src')

m = ['' for _ in range(100)]
util = ''
# 引用带数字的py模组
for fileName in os.listdir('./src'):
    if fileName == 'util.py':
        util = importlib.import_module(fileName.replace('.py', '')).util
        continue
    num = ''
    try:
        num = int(fileName[0:2])
        m[num] = importlib.import_module(
            fileName.replace('.py', ''))
        continue
    except ValueError:
        pass
    try:
        num = int(fileName[0])
        m[num] = importlib.import_module(
            fileName.replace('.py', ''))
        continue
    except ValueError:
        pass

# 菜单显示
def mainPrint():
    printList = ['' for _ in range(100)]
    for fileName in os.listdir('./src'):
        try:
            num = int(fileName[0:2])
            printList[num] = fileName.replace('.py', '')
            continue
        except ValueError:
            pass
        try:
            num = int(fileName[0])
            printList[num] = fileName.replace('.py', '')
            continue
        except ValueError:
            pass
    for str in printList:
        if str != '':
            print(str)
    print('请输入数字来启动对应的脚本：')
    while True:
        str = input()
        for fileName in os.listdir('./src'):
            if str == fileName[0] or str == fileName[0:2]:
                return str
        print('请重新输入数字来启动对应的脚本：')

# 执行adb指令
def adb(command):
    while True:
        AdbPath = '.\\bin\\adb_server.exe '
        ret = subprocess.run(
            AdbPath + command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding="utf-8")
        if ret.returncode == 0:
            if ret.stdout != '':
                print(ret.stdout)
            return ret.stdout
        else:
            print('======adb subprocess error======')
            print(ret)
            continue

if __name__ == '__main__':
    # 初始化
    print('adb初始化开始')
    adb('kill-server')
    adb('connect 127.0.0.1:7555')
    adb('shell mkdir /storage/emulated/0/data')
    adb('shell mkdir /storage/emulated/0/data/screen')
    adb('shell screencap /storage/emulated/0/data/screen/image.png')
    print('adb初始化成功')
    print('')
	
    index = -999
    while True:
        index = int(mainPrint())
        while True:
            try:
                m[index].main()
                break
            except Exception as err:
                if str(err) == 'restart':
                    # 重启脚本
                    continue
                else:
                    print(err.args)
                    print('==========')
                    print(traceback.format_exc()) 
                    continue
                    # input()
                    # sys.exit()
        os.system("cls")

        


        
