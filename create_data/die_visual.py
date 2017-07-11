#coding=utf-8
import pygal
from die import Die

# 创建一个D6
die = Die()

# 掷骰，将结果存放在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# 分析结果
frequencies = []
numbers = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    numbers.append(value)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = numbers
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
