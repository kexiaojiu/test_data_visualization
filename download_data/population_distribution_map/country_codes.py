#coding=utf-8
from pygal_maps_world.i18n import COUNTRIES

"""返回国别码"""
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
            
    # 如果没有找到指定国家就返回none
    return None
