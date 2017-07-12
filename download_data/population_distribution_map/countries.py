#~ from pygal.i18n import COUNTRIES
# pygal2.0中已经没有i18n模块，放在pygal_maps_world中
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
