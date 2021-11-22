from utils.db_conect import covi_data,ccaa_data,desempleo
import pandas as pd
from flask import Flask
from utils.json_srlz import serialize
import json
import os

q= {}
project= {"_id":0}

app = Flask("covid_api")

@app.route("/covid19")
@serialize
def covid_main():
    covid =pd.DataFrame(covi_data.find(q,project))
    return covid

@app.route("/ccaa")
@serialize
def ccaa_datos():
    ccaa = pd.DataFrame(ccaa_data.find(q,project))
    return ccaa

@app.route("/desempleo")
@serialize
def desempl():
    dsp = pd.DataFrame(desempleo.find(q,project))
    return dsp

port = os.getenv("PORT") or 5000
app.run(debug=True, port=port, host="0.0.0.0")