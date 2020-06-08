# Taiwan Lottery Crawler
這個專案是用來爬取 [台灣彩券](https://www.taiwanlottery.com.tw/) 官網上歷史的開獎紀錄，目前支援**威力彩**、**大樂透**、**今彩539**、**雙贏彩** 4 種彩券遊戲。

## Features
- 爬取 威力彩、大樂透、今彩539、雙贏彩 4 種彩券遊戲的開獎紀錄。
- 爬取結果可直接輸出產生成 `json` 格式檔案進行後續使用。
- 針對單一的彩券遊戲可以爬取幾個月前的開獎紀錄。

## Requirements
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

## Install
```shell
$ git clone git@github.com:stu01509/TaiwanLotteryCrawler.git
$ cd TaiwanLotteryCrawler
$ pip install -r requirements.txt
```

## Command

### 爬取當月份的開獎紀錄
```shell
$ python crawl.py
```

### 爬取當月份的開獎紀錄並輸出
```shell
$ python crawl.py -o
```

### 往回爬取指定彩券的幾個月前的開獎紀錄
爬取 5 個月前的開獎資料
```shell
$ python crawl.py 威力彩 5
```

```shell
$ python crawl.py 大樂透 5
```

```shell
$ python crawl.py 今彩539 5
```

```shell
$ python crawl.py 雙贏彩 5
```

### 往回爬取指定彩券的幾個月前的開獎紀錄並輸出
爬取 5 個月前的開獎資料
```shell
$ python crawl.py 威力彩 5 -o
```

```shell
$ python crawl.py 大樂透 5 -o
```

```shell
$ python crawl.py 今彩539 5 -o
```

```shell
$ python crawl.py 雙贏彩 5 -o
```

## Data Source
- [威力彩](https://www.taiwanlottery.com.tw/Lotto/SuperLotto638/history.aspx)
- [大樂透](https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx)
- [今彩539](https://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx)
- [雙贏彩](https://www.taiwanlottery.com.tw/Lotto/Lotto1224/history.aspx)
## License
MIT License