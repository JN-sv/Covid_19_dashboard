import streamlit as st
from streamlit import caching
import pandas as pd
import plotly.express as px 
from peticiones import datos as pm


def euro():
    st.subheader("Datos contagios, fallecidos y vacunados en 2021)")  
    fig = px.funnel(pm.covid_,
                x= pm.covid_["pais"],
                y =  pm.covid_["ctgios"],
                color =pm.covid_["pais"])
    fig.update_layout(width=900,height=700)  
    st.plotly_chart(fig)
        

    
    