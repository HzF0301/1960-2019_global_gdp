from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *


with open('D:/dev/python-learn/1960-2019全球GDP数据.csv', 'r', encoding='GB2312') as f:
    dataset = f.readlines()
del dataset[0]

dict_data = {}
for line in dataset:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    gdp = float(line.split(',')[2])

    try:
        dict_data[year].append([country, gdp])
    except Exception:
        dict_data[year] = []
        dict_data[year].append([country, gdp])

timeline = Timeline({'theme': ThemeType.LIGHT})

sort_year_list = sorted(dict_data.keys())

for year in sort_year_list:
    dict_data[year].sort(key=lambda element: element[1], reverse=True)
    country_gdp_list = dict_data[year][:8]
    country_data = []
    gdp_data = []
    for country_gdp in country_gdp_list:
        country_data.append(country_gdp[0])
        gdp_data.append(country_gdp[1] / 100000000)

    bar = Bar()
    country_data.reverse()
    gdp_data.reverse()
    bar.add_xaxis(country_data)
    bar.add_yaxis('GDP(亿)', gdp_data, label_opts=LabelOpts(position='right'))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f'{year}年全球GDP变化')
    )
    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=500,
    is_auto_play=True,
    is_timeline_show=True,
    is_loop_play=False
)

timeline.render("1960-2019全球前8国家GDP变化.html")


