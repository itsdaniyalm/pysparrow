import piesparrow as ps
import pandas as pd

df = pd.read_csv('population.csv')

ps.init(filename='hello_world', title='Hello World')


df = pd.read_csv('population.csv')
ps.row(
    col1 = ps.pie(
        title = 'Population of Cities',
        dataframe = df,
        labels = 'City',
        data = 'Population 2020',
        height = 400,
        color = ps.dusktilldawn
    )
)
#ps.row(
#    col1= ps.table(df)
#)