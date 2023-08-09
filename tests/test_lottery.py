# -*- coding: utf-8 -*-
from src.lottery import Lottery


def test_super_lotto():
    # Given user wants to get 威力彩 2023-06 result
    lottery = Lottery()

    # When user get the 威力彩 2023-06 result without print and output to json
    super_lotto_result = lottery.super_lotto(False, False, [112, 6])

    # Then the super_lotto_result should be equal to test result
    assert super_lotto_result == [
        {'期別': '112000052', '開獎日期': '112/06/29', '第一區': ['36', '27', '26', '29', '08', '01'], '第二區': '02'},
        {'期別': '112000051', '開獎日期': '112/06/26', '第一區': ['16', '01', '15', '24', '17', '35'], '第二區': '06'},
        {'期別': '112000050', '開獎日期': '112/06/22', '第一區': ['24', '28', '04', '01', '17', '07'], '第二區': '08'},
        {'期別': '112000049', '開獎日期': '112/06/19', '第一區': ['20', '12', '36', '08', '04', '27'], '第二區': '01'},
        {'期別': '112000048', '開獎日期': '112/06/15', '第一區': ['24', '02', '34', '36', '25', '26'], '第二區': '08'},
        {'期別': '112000047', '開獎日期': '112/06/12', '第一區': ['38', '35', '16', '18', '01', '02'], '第二區': '01'},
        {'期別': '112000046', '開獎日期': '112/06/08', '第一區': ['08', '35', '38', '18', '03', '12'], '第二區': '03'},
        {'期別': '112000045', '開獎日期': '112/06/05', '第一區': ['34', '35', '11', '04', '28', '32'], '第二區': '01'},
        {'期別': '112000044', '開獎日期': '112/06/01', '第一區': ['29', '37', '10', '25', '18', '36'], '第二區': '02'}
    ]


def test_lotto649():
    # Given user wants to get 大樂透 2023-06 result
    lottery = Lottery()

    # When user get the 大樂透 2023-06 result without print and output to json
    lotto649_result = lottery.lotto649(False, False, [112, 6])

    # Then the lotto649_result should be equal to test result
    assert lotto649_result == [
        {'期別': '112000064', '開獎日期': '112/06/30', '獎號': ['26', '06', '22', '29', '32', '43'], '特別號': '38'},
        {'期別': '112000063', '開獎日期': '112/06/27', '獎號': ['13', '30', '37', '43', '44', '24'], '特別號': '04'},
        {'期別': '112000062', '開獎日期': '112/06/23', '獎號': ['23', '31', '08', '49', '42', '04'], '特別號': '16'},
        {'期別': '112000061', '開獎日期': '112/06/20', '獎號': ['41', '32', '15', '37', '05', '34'], '特別號': '11'},
        {'期別': '112000060', '開獎日期': '112/06/16', '獎號': ['02', '30', '21', '33', '41', '22'], '特別號': '42'},
        {'期別': '112000059', '開獎日期': '112/06/13', '獎號': ['09', '21', '08', '01', '10', '06'], '特別號': '02'},
        {'期別': '112000058', '開獎日期': '112/06/09', '獎號': ['46', '38', '49', '36', '32', '30'], '特別號': '26'},
        {'期別': '112000057', '開獎日期': '112/06/06', '獎號': ['30', '43', '27', '41', '13', '08'], '特別號': '18'},
        {'期別': '112000056', '開獎日期': '112/06/02', '獎號': ['13', '05', '34', '01', '23', '16'], '特別號': '49'}
    ]


