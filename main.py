import streamlit as st
from streamlit import caching
import plotly.express as px
from peticiones import datos as pm
import pages.euro_page as ep
import pages.espa_page as pe
import pages.cero_page as cero


#st.set_page_config(page_title=" Covid19 en Europa 2021", layout="wide",initial_sidebar_state="auto")

st.sidebar.image('./img/covid_19.gif')
selector=st.sidebar.selectbox("Elige datos",["_","Europa","España"])

if selector == "España":
    pe.espa()
    
elif selector == "Europa":
    ep.euro()
else:
    cero.cero()
