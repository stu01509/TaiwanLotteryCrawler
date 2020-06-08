# -*- coding: utf-8 -*-
import datetime
import math
import logging
import json

# 取得目前月份
def getCurrentMonth():
    currentTime = datetime.datetime.now()
    return currentTime.month

# 取得目前民國年分
def getCurrentRepublicEra():
    currentTime = datetime.datetime.now()
    return currentTime.year - 1911

# 計算月數差
def monthDiff(backMonth):
    currentRepublicEra = datetime.datetime.now().year - 1911
    currentMonth = datetime.datetime.now().month    
    sumMonth = ( currentRepublicEra * 12)  + currentMonth - backMonth
    if backMonth >= sumMonth or backMonth <= -1: 
        logging.error("輸入格式錯誤") 
    calcYear = math.floor(sumMonth / 12)
    calcMonth = sumMonth % 12
    '''處理 calcMonth 為 0 '''
    if (calcMonth == 0): 
        calcMonth = 12
        calcYear-=1
    return [calcYear, calcMonth]

# 輸出成 JSON 檔案
def outputToJson(filename, data):
    try:
        with open(filename + '.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
    except PermissionError as e:
        logging.error(filename + "存取權限異常")     
    except Exception as e:
        logging.error(filename + "存取發生未知的錯誤") 