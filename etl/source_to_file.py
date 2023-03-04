from urllib.request import urlretrieve

url = "https://www.bankofengland.co.uk/-/media/boe/files/statistics/gold/gold-data.xlsx?la=en&hash=42A623758068AD019D1C3C81F0A9FBF38EB81402"
urlretrieve(url, "../gold-data.XLSX")
