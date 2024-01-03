# -*- coding: utf-8 -*-
import datetime
import json
import logging
import math

from terminaltables import AsciiTable


# 取得目前月份
def get_current_month():
    return datetime.datetime.now().strftime('%m')


# 取得目前年
def get_current_year():
    return datetime.datetime.now().strftime('%Y')


# 西元年月份轉民國年月份
def convert_to_republic_era_month(time):
    if ('-' in time):
        return [int(time.split('-')[0]) - 1911, int(time.split('-')[1])]


# 計算月數差
def month_diff(back_month):
    current_republic_era = datetime.datetime.now().year - 1911
    current_month = datetime.datetime.now().month
    sum_month = (current_republic_era * 12) + current_month - back_month
    if back_month >= sum_month or back_month <= -1:
        logging.error("輸入格式錯誤")
    calc_year = math.floor(sum_month / 12)
    calc_month = sum_month % 12
    '''處理 calc_month 為 0 '''
    if (calc_month == 0):
        calc_month = 12
        calc_year -= 1
    return [calc_year, calc_month]


# 輸出成 JSON 檔案
def output_to_json(filename, data):
    try:
        with open(filename + '.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
    except PermissionError:
        logging.error(filename + "存取權限異常")
    except Exception:
        logging.error(filename + "存取發生未知的錯誤")


# 使用 Table 樣式顯示
def print_to_table(title, datas):
    table_datas = []
    if ('第一區' in datas[0] and '第二區' in datas[0]):
        table_datas.append(['期別', '開獎日期', '第一區', '第二區'])
    elif ('獎號' in datas[0] and '特別號' in datas[0]):
        table_datas.append(['期別', '開獎日期', '獎號', '特別號'])
    else:
        table_datas.append(['期別', '開獎日期', '獎號'])
    for i in range(len(datas)):
        if ('第一區' in datas[0] and '第二區' in datas[0]):
            table_datas.append([datas[i]['期別'], datas[i]['開獎日期'], datas[i]['第一區'], datas[i]['第二區']])
        elif ('獎號' in datas[0] and '特別號' in datas[0]):
            table_datas.append([datas[i]['期別'], datas[i]['開獎日期'], datas[i]['獎號'], datas[i]['特別號']])
        else:
            table_datas.append([datas[i]['期別'], datas[i]['開獎日期'], datas[i]['獎號']])
    table = AsciiTable(table_datas)
    table.title = title
    print(table.table)
    print('\n')
