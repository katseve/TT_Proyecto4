import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de conjunto de datos de anuncios de venta de coches")
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.checkbox('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de coches y su cuentakilómetros')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer", color='type')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


disp_button = st.checkbox('Construir gráfico de dispersión') # crear un botón

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de coches y su cuentakilómetros')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", color='type') 

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)