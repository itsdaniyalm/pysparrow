import pysparrow as psp
import pandas as pd

df = pd.read_csv('population.csv')
city = df['City'].to_list()
pop_2020 = df['Population 2020'].to_list()

psp.init(filename='chart_test', title='Bar Chart Test')

psp.row(
    col1 = psp.bar(title='Population of Pakistan Cities', labels=city, dtLabel='', dt=pop_2020)
)
