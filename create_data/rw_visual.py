#coding=utf-8
import matplotlib.pyplot as plt
from random_walk import RandomWalk

#~ # 创建一个RandomwWalk实例
#~ rw = RandomWalk()
#~ rw.fill_walk()
#~ plt.scatter(rw.x_values, rw.y_values, s=15)
#~ plt.title("Random Walk")
#~ plt.show()

# 只要程序处于激活状态就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置图标尺寸，必须放在绘图函数最前面
    plt.figure(figsize=(10,6))
    # 设置标题
    plt.title("Random Walk")
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=0.5)
    # 突出起点和终点
    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolor='none', 
        s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', 
        s=100)  
        
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
          
    plt.show()
    
    keep_running = input("Make another walk?(y/n)? ")
    if keep_running.lower() == 'n':
        break
