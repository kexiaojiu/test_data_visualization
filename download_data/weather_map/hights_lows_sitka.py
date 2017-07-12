#coding=utf-8
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件获取日期和最高温度、最低气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)
    #~ print(header_row)

    #~ for index, column_header in enumerate(header_row):
        #~ print(index, column_header)
    
    dates = []
    highs = []
    lows = []
    for row in reader:
        high = int(row[1])
        low = int(row[3])
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
    #~ print(highs)
    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # 设置图形的格式
    plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperate (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
