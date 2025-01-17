import json
import pyecharts.options as opts
from pyecharts.charts import Radar

f = open('../../data/users_analysis_source.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
g =open('../../data/updated_users_analysis_source.json', encoding='utf-8')
res2 = g.read()
data2 = json.loads(res2)
for k in data.keys():
    v1 = [data[k]["score"]]
    v2 = [data2[k]["score"]]
    for i in range(8):
        for j in range(8):
            v1[0][j] = round(v1[0][j], 2)
    for i in range(8):
        for j in range(8):
            v2[0][j] = round(v2[0][j], 2)

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
            series_name="学生平均得分",
            data=v1,
            linestyle_opts=opts.LineStyleOpts(color="#1098f7",width=3,opacity=0.7),
        )
            .add(
            series_name="学生实际平均得分",
            data=v2,
            linestyle_opts=opts.LineStyleOpts(color="#ff5722",width=3,opacity=0.7),
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(), legend_opts=opts.LegendOpts()
        )
            .render(k + "_radar_chart.html")
    )
