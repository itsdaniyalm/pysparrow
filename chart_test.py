import pysparrow as psp
import pandas as pd

df = pd.read_csv('population.csv')
df2 = pd.read_csv('pop_province.csv')

psp.init(filename='combined_chart', title='Chart Test')
psp.icon = False
psp.row(
    col1w = 40  ,
    col1 = psp.line(
        title='Population trend of Provinces',
        dataframe= df2,
        xlabel = 'Year',
        ylabel1 = 'Balochistan',
        ydata1 = 'Balochistan',
        ylabel2 = 'KPK',
        ydata2 = 'KPK',
        ylabel3 = 'Punjab',
        ydata3 = 'Punjab',
        ylabel4 = 'Sindh',
        ydata4 = 'Sindh',
        height = 70,
    ),
    col2w = 40,
    col2 = psp.bar(
        title='Population of Pakistan Cities',
        dataframe = df,
        xlabel = 'City',
        ydata = 'Population 2020',
        ylabel = 'Population 2020',
        height = 50,
        legenddisplay = 'false'
        )
)
