import streamlit as st
from streamlit import caching
import plotly.express as px
from peticiones import datos as pm

def cero():

    st.image("./img/evicovid19.jpg")
    st. title("Covid19 en Europa 2021") 

    fig = px.bar(pm.europe_populations,
                x= pm.europe_populations["pais"],
                y =  pm.europe_populations["poblacion"],
                color =pm.europe_populations["pais"])
    fig.update_layout(width=900,height=700)  
    st.plotly_chart(fig)


    
    