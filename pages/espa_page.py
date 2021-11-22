import streamlit as st
from streamlit import caching
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 
from peticiones import datos as pm


def espa():
    st.subheader("Datos contagios, fallecidos y vacunados en 2021)")
    selected_option= st.selectbox("Elige Autonomia", ["Andalucia","Asturias","Cantabria"])  