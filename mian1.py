from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import TitleOpts, LabelOpts, InitOpts

from data_define import *
from file_define import *

text_file_reader = TextReader('D:/dev/python-learn/2011年1月销售数据.txt')
json_file_reader = JsonReader('D:/dev/python-learn/2011年2月销售数据JSON.txt')

Jan_data: list[Record] = text_file_reader.read_data()
Feb_data: list[Record] = json_file_reader.read_data()

all_data: list[Record] = Jan_data + Feb_data

record_dict = {}
for record in all_data:
    if record.date in record_dict.keys():
        record_dict[record.date] += record.money
    else:
        record_dict[record.date] = record.money

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(record_dict.keys()))
bar.add_yaxis('销售额', list(record_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')
)

bar.render('每日销售额柱状图.html')







