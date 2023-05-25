import pandas as pd
data = pd.read_csv("data.csv")
grouped_data = data[data["Gender"]== "Male"].groupby(["City","Gender"]).sum()
max_pop = max(grouped_data["Population"])
grouped_data[grouped_data["Population"] == max_pop]