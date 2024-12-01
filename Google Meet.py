import pyautogui
import time
import datetime
import webbrowser

p = "https://meet.google.com/rym-sdya-oxq"
m = "https://meet.google.com/hpo-sjbv-sqa"
cs = "https://meet.google.com/tax-sbed-ymo"
cm = "https://meet.google.com/adh-iycv-mjz"


def selectperiod():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)
    if (8 > hour >= 7 and min >= 55) or (9 > hour >= 8 and min <= 40):
        z = 0
    elif (9 > hour >= 8 and min >= 40) or (10 > hour >= 9 and min <= 20):
        z = 0
    elif (10 > hour >= 9 and min >= 20) or (11 > hour >= 10 and min <= 0):
        z = 1
    elif 11 > hour >= 10 and 50 > min >= 10:
        z = 2
    elif (11 > hour >= 10 and min >= 50) or (12 > hour >= 11 and min <= 30):
        z = 3
    elif (12 > hour >= 11 and min >= 40) or (13 > hour >= 12 and min <= 20):
        z = 4
    elif (13 > hour >= 12 and min >= 20) or (14 > hour >= 13 and min <= 0):
        z = 5
    else:
        z = 100
    return z


def checksub(x):
    if x == "m":
        x = "https://meet.google.com/hpo-sjbv-sqa"
    elif x == "p":
        x = "https://meet.google.com/rym-sdya-oxq"
    elif x == "cs":
        x = "https://meet.google.com/tax-sbed-ymo"
    elif x == "cm":
        x = "https://meet.google.com/jqf-cgwr-ndb"
    return x


def joinnow():
    global D
    if D == 0:
        webbrowser.open(a)
    elif D == 1:
        webbrowser.open(b)
    elif D == 2:
        webbrowser.open(c)
    elif D == 3:
        webbrowser.open(d)
    elif D == 4:
        webbrowser.open(e)
    elif D == 5:
        webbrowser.open(f)
    time.sleep(5)
    pyautogui.click(x=620, y=825)
    time.sleep(1)
    pyautogui.click(x=725, y=825)
    time.sleep(1)
    pyautogui.click(x=1200, y=695)
    time.sleep(1)
    pyautogui.click(x=1350, y=650)
    D = 1


a = input("Period 1:").lower()
b = input("Period 3:").lower()
c = input("Period 4:").lower()
d = input("Period 5:").lower()
e = input("Period 6:").lower()
f = input("Period 7:").lower()

a = checksub(a)
b = checksub(b)
c = checksub(c)
d = checksub(d)
e = checksub(e)
f = checksub(f)

D = selectperiod()
joinnow()

while True:
    while D == 0:  # 8:00 - 9:20
        now = datetime.datetime.now()
        timenow = now.hour, now.minute
        if str(timenow) == "(7, 58)":
            webbrowser.open(a)
            time.sleep(5)
            pyautogui.click(x=620, y=825)
            time.sleep(1)
            pyautogui.click(x=725, y=825)
            time.sleep(1)
            pyautogui.click(x=1200, y=695)
            time.sleep(1)
            pyautogui.click(x=1350, y=650)
            D = 1

    while D == 1:  # 9:20 - 10:00
        now = datetime.datetime.now()
        timenow = now.hour, now.minute
        if str(timenow) == "(9, 20)":
            webbrowser.open(b)
            time.sleep(5)
            pyautogui.click(x=620, y=825)
            time.sleep(1)
            pyautogui.click(x=725, y=825)
            time.sleep(1)
            pyautogui.click(x=1200, y=695)
            time.sleep(1)
            pyautogui.click(x=1350, y=650)
            D += 1

    while D == 2:  # 10:10 - 10:50
        now = datetime.datetime.now()
        timenow = now.hour, now.minute
        if str(timenow) == "(10, 10)":
            webbrowser.open(c)
            time.sleep(5)
            pyautogui.click(x=620, y=825)
            time.sleep(1)
            pyautogui.click(x=725, y=825)
            time.sleep(1)
            pyautogui.click(x=1200, y=695)
            time.sleep(1)
            pyautogui.click(x=1350, y=650)
            D += 1

    while D == 3:  # 10:50 - 11:30
        now = datetime.datetime.now()
        timenow = now.hour, now.minute
        if str(timenow) == "(10, 50)":
            webbrowser.open(d)
            time.sleep(5)
            pyautogui.click(x=620, y=825)
            time.sleep(1)
            pyautogui.click(x=725, y=825)
            time.sleep(1)
            pyautogui.click(x=1200, y=695)
            time.sleep(1)
            pyautogui.click(x=1350, y=650)
            D += 1

    while D == 4:  # 11:40 - 12:20
        now = datetime.datetime.now()
        timenow = now.hour, now.minute
        if str(timenow) == "(11, 40)":
            webbrowser.open(e)
            time.sleep(5)
            pyautogui.click(x=620, y=825)
            time.sleep(1)
            pyautogui.click(x=725, y=825)
            time.sleep(1)
            pyautogui.click(x=1200, y=695)
            time.sleep(1)
            pyautogui.click(x=1350, y=650)
            D += 1

    while D == 5:  # 12:20 - 01:00
        now = datetime.datetime.now()
        timenow = now.hour, now.minute
        if str(timenow) == "(12, 20)":
            webbrowser.open(f)
            time.sleep(5)
            pyautogui.click(x=620, y=825)
            time.sleep(1)
            pyautogui.click(x=725, y=825)
            time.sleep(1)
            pyautogui.click(x=1200, y=695)
            time.sleep(1)
            pyautogui.click(x=1350, y=650)
            D += 1

    '''while D== 100: #Trial
            now = datetime.datetime.now()
            timenow = now.hour, now.minute
            if str(timenow) == "(21, 43)":
                webbrowser.open(a)
                time.sleep(5)
                pyautogui.click(x=620, y=825)
                time.sleep(1)
                pyautogui.click(x=725, y=825)
                time.sleep(1)
                pyautogui.click(x=1200, y=695)
                time.sleep(1)
                pyautogui.click(x=1350, y=650)
                D += 1'''
