#coding=utf-8
import json
from country_codes import get_country_code
import pygal

# 将数据加载到一个列表中
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

cc_populatioms = {}

# 打印每个国家2010年人口的数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        try:
            country_name = pop_dict['Country Name']
            population = int(float((pop_dict['Value'])))
            code = get_country_code(country_name)
        except ValueError:
            print("The number of the population in " + country_name +
                    " is not right formation.")
        else:
            if code:
                print(code + ": " + country_name + ": " + str(population))
                cc_populatioms[code] = population
            else:
                print("ERROR - " + country_name + ": " + str(population))
            

# 绘制世界人口分布地图
wm = pygal.maps.world.World()
wm.title = "World Population in 2010, by Country" 
wm.add('2010', cc_populatioms)

wm.render_to_file('world_population.svg')
