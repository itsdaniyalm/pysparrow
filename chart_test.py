import pysparrow as psp
import pandas as pd

df = pd.read_csv('population.csv')

psp.init(filename='chart_test_2', title='Bar Chart Test')
psp.icon = False
psp.row(
    col1 = psp.bar(
        title='Population of Pakistan Cities',
        dataframe = df,
        xlabel = 'City',
        xdata = 'Population 2020',
        ylabel = 'Population 2020'
        )
)
