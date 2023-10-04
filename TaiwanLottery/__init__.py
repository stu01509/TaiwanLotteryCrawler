# -*- coding: utf-8 -*-
import logging
import random
import time

import requests
from bs4 import BeautifulSoup

from TaiwanLottery import utils


class TaiwanLotteryCrawler():
    COUNT_OF_3D_LOTTERY_PRIZE_NUMBER = 3
    COUNT_OF_4D_LOTTERY_PRIZE_NUMBER = 4
    COUNT_OF_38M6_LOTTERY_PRIZE_NUMBER = 6
    COUNT_OF_49M6_LOTTERY_PRIZE_NUMBER = 6
    COUNT_OF_39M5_LOTTERY_PRIZE_NUMBER = 5

    html_parser = 'html.parser'
    no_data = '查無資料'

    def initial_default_payload(self, url, payload, keys):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, self.html_parser)

        for key in keys:
            payload[key] = soup.select_one('#' + key)["value"]

    # 威力彩
    def super_lotto(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/SuperLotto638/history.aspx'
        title = '威力彩_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'SuperLotto638Control_history1$chk': 'radYM',
            'SuperLotto638Control_history1$dropYear': back_time[0],
            'SuperLotto638Control_history1$dropMonth': back_time[1],
            'SuperLotto638Control_history1$btnSubmit': '查詢'
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center")
        second_nums = soup.select(".td_w.font_red14b_center")
        data_count = len(second_nums) / 2

        for i in range(0, int(data_count)):
            temp_second_nums = []
            stage = soup.select(
                '#SuperLotto638Control_history1_dlQuery_DrawTerm_' + str(i))
            date = soup.select(
                '#SuperLotto638Control_history1_dlQuery_Date_' + str(i))

            for j in range(6):
                temp_second_nums.append(first_nums[((i * 2) * 6) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "第一區": temp_second_nums,
                "第二區": second_nums[i * 2].text.strip()
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 大樂透
    def lotto649(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
        title = '大樂透_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'Lotto649Control_history$chk': 'radYM',
            'Lotto649Control_history$dropYear': back_time[0],
            'Lotto649Control_history$dropMonth': back_time[1],
            'Lotto649Control_history$btnSubmit': '查詢'
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center")
        second_nums = soup.select(".td_w.font_red14b_center")
        data_count = len(second_nums) / 2

        for i in range(0, int(data_count)):
            temp_second_nums = []
            stage = soup.select(
                '#Lotto649Control_history_dlQuery_L649_DrawTerm_' + str(i))
            date = soup.select(
                '#Lotto649Control_history_dlQuery_L649_DDate_' + str(i))

            for j in range(6):
                temp_second_nums.append(first_nums[((i * 2) * 6) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "獎號": temp_second_nums,
                "特別號": second_nums[i * 2].text.strip()
            }

            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 今彩539
    def daily_cash(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx'
        title = '今彩539_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'D539Control_history1$chk': 'radYM',
            'D539Control_history1$dropYear': back_time[0],
            'D539Control_history1$dropMonth': back_time[1],
            'D539Control_history1$btnSubmit': '查詢'
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center")
        data_count = len(first_nums) / 5 / 2

        for i in range(0, int(data_count)):
            temp_second_nums = []
            stage = soup.select(
                '#D539Control_history1_dlQuery_D539_DrawTerm_' + str(i))
            date = soup.select(
                '#D539Control_history1_dlQuery_D539_DDate_' + str(i))

            for j in range(5):
                temp_second_nums.append(first_nums[((i * 2) * 5) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "獎號": temp_second_nums,
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 雙贏彩
    def lotto1224(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Lotto1224/history.aspx'
        title = '雙贏彩_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'Lotto1224Control_history$chk': 'radYM',
            'Lotto1224Control_history$dropYear': back_time[0],
            'Lotto1224Control_history$dropMonth': back_time[1],
            'Lotto1224Control_history$btnSubmit': '查詢'
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center")
        data_count = len(first_nums) / 2 / 12

        for i in range(0, int(data_count)):
            temp_second_nums = []
            stage = soup.select(
                '#Lotto1224Control_history_dlQuery_Lotto1224_DrawTerm_' + str(i))
            date = soup.select(
                '#Lotto1224Control_history_dlQuery_Lotto1224_DDate_' + str(i))

            for j in range(12):
                temp_second_nums.append(first_nums[((i * 2) * 12) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "獎號": temp_second_nums,
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 3星彩
    def lotto3d(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/3D/history.aspx'
        title = '3星彩_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'L3DControl_history1$chk': 'radYM',
            'L3DControl_history1$dropYear': back_time[0],
            'L3DControl_history1$dropMonth': back_time[1],
            'L3DControl_history1$btnSubmit': '查詢'
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center")
        data_count = len(first_nums) / self.COUNT_OF_3D_LOTTERY_PRIZE_NUMBER
        stage = soup.select('table[class*="table_"] > tr:nth-child(3) > td:nth-child(1)')
        date = soup.select('table[class*="table_"] > tr:nth-child(3) > td:nth-child(2) > p')

        for i in range(0, int(data_count)):
            temp_second_nums = []

            for j in range(self.COUNT_OF_3D_LOTTERY_PRIZE_NUMBER):
                temp_second_nums.append(first_nums[((i) * self.COUNT_OF_3D_LOTTERY_PRIZE_NUMBER) + j].text.strip())

            data = {
                "期別": stage[i].text,
                "開獎日期": date[i].text.replace('開獎', ''),
                "獎號": temp_second_nums,
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 4星彩
    def lotto4d(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/4D/history.aspx'
        title = '4星彩_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'L4DControl_history1$chk': 'radYM',
            'L4DControl_history1$dropYear': back_time[0],
            'L4DControl_history1$dropMonth': back_time[1],
            'L4DControl_history1$btnSubmit': '查詢'
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center > span.td_w")
        data_count = len(first_nums) / self.COUNT_OF_4D_LOTTERY_PRIZE_NUMBER
        stage = soup.select('table[class*="table_"] > tr:nth-child(3) > td:nth-child(1)')
        date = soup.select('table[class*="table_"] > tr:nth-child(3) > td:nth-child(2) > p')

        for i in range(0, int(data_count)):
            temp_second_nums = []

            for j in range(self.COUNT_OF_4D_LOTTERY_PRIZE_NUMBER):
                temp_second_nums.append(first_nums[((i) * self.COUNT_OF_4D_LOTTERY_PRIZE_NUMBER) + j].text.strip())

            data = {
                "期別": stage[i].text,
                "開獎日期": date[i].text.replace('開獎', ''),
                "獎號": temp_second_nums,
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 38樂合彩
    def lotto38m6(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/38m6/history.aspx'
        title = '38樂合彩_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'M638Control_history1$chk': 'radYM',
            'M638Control_history1$dropYear': back_time[0],
            'M638Control_history1$dropMonth': back_time[1],
            'M638Control_history1$btnSubmit': '查詢',
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION', '__VIEWSTATEENCRYPTED'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center > span")
        data_count = len(first_nums) / self.COUNT_OF_38M6_LOTTERY_PRIZE_NUMBER / 2

        for i in range(0, int(data_count)):
            temp_second_nums = []
            stage = soup.select(
                '#M638Control_history1_dlQuery_lbM638_DrawTerm_' + str(i))
            date = soup.select(
                '#M638Control_history1_dlQuery_M638_DDate_' + str(i))

            for j in range(self.COUNT_OF_38M6_LOTTERY_PRIZE_NUMBER):
                temp_second_nums.append(first_nums[((i * 2) * self.COUNT_OF_38M6_LOTTERY_PRIZE_NUMBER) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "獎號": temp_second_nums,
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 49樂合彩
    def lotto49m6(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/49m6/history.aspx'
        title = '49樂合彩_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'M649Control_history1$chk': 'radYM',
            'M649Control_history1$dropYear': back_time[0],
            'M649Control_history1$dropMonth': back_time[1],
            'M649Control_history1$btnSubmit': '查詢',
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION', '__VIEWSTATEENCRYPTED'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center > span")
        data_count = len(first_nums) / self.COUNT_OF_49M6_LOTTERY_PRIZE_NUMBER / 2

        for i in range(0, int(data_count)):
            temp_second_nums = []
            stage = soup.select(
                '#M649Control_history1_dlQuery_M649_DrawTerm_' + str(i))
            date = soup.select(
                '#M649Control_history1_dlQuery_M649_DDate_' + str(i))

            for j in range(self.COUNT_OF_38M6_LOTTERY_PRIZE_NUMBER):
                temp_second_nums.append(first_nums[((i * 2) * self.COUNT_OF_49M6_LOTTERY_PRIZE_NUMBER) + j].text.strip())

            data = {
                "期別": stage[0].text,
                "開獎日期": date[0].text,
                "獎號": temp_second_nums,
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 39樂合彩
    def lotto39m5(self, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/39m5/history.aspx'
        title = '39樂合彩_' + str(back_time[0]) + '_' + str(back_time[1])

        datas = []
        payload = {
            'M539Control_history1$chk': 'radYM',
            'M539Control_history1$dropYear': back_time[0],
            'M539Control_history1$dropMonth': back_time[1],
            'M539Control_history1$btnSubmit': '查詢',
        }

        self.initial_default_payload(URL, payload, ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION', '__VIEWSTATEENCRYPTED'])

        res = requests.post(URL, data=payload)
        soup = BeautifulSoup(res.text, self.html_parser)

        if (self.no_data in res.text):
            logging.warning(self.no_data + title)
            return

        first_nums = soup.select(".td_w.font_black14b_center > span")
        data_count = len(first_nums) / self.COUNT_OF_39M5_LOTTERY_PRIZE_NUMBER / 2

        stage = soup.select('table[class*="table_"] tr:nth-child(2) > td:nth-child(1) > span')
        date = soup.select('table[class*="table_"] tr:nth-child(2) > td:nth-child(2) > span > span')

        for i in range(0, int(data_count)):
            temp_second_nums = []

            for j in range(self.COUNT_OF_39M5_LOTTERY_PRIZE_NUMBER):
                temp_second_nums.append(first_nums[((i * 2) * self.COUNT_OF_39M5_LOTTERY_PRIZE_NUMBER) + j].text.strip())

            data = {
                "期別": stage[i].text,
                "開獎日期": date[i].text,
                "獎號": temp_second_nums,
            }
            datas.append(data)

        if len(datas) == 0:
            logging.warning(self.no_data + title)
            return

        return datas

    # 威力彩歷史查詢
    def super_lotto_back(self, back_month='0'):
        for i in range(int(back_month), -1, -1):
            time.sleep(random.random())
            self.super_lotto(utils.month_diff(i))
            logging.debug(str(utils.month_diff(i)[0]) + '_' + str(utils.month_diff(i)[1]))

    # 大樂透歷史查詢
    def lotto649_back(self, back_month='0'):
        for i in range(int(back_month), -1, -1):
            time.sleep(random.random())
            self.lotto649(utils.month_diff(i))
            logging.debug(str(utils.month_diff(i)[0]) + '_' + str(utils.month_diff(i)[1]))

    # 今彩539歷史查詢
    def daily_cash_back(self, back_month='0'):
        for i in range(int(back_month), -1, -1):
            time.sleep(random.random())
            self.daily_cash(utils.month_diff(i))
            logging.debug(str(utils.month_diff(i)[0]) + '_' + str(utils.month_diff(i)[1]))

    # 雙贏彩歷史查詢
    def lotto1224_back(self, back_month='0'):
        for i in range(int(back_month), -1, -1):
            time.sleep(random.random())
            self.lotto1224(utils.month_diff(i))
            logging.debug(str(utils.month_diff(i)[0]) + '_' + str(utils.month_diff(i)[1]))
