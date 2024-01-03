# Taiwan Lottery Crawler

[![PyPI](https://img.shields.io/pypi/v/taiwanlottery)](https://pypi.org/project/taiwanlottery/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/taiwanlottery)](https://pypi.org/project/taiwanlottery/)
[![CI Status](https://github.com/stu01509/TaiwanLotteryCrawler/actions/workflows/ci.yaml/badge.svg)](https://github.com/stu01509/TaiwanLotteryCrawler/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/gh/stu01509/TaiwanLotteryCrawler/branch/master/graph/badge.svg?token=AX0LW032B4)](https://codecov.io/gh/stu01509/TaiwanLotteryCrawler)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=stu01509_TaiwanLotteryCrawler&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=stu01509_TaiwanLotteryCrawler)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=stu01509_TaiwanLotteryCrawler&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=stu01509_TaiwanLotteryCrawler)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=stu01509_TaiwanLotteryCrawler&metric=bugs)](https://sonarcloud.io/summary/new_code?id=stu01509_TaiwanLotteryCrawler)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## 介紹

這個專案是用來爬取 [台灣彩券](https://www.taiwanlottery.com.tw/) 官網上歷史的開獎紀錄，目前支援**威力彩**、**大樂透**、**今彩539**、**雙贏彩**、**3星彩**、**4星彩**、**38樂合彩**、**39樂合彩**、**49樂合彩** 9 種彩券遊戲。

## 功能

- 爬取威力彩、大樂透、今彩539、雙贏彩、3星彩、4星彩、38樂合彩、39樂合彩、49樂合彩 9 種彩券遊戲的開獎紀錄。

## 環境需求

Python >= 3.6

## 安裝

```shell
pip install taiwanlottery
```

## 範例

### 爬取當月份的開獎紀錄

[威力彩](https://codesandbox.io/p/sandbox/dark-breeze-r2yfsf?file=%2Fmain.py%3A6%2C1)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.super_lotto()
print(result)
```

[大樂透](https://codesandbox.io/p/sandbox/wei-li-cai-dang-yue-fen-de-kai-jiang-ji-lu-forked-rt67ty)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto649()
print(result)
```

[今彩539](https://codesandbox.io/p/sandbox/da-le-tou-dang-yue-fen-de-kai-jiang-ji-lu-forked-n5t886)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.daily_cash()
print(result)
```

[雙贏彩](https://codesandbox.io/p/sandbox/da-le-tou-dang-yue-fen-de-kai-jiang-ji-lu-forked-vmlhst)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto1224()
print(result)
```

[3星彩](https://codesandbox.io/p/sandbox/3xing-cai-dang-yue-fen-de-kai-jiang-ji-lu-vsxs3p)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto3d()
print(result)
```

[4星彩](https://codesandbox.io/p/sandbox/4xing-cai-dang-yue-fen-de-kai-jiang-ji-lu-3pwkfk)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto4d()
print(result)
```

[38樂合彩](https://codesandbox.io/p/sandbox/38le-he-cai-dang-yue-fen-de-kai-jiang-ji-lu-yfphxf)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto38m6()
print(result)
```

[39樂合彩](https://codesandbox.io/p/sandbox/39le-he-cai-dang-yue-fen-de-kai-jiang-ji-lu-mgqwfg)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto39m5()
print(result)
```

[49樂合彩](https://codesandbox.io/p/sandbox/49le-he-cai-dang-yue-fen-de-kai-jiang-ji-lu-jgy94n)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto49m6()
print(result)
```

---

### 爬取指定年月的開獎紀錄(YYYY-MM)

[威力彩](https://codesandbox.io/p/sandbox/da-le-tou-dang-yue-fen-de-kai-jiang-ji-lu-forked-ksq74y)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.super_lotto(['2023', '06'])
print(result)
```

[大樂透](https://codesandbox.io/p/sandbox/wei-li-cai-zhi-ding-nian-yue-de-kai-jiang-ji-lu-forked-lqcfht)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto649(['2023', '06'])
print(result)
```

[今彩539](https://codesandbox.io/p/sandbox/wei-li-cai-zhi-ding-nian-yue-de-kai-jiang-ji-lu-forked-ntvjp7)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.daily_cash(['2023', '06'])
print(result)
```

[雙贏彩](https://codesandbox.io/p/sandbox/wei-li-cai-zhi-ding-nian-yue-de-kai-jiang-ji-lu-forked-22dtrx)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto1224(['2023', '06'])
print(result)
```

[3星彩](https://codesandbox.io/p/sandbox/3xing-cai-zhi-ding-nian-yue-de-kai-jiang-ji-lu-vsfvlx)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto3d(['2023', '08'])
print(result)
```

[4星彩](https://codesandbox.io/p/sandbox/4xing-cai-zhi-ding-nian-yue-de-kai-jiang-ji-lu-r8fpxq)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto4d(['2023', '08'])
print(result)
```

[38樂合彩](https://codesandbox.io/p/sandbox/38le-he-cai-zhi-ding-nian-yue-de-kai-jiang-ji-lu-m4s9jn)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto38m6(['2023', '08'])
print(result)
```

[39樂合彩](https://codesandbox.io/p/sandbox/39le-he-cai-zhi-ding-nian-yue-de-kai-jiang-ji-lu-lskqmm)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto39m5(['2023', '08'])
print(result)
```

[49樂合彩](https://codesandbox.io/p/sandbox/49le-he-cai-zhi-ding-nian-yue-de-kai-jiang-ji-lu-ff6d5d)

```python
from TaiwanLottery import TaiwanLotteryCrawler

lottery = TaiwanLotteryCrawler()
result = lottery.lotto49m6(['2023', '08'])
print(result)
```

## 資料來源

- [https://www.taiwanlottery.com/lotto/history/history_result/](https://www.taiwanlottery.com/lotto/history/history_result/)

## License

MIT License
