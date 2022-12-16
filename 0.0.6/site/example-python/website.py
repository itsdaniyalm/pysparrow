import pandas as pd
import piesparrow as ps

df = pd.read_csv('color.csv')

ps.init(filename='webtest', title='web test', basetheme=ps.dark, charttheme=ps.rainbow_dark)

ps.row(ps.donut(title="ch", df=df, columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10'],legend='false'))
