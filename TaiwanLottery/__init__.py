# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import logging
import time
from TaiwanLottery import utils
import random


class TaiwanLotteryCrawler():

    html_parser = 'html.parser'
    no_data = '查無資料'

    # 威力彩
    def super_lotto(self, is_print_data=True, is_output=False, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/SuperLotto638/history.aspx'
        title = '威力彩_' + str(back_time[0]) + '_' + str(back_time[1])

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, self.html_parser)

        datas = []
        payload = {
            'SuperLotto638Control_history1$chk': 'radYM',
            'SuperLotto638Control_history1$dropYear': back_time[0],
            'SuperLotto638Control_history1$dropMonth': back_time[1],
            'SuperLotto638Control_history1$btnSubmit': '查詢'
        }
        payload["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = soup.select_one(
            "#__VIEWSTATEGENERATOR")["value"]
        payload["__EVENTVALIDATION"] = soup.select_one(
            "#__EVENTVALIDATION")["value"]

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

        if is_print_data:
            utils.print_to_table(title, datas)
        if is_output:
            utils.output_to_json(title, datas)
        return datas

    # 大樂透
    def lotto649(self, is_print_data=True, is_output=False, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
        title = '大樂透_' + str(back_time[0]) + '_' + str(back_time[1])

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, self.html_parser)

        datas = []
        payload = {
            'Lotto649Control_history$chk': 'radYM',
            'Lotto649Control_history$dropYear': back_time[0],
            'Lotto649Control_history$dropMonth': back_time[1],
            'Lotto649Control_history$btnSubmit': '查詢'
        }
        payload["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = soup.select_one(
            "#__VIEWSTATEGENERATOR")["value"]
        payload["__EVENTVALIDATION"] = soup.select_one(
            "#__EVENTVALIDATION")["value"]

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

        if is_print_data:
            utils.print_to_table(title, datas)
        if is_output:
            utils.output_to_json(title, datas)
        return datas

    # 今彩539
    def daily_cash(self, is_print_data=True, is_output=False, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx'
        title = '今彩539_' + str(back_time[0]) + '_' + str(back_time[1])

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, self.html_parser)
        datas = []

        payload = {
            'D539Control_history1$chk': 'radYM',
            'D539Control_history1$dropYear': back_time[0],
            'D539Control_history1$dropMonth': back_time[1],
            'D539Control_history1$btnSubmit': '查詢'
        }
        payload["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = soup.select_one(
            "#__VIEWSTATEGENERATOR")["value"]
        payload["__EVENTVALIDATION"] = soup.select_one(
            "#__EVENTVALIDATION")["value"]

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
        if is_print_data:
            utils.print_to_table(title, datas)
        if is_output:
            utils.output_to_json(title, datas)
        return datas

    # 雙贏彩
    def lotto1224(self, is_print_data=True, is_output=False, back_time=[utils.get_current_republic_era(), utils.get_current_month()]):
        URL = 'https://www.taiwanlottery.com.tw/Lotto/Lotto1224/history.aspx'
        title = '雙贏彩_' + str(back_time[0]) + '_' + str(back_time[1])

        res = requests.get(URL)
        soup = BeautifulSoup(res.text, self.html_parser)
        datas = []

        payload = {
            'Lotto1224Control_history$chk': 'radYM',
            'Lotto1224Control_history$dropYear': back_time[0],
            'Lotto1224Control_history$dropMonth': back_time[1],
            'Lotto1224Control_history$btnSubmit': '查詢'
        }
        payload["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload["__VIEWSTATEGENERATOR"] = soup.select_one(
            "#__VIEWSTATEGENERATOR")["value"]
        payload["__EVENTVALIDATION"] = soup.select_one(
            "#__EVENTVALIDATION")["value"]

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
        if is_print_data:
            utils.print_to_table(title, datas)
        if is_output:
            utils.output_to_json(title, datas)
        return datas

    # 威力彩歷史查詢
    def super_lotto_back(self, is_print_data=True, is_output=True, back_month='0'):
        for i in range(int(back_month), -1, -1):
            time.sleep(random.random())
            self.super_lotto(is_print_data, is_output, utils.month_diff(i))
            logging.debug(str(utils.month_diff(i)[0]) + '_' + str(utils.month_diff(i)[1]))

    # 大樂透歷史查詢
    def lotto649_back(self, is_print_data=True, is_output=True, back_month='0'):
        for i in range(int(back_month), -1, -1):
            time.sleep(random.random())
            self.lotto649(is_print_data, is_output, utils.month_diff(i))
            logging.debug(str(utils.month_diff(i)[0]) + '_' + str(utils.month_diff(i)[1]))

    # 今彩539歷史查詢
    def daily_cash_back(self, is_print_data=True, is_output=True, back_month='0'):
        for i in range(int(back_month), -1, -1):
            time.sleep(random.random())
            self.daily_cash(is_print_data, is_output, utils.month_diff(i))
            logging.debug(str(utils.month_diff(i)[0]) + '_' + str(utils.month_diff(i)[1]))

    # 雙贏彩歷史查詢
    def lotto1224_back(self, is_print_data=True, is_output=True, back_month='0'):
        for i in range(int(back_month), -1, -1):
            time.sleep(random.random())
            self.lotto1224(is_print_data, is_output, utils.month_diff(i))
            logging.debug(str(utils.month_diff(i)[0]) + '_' + str(utils.month_diff(i)[1]))
