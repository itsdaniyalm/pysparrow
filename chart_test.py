import piesparrow as psp
import pandas as pd

df = pd.read_csv('population.csv')
df2 = pd.read_csv('pop_province.csv')
df3 = pd.read_csv('population.csv')

psp.init(filename='chart_test_pie', title='Chart Test', icon=True)
psp.row(
    col1w = 100,
    col1 = psp.p('Heading'+ psp.bold('This is bold text')) 
)
psp.row(
    col1w = 50  ,
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
        legenddisplay = 'true'
    ),
    col2w = 50,
    col2 = psp.bar(
        title='Population of Pakistan Cities',
        dataframe = df,
        xlabel = 'City',
        ydata = 'Population 2020',
        ylabel = 'Population 2020',
        height = 70,
        legenddisplay = 'false',
        color = psp.rainbow
        )
)
psp.row(
    col1w = 50,
    col1 = psp.pie(
        title = 'Population of Cities',
        dataframe = df3,
        labels = 'City',
        data = 'Population 2020',
        height = 400
    )
)
psp.row(
    col1w = 50,
    col1 = psp.img('https://raw.githubusercontent.com/itsdaniyalm/pysparrow-dev/master/images/logo.png', width='25', height='25')
)