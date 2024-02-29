from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola mundo 🌎"}

@app.get("/data", response_class=HTMLResponse)
def get_home():
    return """
        <h1>Hola mundo 🌎</h1>
    """ 