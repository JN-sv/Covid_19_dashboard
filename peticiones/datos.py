import pandas as pd
import requests
import json
import os 


def get_url():
     return "http://localhost:5000/"
   
covid_dic = requests.get(f"{get_url()}/covid19").json()
df = pd.DataFrame(covid_dic) 
covid_= df.drop(columns=["date","ctry_name"])
covid_["date"] = covid_["year"].astype("str") + "-" + covid_["month"].astype("str")+ "-"+ covid_["day"].astype("str").str.rjust(2,"0")
covid_["date"] = pd.to_datetime(covid_["date"], format="%Y-%m-%d")
covid_.fillna(0)
europe_populations=covid_[['pais','poblacion']].drop_duplicates().sort_values(by='poblacion')
c_conta=covid_.pivot(index="date",columns="pais", values ="ctgios").fillna(0)
c_vac=covid_.pivot(index="date",columns="pais", values ="vacunas_dia").fillna(0)
vacu_month= covid_.groupby(["pais","year","month"]).agg({"vacunas_dia":"sum"}).reset_index()

ccaa_dic=requests.get(f"{get_url()}/ccaa").json()
ccaa={"AN":"Andalucía","AR":"Aragón","AS":"Asturias","CN":"Canarias","CB":"Cantabria","CE":"Ceuta","CM":"Castilla-La Mancha",\
    "CL":"Castilla y León","CT":"Cataluña", "EX":"Extremadura","GA":"Galicia", "IB":"Baleares", "RI":"La Rioja","ML":"Melilla",\
    "MD":"Madrid","MC":"Murcia","NC":"Navarra","PV":"País Vasco", "VC":"Valencia"}
casos_ccaa = pd.DataFrame(ccaa_dic) 
casos_ccaa["autonomia"]=casos_ccaa["ccaa_iso"].apply(lambda x:ccaa["".join([e for e in x ])])
casos_ccaa.drop(columns=["ccaa_iso"])
casos_ccaa["date"] = pd.to_datetime(casos_ccaa["fecha"], format="%Y-%m-%d")
casos_esp= casos_ccaa.groupby(["autonomia","fecha"]).agg({"num_casos":"sum"}).reset_index()
p_ccaa=casos_esp.pivot(index="fecha",columns="autonomia", values ="num_casos").fillna(0)

dspleo_dic = requests.get(f"{get_url()}/desempleo").json()
dsp_europa=pd.DataFrame(dspleo_dic)
desempl_europa=dsp_europa.melt(id_vars=["cntry_name"]).sort_values("cntry_name")\
    .rename(columns={"cntry_name":"pais","variable":"fecha","value":"desempleo"})
desempl_europa["year"]=desempl_europa["fecha"].apply(lambda x:int("20"+"".join([e for e in x if e.isnumeric()])))
mes_num = {"enero":1,"feb":2,"nov":11,"agost":8,"junio":6,'dic':12, 'sep':9,\
       'mayo':5, 'abril':4,"marzo":3,"julio":7,"octubre":10}
desempl_europa["month"]=desempl_europa["fecha"].apply(lambda x:mes_num["".join([e for e in x if  not e.isnumeric()])])
vacu_dsp_mes = pd.merge(vacu_month, desempl_europa, on=['year','month',"pais"]).drop(columns= ["fecha"])
#vacu_dsp_mes["date"] = pd.to_datetime(vacu_dsp_mes["date"], format="%Y-%m")
#vacu_des_mes = vacu_dsp_mes.drop(columns=["year", "month"])
#vacunas_desempleo = vacu_des_mes.set_index(['pais', 'date'])