def test_daily_cash():
    # Given user wants to get 今彩539 2023-06 result
    lottery = Lottery()

    # When user get the 今彩539 2023-06 result without print and output to json
    daily_cash_result = lottery.daily_cash(False, False, [112, 6])

    # Then the daily_cash_result should be equal to test result
    assert daily_cash_result == [
        {'期別': '112000155', '開獎日期': '112/06/30', '獎號': ['36', '03', '20', '11', '30']},
        {'期別': '112000154', '開獎日期': '112/06/29', '獎號': ['17', '14', '27', '10', '02']},
        {'期別': '112000153', '開獎日期': '112/06/28', '獎號': ['08', '32', '05', '21', '33']},
        {'期別': '112000152', '開獎日期': '112/06/27', '獎號': ['39', '28', '14', '12', '04']},
        {'期別': '112000151', '開獎日期': '112/06/26', '獎號': ['05', '26', '20', '15', '14']},
        {'期別': '112000150', '開獎日期': '112/06/24', '獎號': ['13', '10', '07', '14', '22']},
        {'期別': '112000149', '開獎日期': '112/06/23', '獎號': ['24', '30', '20', '11', '13']},
        {'期別': '112000148', '開獎日期': '112/06/22', '獎號': ['33', '34', '06', '10', '39']},
        {'期別': '112000147', '開獎日期': '112/06/21', '獎號': ['23', '30', '09', '38', '02']},
        {'期別': '112000146', '開獎日期': '112/06/20', '獎號': ['25', '34', '11', '27', '37']},
        {'期別': '112000145', '開獎日期': '112/06/19', '獎號': ['36', '13', '01', '33', '39']},
        {'期別': '112000144', '開獎日期': '112/06/17', '獎號': ['36', '29', '09', '02', '20']},
        {'期別': '112000143', '開獎日期': '112/06/16', '獎號': ['09', '24', '39', '12', '28']},
        {'期別': '112000142', '開獎日期': '112/06/15', '獎號': ['18', '15', '21', '02', '11']},
        {'期別': '112000141', '開獎日期': '112/06/14', '獎號': ['06', '21', '34', '32', '01']},
        {'期別': '112000140', '開獎日期': '112/06/13', '獎號': ['29', '36', '37', '34', '24']},
        {'期別': '112000139', '開獎日期': '112/06/12', '獎號': ['13', '26', '08', '19', '22']},
        {'期別': '112000138', '開獎日期': '112/06/10', '獎號': ['19', '09', '08', '28', '01']},
        {'期別': '112000137', '開獎日期': '112/06/09', '獎號': ['15', '02', '17', '29', '13']},
        {'期別': '112000136', '開獎日期': '112/06/08', '獎號': ['15', '38', '12', '01', '23']},
        {'期別': '112000135', '開獎日期': '112/06/07', '獎號': ['11', '07', '08', '29', '03']},
        {'期別': '112000134', '開獎日期': '112/06/06', '獎號': ['11', '37', '29', '18', '26']},
        {'期別': '112000133', '開獎日期': '112/06/05', '獎號': ['20', '16', '05', '01', '29']},
        {'期別': '112000132', '開獎日期': '112/06/03', '獎號': ['23', '13', '03', '07', '34']},
        {'期別': '112000131', '開獎日期': '112/06/02', '獎號': ['04', '09', '08', '37', '22']},
        {'期別': '112000130', '開獎日期': '112/06/01', '獎號': ['25', '08', '27', '34', '18']}
    ]


