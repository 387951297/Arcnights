import importlib
import sys
import os
import ctypes
import traceback
sys.path.append(os.getcwd().replace('\\', '/')+'/src')

m = ['' for _ in range(100)]
# 引用带数字的py模组
for fileName in os.listdir('./src'):
    try:
        int(fileName[0])
        m[int(fileName[0])] = importlib.import_module(
            fileName.replace('.py', ''))
    except ValueError:
        pass

# 是否为管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# 获取管理员权限
def changeAdmin():
    if not is_admin():
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, __file__, None, 1)
            sys.exit()

# 菜单显示
def mainPrint():
    os.system("cls")
    for fileName in os.listdir('./src'):
        try:
            int(fileName[0])
            print(fileName.replace('.py', ''))
        except ValueError:
            pass
    print('请输入数字来启动对应的脚本：')
    while True:
        str = input()
        for fileName in os.listdir('./src'):
            if str == fileName[0]:
                return str
        print('请重新输入数字来启动对应的脚本：')


if __name__ == '__main__':
    changeAdmin()
    while True:
        try:
            m[int(mainPrint())].main()
        except Exception as err:
            print(err.args)
            print('==========')
            print(traceback.format_exc()) 
            input()
            sys.exit()



        
