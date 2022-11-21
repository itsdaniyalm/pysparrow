import pysparrow as psp
import pandas as pd

df = pd.read_csv('population.csv')

psp.init(filename='chart_test', title='Bar Chart Test')

psp.row(
    col1 = psp.bar(title='Population of Pakistan Cities', labels=df.City, dtLabel='2020 Pop', dt=df['Population 2020'])
)
