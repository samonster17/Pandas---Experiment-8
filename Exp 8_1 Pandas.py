import pandas as pd 
data = pd.read_csv("cars.csv") 
df = pd.DataFrame
first5 = data[:5]  # same as df.head(5)
last5 = data[-5:] # same as df.tail(5)
