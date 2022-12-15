import pandas as pd
import piesparrow as ps

data = pd.read_csv('mock-data.csv')

ps.init(filename = 'myChart',title = 'My Chart')

ps.row(
	ps.chart(
		title = 'myChart',
		df = data,
		columns = ['Month','Data 1'],
		xcolumn = 'Month',
		type = 'bar'
   )
) 