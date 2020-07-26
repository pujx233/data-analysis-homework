import json
import pyecharts.options as opts
from pyecharts.charts import Radar

f = open('../data/users_analysis_source.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

for k in data.keys():
    v=[data[k]["score"]]


    (
        Radar(init_opts=opts.InitOpts())
            .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="字符串", max_=100),
                opts.RadarIndicatorItem(name="图结构", max_=100),
                opts.RadarIndicatorItem(name="树结构", max_=100),
                opts.RadarIndicatorItem(name="数字操作", max_=100),
                opts.RadarIndicatorItem(name="排序算法", max_=100),
                opts.RadarIndicatorItem(name="查找算法", max_=100),
                opts.RadarIndicatorItem(name="数组", max_=100),
                opts.RadarIndicatorItem(name="线性表", max_=100),

            ],
            splitarea_opt=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
            textstyle_opts=opts.TextStyleOpts(color="#000"),
        )

            .add(
            series_name="得分分布",
            data=v,
            linestyle_opts=opts.LineStyleOpts(color="#ff5722",width=3,opacity=0.7),
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(), legend_opts=opts.LegendOpts()
        )
            .render(k + "_radar_chart.html")
    )
