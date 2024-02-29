from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from charts.chart import get_data_of_csv

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola mundo 🌎"}

@app.get("/data")
def get_home():
    labels, values, dataframe = get_data_of_csv('assets/csv/world_population.csv', "CCA3", "World Population Percentage", ('Continent', 'South America'))
    return  {
        "labels": list(labels),
        "values": list(values),
    }