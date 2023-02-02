import mongoengine
from openpyxl import load_workbook
from Schema import TimeSeries


def process_data():
    workbook = load_workbook("gold-data.XLSX")
    sheet = workbook.active
    dates = []
    values = []
    percentages = []

    for cell in sheet["B"]:
        if cell.value is not None:
            _date = cell.value
            if type(_date) is not str:
                dates.append(_date)

    for cell in sheet["A"]:
        if cell.value is not None:
            _date = cell.value
            if type(_date) is not str:
                dates.append(_date)

    for cell in sheet["C"]:
        if cell.value is not None:
            _val = cell.value
            if type(_val) is not str:
                values.append(_val)

    for cell in sheet["D"]:
        if cell.value is not None:
            _val = cell.value
            if type(_val) is not str:
                percentages.append(_val)
    percentages.insert(0, 0)

    for date, value, per in zip(dates, values, percentages):
        data = TimeSeries(
            date=str(date),
            value=value,
            percentage_change=per
        )
        print(f"{date} : {value} : {per}: {data}")
        data.save()


def connect_mongoengine():
    mongoengine.connect(host="mongodb://localhost:27017/gold-data")


if __name__ == "__main__":
    connect_mongoengine()
    process_data()
