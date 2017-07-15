#!/usr/bin/env python
#conding=utf-8
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#改变标准输出的默认编码 
import io  
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

languages = ['python', 'javascrip', 'ruby', 'c', 'java', 'perl', 'haskell', 'go']
for language in languages:
    # 执行API调用并存储响应
    url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars'
    r = requests.get(url)
    print(url + " --- Status code: ", r.status_code)
    if r.status_code != 200:
        print("\nBad url: " + url + "\n")
        continue
        
    # 将API响应存储在一个变量中
    response_dict = r.json()

    # 处理结果
    print(response_dict.keys())
    print("Total repositories: ", response_dict['total_count'])

    # 搜索有关仓库的信息
    repo_dicts = response_dict['items']
    print("Repositories returned: ", len(repo_dicts))

    names, plot_dicts = [],[]
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        #~ print('Name:', repo_dict['name'])
        #~ print('Owner: ', repo_dict['owner'])
        #~ print('Stars:', repo_dict['stargazers_count'])
        #~ print('Repository:', repo_dict['html_url'])
        #~ print('Description:', repo_dict['description'])
        names.append(repo_dict['name'])
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': str(repo_dict['description']),
            'xlink': repo_dict['html_url']
            }
        plot_dicts.append(plot_dict)

    # 可视化
    my_style = LS('#333366', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size =18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred' + language.title() + 'Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    file_name = language + '_repos_plot_dicts.svg'
    chart.render_to_file(file_name)
