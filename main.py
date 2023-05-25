import pandas as pd
from fastapi import FastAPI


app = FastAPI()


app.get("/{city_name}")
def get_city_population(city_name):
    my_data = pd.read_csv('data.csv')
    record = mydata[my_data["City"] == city_name]
    return {"male":record[record["Gender"]=="Male"]["Population"].sum(),"Female":record[record["Gender"]=="Female"]["Population"].sum()}
