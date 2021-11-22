from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

user =  os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")

url = f"mongodb+srv://{user}:{password}@cluster0.bbhb7.mongodb.net/covid19?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.get_database("covid19")
covi_data= db.covid_main
ccaa_data=db.casos_ccaa
desempleo = db.covid_dspleo