def test_lotto1224():
    # Given user wants to get 雙贏彩 2023-06 result
    lottery = Lottery()

    # When user get the 雙贏彩 2023-06 result without print and output to json
    lotto1224_result = lottery.lotto1224(False, False, [112, 6])

    # Then the lotto1224_result should be equal to test result
    assert lotto1224_result == [
        {'期別': '112000155', '開獎日期': '112/06/30', '獎號': ['15', '20', '16', '02', '06', '24', '01', '10', '07', '12', '05', '14']},
        {'期別': '112000154', '開獎日期': '112/06/29', '獎號': ['05', '01', '12', '23', '06', '08', '02', '19', '04', '13', '24', '11']},
        {'期別': '112000153', '開獎日期': '112/06/28', '獎號': ['05', '21', '06', '19', '08', '10', '24', '13', '07', '04', '09', '23']},
        {'期別': '112000152', '開獎日期': '112/06/27', '獎號': ['08', '10', '09', '04', '07', '01', '24', '15', '22', '13', '16', '02']},
        {'期別': '112000151', '開獎日期': '112/06/26', '獎號': ['15', '04', '10', '17', '24', '05', '21', '07', '06', '18', '23', '16']},
        {'期別': '112000150', '開獎日期': '112/06/24', '獎號': ['20', '17', '15', '14', '22', '18', '01', '16', '19', '09', '05', '08']},
        {'期別': '112000149', '開獎日期': '112/06/23', '獎號': ['13', '12', '19', '04', '05', '03', '23', '16', '06', '10', '22', '20']},
        {'期別': '112000148', '開獎日期': '112/06/22', '獎號': ['23', '17', '04', '03', '19', '12', '14', '13', '09', '18', '21', '06']},
        {'期別': '112000147', '開獎日期': '112/06/21', '獎號': ['01', '07', '19', '13', '14', '12', '24', '23', '18', '10', '03', '22']},
        {'期別': '112000146', '開獎日期': '112/06/20', '獎號': ['01', '14', '23', '19', '05', '04', '07', '10', '03', '02', '18', '06']},
        {'期別': '112000145', '開獎日期': '112/06/19', '獎號': ['23', '09', '24', '22', '17', '04', '06', '16', '19', '03', '07', '11']},
        {'期別': '112000144', '開獎日期': '112/06/17', '獎號': ['08', '24', '13', '05', '02', '11', '04', '01', '20', '09', '16', '21']},
        {'期別': '112000143', '開獎日期': '112/06/16', '獎號': ['12', '14', '18', '09', '19', '08', '21', '22', '01', '23', '11', '03']},
        {'期別': '112000142', '開獎日期': '112/06/15', '獎號': ['18', '08', '02', '22', '09', '20', '24', '15', '19', '21', '04', '13']},
        {'期別': '112000141', '開獎日期': '112/06/14', '獎號': ['20', '18', '03', '06', '24', '19', '12', '23', '10', '13', '02', '04']},
        {'期別': '112000140', '開獎日期': '112/06/13', '獎號': ['02', '04', '23', '09', '10', '22', '16', '06', '24', '03', '21', '07']},
        {'期別': '112000139', '開獎日期': '112/06/12', '獎號': ['23', '24', '12', '01', '04', '09', '15', '02', '07', '03', '16', '06']},
        {'期別': '112000138', '開獎日期': '112/06/10', '獎號': ['17', '01', '23', '24', '12', '20', '08', '09', '18', '21', '15', '22']},
        {'期別': '112000137', '開獎日期': '112/06/09', '獎號': ['08', '09', '22', '16', '23', '05', '12', '20', '19', '10', '13', '04']},
        {'期別': '112000136', '開獎日期': '112/06/08', '獎號': ['07', '17', '05', '10', '24', '12', '04', '08', '03', '02', '22', '19']},
        {'期別': '112000135', '開獎日期': '112/06/07', '獎號': ['03', '02', '11', '23', '21', '07', '19', '01', '08', '14', '04', '09']},
        {'期別': '112000134', '開獎日期': '112/06/06', '獎號': ['02', '10', '12', '17', '21', '09', '24', '19', '13', '11', '16', '22']},
        {'期別': '112000133', '開獎日期': '112/06/05', '獎號': ['23', '02', '15', '19', '12', '06', '20', '14', '21', '08', '17', '03']},
        {'期別': '112000132', '開獎日期': '112/06/03', '獎號': ['05', '20', '22', '11', '23', '01', '15', '13', '16', '07', '14', '12']},
        {'期別': '112000131', '開獎日期': '112/06/02', '獎號': ['08', '12', '24', '01', '07', '15', '11', '18', '19', '06', '21', '14']},
        {'期別': '112000130', '開獎日期': '112/06/01', '獎號': ['23', '17', '10', '14', '20', '03', '05', '09', '15', '12', '07', '19']}
    ]
