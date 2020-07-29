import json
import pyecharts.options as opts
from pyecharts.charts import Radar

f = open('../../data/simplified_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

for k in data.keys():
    v=[data[k]["final"]]
    for i in range(7):
        for j in range(7):
            v[0][j] = round(v[0][j], 2)


    (
        Radar(init_opts=opts.InitOpts())
            .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="题目难度评分", max_=100),
                opts.RadarIndicatorItem(name="其它语言占比", max_=100),
                opts.RadarIndicatorItem(name="面向用例编程题目占比", max_=100),
                opts.RadarIndicatorItem(name="平均分", max_=100),
                opts.RadarIndicatorItem(name="有效满分占比", max_=100),
                opts.RadarIndicatorItem(name="抄袭占比", max_=100),
                opts.RadarIndicatorItem(name="通过率", max_=100),

            ],
            splitarea_opt=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
            textstyle_opts=opts.TextStyleOpts(color="#000"),
        )

            .add(
            series_name="题目分析",
            data=v,
            linestyle_opts=opts.LineStyleOpts(color="#ff5722",width=3,opacity=0.7),
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(), legend_opts=opts.LegendOpts()
        )
            .render(k + "_radar_chart.html")
    )

