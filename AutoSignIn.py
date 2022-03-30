# author: skywoodsz

import os
import pandas as pd
import pyautogui
import time
from datetime import datetime
import cv2
'''
	利用opencv模板匹配进行入会像素坐标获取，执行鼠标相应动作与密码验证存在判断
	@param tempFile: 模板匹配图像
		   whatDo：鼠标执行动作
		   debug： debug
'''
def ImgAutoClick(tempFile, whatDo, debug=False):
    pyautogui.screenshot('screen.png')
    gray = cv2.imread('screen.png', 0)
    img_templete = cv2.imread(tempFile, 0)
    w, h = img_templete.shape[::-1]
    res = cv2.matchTemplate(gray, img_templete, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    pyautogui.moveTo(top+h/2, left+w/2)
    if(min_val < 1000):
        whatDo(x)
    else:
        return False

    if debug:
        img = cv2.imread("screen.png",1)
        cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
        cv2.imshow("processed",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    os.remove("screen.png")
    
    return True

'''
	会议自动登录
	@param meeting_id: 会议号
		   password：密码，若则保持默认NULL
'''
def SignIn(meeting_id, password=NULL):
    os.startfile("D:\gongju\wemeetapp.exe")
    time.sleep(7)
    ImgAutoClick("JoinMeeting.png", pyautogui.click, False)
    time.sleep(1)
    ImgAutoClick("meeting_id.png", pyautogui.click, False)
    time.sleep(2)
    pyautogui.write(meeting_id)
    time.sleep(2)
    ImgAutoClick("final.png", pyautogui.click, False)
    time.sleep(1)
    res = ImgAutoClick("password.png", pyautogui.moveTo, False)
    if res & password != NULL:
        pyautogui.write(password)
        time.sleep(1)
        ImgAutoClick("passwordJoin.png", pyautogui.click, False)
        time.sleep(1)
    return True

while True:
    now = datetime.now().strftime("%m-%d-%H:%M")
    meeting_id = "xxx xxxx xxxx" # meeting id
    password = "xxxx" # meeting password
    if now == "03-30-11:44": # sign in time
        SignIn(meeting_id, password)
        print("Sign In!")
        break