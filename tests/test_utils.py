# -*- coding: utf-8 -*-
from TaiwanLottery import utils


def test_convert_to_republic_era_month():
    # Given user wants to convert 2023-06
    # When user get the 2023-06 convert result
    republic_era_month_result = utils.convert_to_republic_era_month('2023-06')

    # Then the republic_era_month_result should be equal to [112, 6]
    assert republic_era_month_result == [112, 6]
