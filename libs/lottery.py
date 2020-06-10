# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import logging
from libs import utils

class Lottery():
    def __init__(self):        
        pass
        
    # 威力彩
    def superLotto(self, isPrintData=True, isOutput=False, backTime=[utils.getCurrentRepublicEra(), utils.getCurrentMonth()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/SuperLotto638/history.aspx'
        title = '威力彩_' + str( backTime[0]) + '_' + str( backTime[1])

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')

        datas = []
        payload = {
            'SuperLotto638Control_history1$DropDownList1': '1',
            'SuperLotto638Control_history1$chk': 'radYM',
            'SuperLotto638Control_history1$dropYear': backTime[0],
            'SuperLotto638Control_history1$dropMonth': backTime[1],
            'SuperLotto638Control_history1$btnSubmit': '查詢'
        }
        payload["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = soup.select_one(
            "#__VIEWSTATEGENERATOR")["value"]
        payload["__EVENTVALIDATION"] = soup.select_one(
            "#__EVENTVALIDATION")["value"]

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, 'html.parser')

        if ('查無資料' in res.text):
            logging.warning('查無資料 ' + title)
            return

        firstNums = soup.select(".td_w.font_black14b_center")
        secondNums = soup.select(".td_w.font_red14b_center")
        dataCount = len(secondNums) / 2

        for i in range(0, int(dataCount)):
            tempSecondNums = []
            stage = soup.select(
                '#SuperLotto638Control_history1_dlQuery_DrawTerm_' + str(i))
            date = soup.select(
                '#SuperLotto638Control_history1_dlQuery_Date_' + str(i))

            for j in range(6):
                tempSecondNums.append(firstNums[((i * 2) * 6) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "第一區": tempSecondNums,
                "第二區": secondNums[i * 2].text.strip()
            }
            datas.append(data)
        
        if len(datas) == 0:
            logging.warning('查無資料 ' + title)
            return

        if isPrintData:
            utils.printToTable(title, datas)
        if isOutput:
            utils.outputToJson(title, datas)
        return datas

    # 大樂透
    def lotto649(self, isPrintData=True, isOutput=False, backTime=[utils.getCurrentRepublicEra(), utils.getCurrentMonth()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
        title = '大樂透_' + str( backTime[0]) + '_' + str( backTime[1])    


        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')

        datas = []
        payload = {
            'Lotto649Control_history$DropDownList1': '2',
            'Lotto649Control_history$chk': 'radYM',
            'Lotto649Control_history$dropYear': backTime[0],
            'Lotto649Control_history$dropMonth': backTime[1],
            'Lotto649Control_history$btnSubmit': '查詢'
        }
        payload["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = soup.select_one(
            "#__VIEWSTATEGENERATOR")["value"]
        payload["__EVENTVALIDATION"] = soup.select_one(
            "#__EVENTVALIDATION")["value"]

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, 'html.parser')

        if ('查無資料' in res.text):
            logging.warning('查無資料 ' + title)
            return

        firstNums = soup.select(".td_w.font_black14b_center")
        secondNums = soup.select(".td_w.font_red14b_center")
        dataCount = len(secondNums) / 2

        for i in range(0, int(dataCount)):
            tempSecondNums = []
            stage = soup.select(
                '#Lotto649Control_history_dlQuery_L649_DrawTerm_' + str(i))
            date = soup.select(
                '#Lotto649Control_history_dlQuery_L649_DDate_' + str(i))

            for j in range(6):
                tempSecondNums.append(firstNums[((i * 2) * 6) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "獎號": tempSecondNums,
                "特別號": secondNums[i * 2].text.strip()
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning('查無資料 ' + title)
            return
        
        if isPrintData:
            utils.printToTable(title, datas)
        if isOutput:
            utils.outputToJson(title, datas)
        return datas

    # 今彩539
    def dailyCash(self, isPrintData=True, isOutput=False, backTime=[utils.getCurrentRepublicEra(), utils.getCurrentMonth()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx'
        title = '今彩539_' + str( backTime[0]) + '_' + str( backTime[1]) 

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        datas = []

        payload = {
            'D539Control_history1$DropDownList1': '5',
            'D539Control_history1$chk': 'radYM',
            'D539Control_history1$dropYear': backTime[0],
            'D539Control_history1$dropMonth': backTime[1],
            'D539Control_history1$btnSubmit': '查詢'
        }
        payload["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = soup.select_one(
            "#__VIEWSTATEGENERATOR")["value"]
        payload["__EVENTVALIDATION"] = soup.select_one(
            "#__EVENTVALIDATION")["value"]

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, 'html.parser')

        if ('查無資料' in res.text):
            logging.warning('查無資料 ' + title)
            return

        firstNums = soup.select(".td_w.font_black14b_center")
        dataCount = len(firstNums) / 5 / 2

        for i in range(0, int(dataCount)):
            tempSecondNums = []
            stage = soup.select(
                '#D539Control_history1_dlQuery_D539_DrawTerm_' + str(i))
            date = soup.select(
                '#D539Control_history1_dlQuery_D539_DDate_' + str(i))

            for j in range(5):
                tempSecondNums.append(firstNums[((i * 2) * 5) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "獎號": tempSecondNums,
            }
            datas.append(data)
        
        if len(datas) == 0:
            logging.warning('查無資料 ' + title)
            return
        if isPrintData:
            utils.printToTable(title, datas)            
        if isOutput:
            utils.outputToJson(title, datas)
        return datas

    # 雙贏彩
    def lotto1224(self, isPrintData=True, isOutput=False, backTime=[utils.getCurrentRepublicEra(), utils.getCurrentMonth()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Lotto1224/history.aspx'
        title = '雙贏彩_' + str( backTime[0]) + '_' + str( backTime[1])

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        datas = []

        payload = {
            'Lotto1224Control_history$DropDownList1': '12',
            'Lotto1224Control_history$chk': 'radYM',
            'Lotto1224Control_history$dropYear': backTime[0],
            'Lotto1224Control_history$dropMonth': backTime[1],
            'Lotto1224Control_history$btnSubmit': '查詢'
        }
        payload["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = soup.select_one(
            "#__VIEWSTATEGENERATOR")["value"]
        payload["__EVENTVALIDATION"] = soup.select_one(
            "#__EVENTVALIDATION")["value"]
        
        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, 'html.parser')

        if ('查無資料' in res.text):
            logging.warning('查無資料 ' + title)
            return

        firstNums = soup.select(".td_w.font_black14b_center")
        dataCount = len(firstNums) / 2 / 12

        for i in range(0, int(dataCount)):
            tempSecondNums = []
            stage = soup.select(
                '#Lotto1224Control_history_dlQuery_Lotto1224_DrawTerm_' + str(i))
            date = soup.select(
                '#Lotto1224Control_history_dlQuery_Lotto1224_DDate_' + str(i))

            for j in range(12):
                tempSecondNums.append(firstNums[((i * 2) * 12) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "獎號": tempSecondNums,
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning('查無資料 ' + title)
            return
        if isPrintData:
            utils.printToTable(title, datas)
        if isOutput:
            utils.outputToJson(title, datas)
        return datas

    # 威力彩歷史查詢
    def superLottoBack(self, isPrintData=True, isOutput=True, backMonth='0'):
        for i in range(backMonth, -1, -1):
            self.superLotto(isPrintData, isOutput, utils.monthDiff(i))
            logging.debug(str(utils.monthDiff(i)[0]) + '_' +  str(utils.monthDiff(i)[1]))      

    # 大樂透歷史查詢
    def lotto649Back(self, isPrintData=True, isOutput=True, backMonth='0'):
        for i in range(backMonth, -1, -1):
            self.lotto649(isPrintData, isOutput, utils.monthDiff(i))
            logging.debug(str(utils.monthDiff(i)[0]) + '_' +  str(utils.monthDiff(i)[1]))      

    # 今彩539歷史查詢
    def dailyCashBack(self, isPrintData=True, isOutput=True, backMonth='0'):
        for i in range(backMonth, -1, -1):
            self.dailyCash(isPrintData, isOutput, utils.monthDiff(i))
            logging.debug(str(utils.monthDiff(i)[0]) + '_' +  str(utils.monthDiff(i)[1]))      
    
    # 雙贏彩歷史查詢
    def lotto1224Back(self, isPrintData=True, isOutput=True, backMonth='0'):
        for i in range(backMonth, -1, -1):
            self.lotto1224(isPrintData, isOutput, utils.monthDiff(i))
            logging.debug(str(utils.monthDiff(i)[0]) + '_' +  str(utils.monthDiff(i)[1]))      


