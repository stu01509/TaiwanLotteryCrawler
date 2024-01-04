# -*- coding: utf-8 -*-
import logging

import requests

from TaiwanLottery import utils


class TaiwanLotteryCrawler():
    NO_DATA = '查無資料'
    BASE_URL = 'https://api.taiwanlottery.com/TLCAPIWeB/Lottery'
    COUNT_OF_GROUP_1 = 6

    def get_lottery_result(self, url):
        response = requests.get(url)
        return response.json()

    # 威力彩
    def super_lotto(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/SuperLotto638Result?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '威力彩_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        super_lotto638_result = result['content']['superLotto638Res']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": super_lotto638_result[i]['period'],
                "開獎日期": super_lotto638_result[i]['lotteryDate'],
                "第一區": super_lotto638_result[i]['drawNumberSize'][0:self.COUNT_OF_GROUP_1],
                "第二區": super_lotto638_result[i]['drawNumberSize'][self.COUNT_OF_GROUP_1]
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas

    # 大樂透
    def lotto649(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/Lotto649Result?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '大樂透_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        lotto649_result = result['content']['lotto649Res']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": lotto649_result[i]['period'],
                "開獎日期": lotto649_result[i]['lotteryDate'],
                "獎號": lotto649_result[i]['drawNumberSize'][0:self.COUNT_OF_GROUP_1],
                "特別號": lotto649_result[i]['drawNumberSize'][self.COUNT_OF_GROUP_1]
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas

    # # 今彩539
    def daily_cash(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/Daily539Result?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '今彩539_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        daily539_result = result['content']['daily539Res']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": daily539_result[i]['period'],
                "開獎日期": daily539_result[i]['lotteryDate'],
                "獎號": daily539_result[i]['drawNumberSize'],
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas

    # # 雙贏彩
    def lotto1224(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/Lotto1224Result?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '雙贏彩_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        lotto1224_result = result['content']['lotto1224Res']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": lotto1224_result[i]['period'],
                "開獎日期": lotto1224_result[i]['lotteryDate'],
                "獎號": lotto1224_result[i]['drawNumberSize'],
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas

    # # 3星彩
    def lotto3d(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/3DHistoryResult?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '3星彩_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        lotto_3d_history_result = result['content']['lotto3DHistoryRes']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": lotto_3d_history_result[i]['period'],
                "開獎日期": lotto_3d_history_result[i]['lotteryDate'],
                "獎號": lotto_3d_history_result[i]['drawNumberAppear'],
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas

    # 4星彩
    def lotto4d(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/4DHistoryResult?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '4星彩_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        lotto_4d_history_result = result['content']['lotto4DHistoryRes']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": lotto_4d_history_result[i]['period'],
                "開獎日期": lotto_4d_history_result[i]['lotteryDate'],
                "獎號": lotto_4d_history_result[i]['drawNumberAppear'],
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas

    # 38樂合彩
    def lotto38m6(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/38M6Result?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '38樂合彩_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        m638_result = result['content']['m638Res']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": m638_result[i]['period'],
                "開獎日期": m638_result[i]['lotteryDate'],
                "獎號": m638_result[i]['drawNumberSize'],
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas

    # 49樂合彩
    def lotto49m6(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/49M6Result?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '49樂合彩_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        m649_result = result['content']['m649Res']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": m649_result[i]['period'],
                "開獎日期": m649_result[i]['lotteryDate'],
                "獎號": m649_result[i]['drawNumberSize'],
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas

    # 39樂合彩
    def lotto39m5(self, back_time=[utils.get_current_year(), utils.get_current_month()]):
        URL = "{}/39M5Result?period&month={}-{}&pageSize=31".format(self.BASE_URL, back_time[0], back_time[1])

        title = '39樂合彩_' + str(back_time[0]) + '_' + str(back_time[1])
        result = self.get_lottery_result(URL)
        total_size = result['content']['totalSize']
        m539_result = result['content']['m539Res']
        datas = []

        for i in range(total_size):
            datas.append({
                "期別": m539_result[i]['period'],
                "開獎日期": m539_result[i]['lotteryDate'],
                "獎號": m539_result[i]['drawNumberSize'],
            })

        if len(datas) == 0:
            logging.warning(self.NO_DATA + title)

        return datas
