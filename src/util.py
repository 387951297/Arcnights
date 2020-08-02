import base64
import sys
import threading
import time
from datetime import datetime
import os

import numpy as np
import pyautogui
import requests
from cv2 import cv2
from PIL import ImageGrab



class Util:
    __Token = ''

    __TMP_IMAGE = './tmp/image.jpg'

    def __initToken(self):
        pyautogui.FAILSAFE = False
        # 你的 APPID AK SK
        #APP_ID = '18540285'
        API_KEY = '4jBHa2k1I6BaqXObDXon8PM8'
        SECRET_KEY = '52OBvqTOSaSLYLPRI278Rabv5823zsjI'
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
            API_KEY+'&client_secret='+SECRET_KEY
        response = requests.get(host)
        if response:
            self.__Token = response.json()['access_token']

    def __init__(self):
        self.__initToken()

    # 今天星期几
    def dayOfWeek(self):
        return datetime.now().isoweekday()

    # 截图识字
    def getNumbers(self, size):
        request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/numbers'
        img = ImageGrab.grab(size)
        img.save(self.__TMP_IMAGE)
        # 二进制方式打开图片文件
        f = open(self.__TMP_IMAGE, 'rb')
        img = base64.b64encode(f.read())

        params = {'image': img}
        access_token = self.__Token
        request_url = request_url + '?access_token=' + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            request_url, data=params, headers=headers).json()
        print(response)
        list = []
        if 'error_code' in response:
            return list
        for i in range(response['words_result_num']):
            list.append(response['words_result'][i]['words'])
        return list

    # 限定范围内百度api识字 输出list
    def getWords(self, size):
        request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
        img = ImageGrab.grab(size)
        img.save(self.__TMP_IMAGE)
        # 二进制方式打开图片文件
        f = open(self.__TMP_IMAGE, 'rb')
        img = base64.b64encode(f.read())

        params = {'image': img}
        access_token = self.__Token
        request_url = request_url + '?access_token=' + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            request_url, data=params, headers=headers).json()
        print(response)
        list = []
        if 'error_code' in response:
            return list
        for i in range(response['words_result_num']):
            list.append(response['words_result'][i]['words'])
        return list

    # 颜色匹配
    def isFindColor(self, x, y, color):
        image = ImageGrab.grab()
        print(image.getpixel((x, y)))
        return color == image.getpixel((x, y))

    # 截图返回cv2格式的图片
    def grab(self, size=(0, 0, 0, 0)):
        if size != (0, 0, 0, 0):
            image = ImageGrab.grab(size)
        else:
            image = ImageGrab.grab()
        try:
            image.save(self.__TMP_IMAGE)
        except Exception as e:
            print(e)
        return cv2.imread(self.__TMP_IMAGE, 0)

    # url图片与屏幕截图匹配,return中心点x,y
    def findPic(self, url, threshold=0.9, size=(0, 0, 0, 0), img=None, template=None):
        if np.all(img == None):
            img = self.grab(size) if size != (0, 0, 0, 0) else self.grab()
        if np.all(template == None):
            template = cv2.imread(url, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        cv2.waitKey(0)
        if max_val >= threshold:
            return (max_loc[0] + w // 2, max_loc[1] + h // 2)
        else:
            return (-1, -1)
        '''
		loc = np.where(res >= threshold)
		cv2.waitKey(0)
		for pt in zip(*loc[::-1]):
			return (pt[0] + w // 2, pt[1] + h // 2)
		return (-1,-1)
		'''

    # 识图返回列表
    def findPicList(self, url, threshold=0.8, size=(0, 0, 0, 0), img=None, template=None):
        if np.all(img == None):
            img = self.grab(size) if size != (0, 0, 0, 0) else self.grab()
        if np.all(template == None):
            template = cv2.imread(url, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        cv2.waitKey(0)
        list = []
        for pt in zip(*loc[::-1]):
            list.append((pt[0] + w // 2, pt[1] + h // 2))
        return list

    # 循环找图 直到找到退出
    def findPicLoop(self, url, threshold=0.8, size=(0, 0, 0, 0)):
        while True:
            x, y = self.findPic(url, threshold, size)
            if x != -1 and y != -1:
                return (x, y)
            time.sleep(.100)

    # 判断是否找到图
    def isFindPic(self, url, threshold=0.8, size=(0, 0, 0, 0)):
        x, y = self.findPic(url, threshold, size)
        if x == -1 and y == -1:
            return False
        else:
            return True

    # 退出脚本
    def exitScript(self):
        print('脚本结束')
        sys.exit()


util = Util()
