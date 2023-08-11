# -*- coding: utf-8 -*-
import argparse
import logging
from TaiwanLottery import TaiwanLotteryCrawler
from TaiwanLottery import utils

logging.basicConfig(level=logging.INFO)

LOTTERY_GAME_MAPPING = {
    'SUPER_LOTTO': '威力彩',
    'LOTTO649': '大樂透',
    'DAILY_CASH': '今彩539',
    'LOTTO1224': '雙贏彩',
}


def main():
    parser = argparse.ArgumentParser(
        description='Taiwan Lottery 台灣彩券爬蟲',
        epilog='https://github.com/stu01509/TaiwanLottery')

    parser.add_argument('game', nargs='?', default='',
                        help='爬取指定的彩券類型, 威力彩 大樂透 今彩539 雙贏彩')
    parser.add_argument('-b', '--back', default=0,
                        help='爬取幾個月前的資料')
    parser.add_argument('-t', '--time', default=0,
                        help='爬取指定年月份的資料 格式(YYYY-MM)')
    parser.add_argument('-o', '--output', action='store_true',
                        help='將爬取資料輸出成 json')

    args = parser.parse_args()
    logging.debug(args)

    lottery = TaiwanLotteryCrawler()

    if (args.output is False and args.game == '' and args.back == 0 and args.time == 0):
        lottery.super_lotto()
        lottery.lotto649()
        lottery.daily_cash()
        lottery.lotto1224()
    elif (args.output is True and args.game == '' and args.back == 0 and args.time == 0):
        lottery.super_lotto(True, True)
        lottery.lotto649(True, True)
        lottery.daily_cash(True, True)
        lottery.lotto1224(True, True)
    elif (args.output is False and args.game != '' and args.back != 0 and args.time == 0):
        if (args.game == LOTTERY_GAME_MAPPING['SUPER_LOTTO']):
            lottery.super_lotto_back(True, False, args.back)
        elif (args.game == LOTTERY_GAME_MAPPING['LOTTO649']):
            lottery.lotto649_back(True, False, args.back)
        elif (args.game == LOTTERY_GAME_MAPPING['DAILY_CASH']):
            lottery.daily_cash_back(True, False, args.back)
        elif (args.game == LOTTERY_GAME_MAPPING['LOTTO1224']):
            lottery.lotto1224_back(True, False, args.back)
    elif (args.output is True and args.game != '' and args.back != 0 and args.time == 0):
        if (args.game == LOTTERY_GAME_MAPPING['SUPER_LOTTO']):
            lottery.super_lotto_back(True, True, args.back)
        elif (args.game == LOTTERY_GAME_MAPPING['LOTTO649']):
            lottery.lotto649_back(True, True, args.back)
        elif (args.game == LOTTERY_GAME_MAPPING['DAILY_CASH']):
            lottery.daily_cash_back(True, True, args.back)
        elif (args.game == LOTTERY_GAME_MAPPING['LOTTO1224']):
            lottery.lotto1224_back(True, True, args.back)
    elif (args.output is False and args.game != '' and args.back == 0 and args.time != 0):
        if (args.game == LOTTERY_GAME_MAPPING['SUPER_LOTTO']):
            lottery.super_lotto(True, False, utils.convert_to_republic_era_month(args.time))
        elif (args.game == LOTTERY_GAME_MAPPING['LOTTO649']):
            lottery.lotto649(True, False, utils.convert_to_republic_era_month(args.time))
        elif (args.game == LOTTERY_GAME_MAPPING['DAILY_CASH']):
            lottery.daily_cash(True, False, utils.convert_to_republic_era_month(args.time))
        elif (args.game == LOTTERY_GAME_MAPPING['LOTTO1224']):
            lottery.lotto1224(True, False, utils.convert_to_republic_era_month(args.time))
    elif (args.output is True and args.game != '' and args.back == 0 and args.time != 0):
        if (args.game == LOTTERY_GAME_MAPPING['SUPER_LOTTO']):
            lottery.super_lotto(True, True, utils.convert_to_republic_era_month(args.time))
        elif (args.game == LOTTERY_GAME_MAPPING['LOTTO649']):
            lottery.lotto649(True, True, utils.convert_to_republic_era_month(args.time))
        elif (args.game == LOTTERY_GAME_MAPPING['DAILY_CASH']):
            lottery.daily_cash(True, True, utils.convert_to_republic_era_month(args.time))
        elif (args.game == LOTTERY_GAME_MAPPING['LOTTO1224']):
            lottery.lotto1224(True, True, utils.convert_to_republic_era_month(args.time))


if __name__ == '__main__':
    main()
