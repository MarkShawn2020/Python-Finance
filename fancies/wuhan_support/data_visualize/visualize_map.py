# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/1/26 13:04
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------


from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map, Geo
from pyecharts.globals import ChartType


def map_base() -> Map:
    c = (
        Map()
        .add(
            "商家A",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            "china",

        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    )
    return c

def geo_heatmap() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "geo",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_=ChartType.HEATMAP,

        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-HeatMap"),
        )
    )
    return c




# map = map_base()
# map = geo_heatmap()
# map.render()

guizhou_show()