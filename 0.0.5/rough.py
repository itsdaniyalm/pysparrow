import pandas as pd

pop = pd.read_csv('population.csv')

dataframe = pop

df = f'pd.{dataframe}'

xdata = 'City'

x_data = pop[xdata].tolist()

print(x_data)

