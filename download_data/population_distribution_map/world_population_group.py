#coding=utf-8
import json
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle as RS
from pygal.style import LightColorizedStyle as LCS

# 将数据加载到一个列表中
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}

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
                cc_populations[code] = population
            else:
                print("ERROR - " + country_name + ": " + str(population))

# 根据人口把国家分为三组            
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
    

# 绘制世界人口分布地图
wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "World Population in 2010, by Country" 
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('> 1bn', cc_pops_3)

wm.render_to_file('world_population_group.svg')
