from pyecharts.charts import Line
line=Line()
line.add_xaxis(["中国","美国","俄罗斯"])
line.add_yaxis("GDP",[20,30,15])
line.render()