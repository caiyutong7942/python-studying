from fine_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import TitleOpts,LabelOpts,InitOpts
from pyecharts.globals import ThemeType

text_file = TextFileReader("c:\\2011年1月销售数据.txt")
json_file = JsonFileReader("c:\\2011年2月销售数据JSON.txt")

jan_data = text_file.read_data()
feb_data = json_file.read_data()

all_data:list[Record] = jan_data + feb_data

dict_data = {}

for record in all_data:
    if record.date in dict_data:
        dict_data[record.date] += int(record.money)
    else:
        dict_data[record.date] = int(record.money)

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(dict_data.keys()))
bar.add_yaxis("销售额",list(dict_data.values()),label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")

print(dir(FileReader()))