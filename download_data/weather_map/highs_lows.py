#coding=utf-8
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件获取日期和最高温度
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)
    #~ print(header_row)

    #~ for index, column_header in enumerate(header_row):
        #~ print(index, column_header)
    
    dates = []
    highs = []
    for row in reader:
        high = int(row[1])
        date = row[0]
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(high)
    
    #~ print(highs)
    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red')
    
    # 设置图形的格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperate (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
