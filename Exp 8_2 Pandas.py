import pandas as pd 
data = pd.read_csv("cars.csv") 
a = data.iloc[0:5, 0::2]
b = data.iloc[0:1]
c = data.loc[[23],["Model","cyl"]]
d = data.loc[[1,28,18],["Model","cyl","gear"]]
