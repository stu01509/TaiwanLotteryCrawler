# -*- coding: utf-8 -*-
import datetime
import math
import logging
import json
from terminaltables import AsciiTable


# 取得目前月份
def getCurrentMonth():
    currentTime = datetime.datetime.now()
    return currentTime.month

# 取得目前民國年分
def getCurrentRepublicEra():
    currentTime = datetime.datetime.now()
    return currentTime.year - 1911

# 西元年月份轉民國年月份
def convertToRepublicEraMonth(time):
    if ('-' in time):
        return [int(time.split('-')[0]) - 1911, int(time.split('-')[1])]

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

# 使用 Table 樣式顯示
def printToTable(title, datas):
    tableDatas = []
    if ('第一區' in datas[0] and '第二區' in datas[0]):
        tableDatas.append(['期別', '開獎日期', '第一區', '第二區'])
    elif ('獎號' in datas[0] and '特別號' in datas[0]):
        tableDatas.append(['期別', '開獎日期', '獎號', '特別號'])
    else:
        tableDatas.append(['期別', '開獎日期', '獎號'])
    for i in range(len(datas)):
        if ('第一區' in datas[0] and '第二區' in datas[0]):
            tableDatas.append([datas[i]['期別'], datas[i]['開獎日期'], datas[i]['第一區'], datas[i]['第二區']])
        elif ('獎號' in datas[0] and '特別號' in datas[0]):
            tableDatas.append([datas[i]['期別'], datas[i]['開獎日期'], datas[i]['獎號'], datas[i]['特別號']])
        else:
            tableDatas.append([datas[i]['期別'], datas[i]['開獎日期'], datas[i]['獎號']])
    table = AsciiTable(tableDatas)
    table.title = title
    print(table.table)
    print('\n')