import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Análisis del dataset de vehículos')

hist_checkbox = st.checkbox('Construir un histograma')
hist_button = st.button('Construir histograma') # crear un botón
hist_fig = px.histogram(car_data, x="odometer")
disper_fig = px.scatter(car_data, x="odometer", y="price")

if hist_checkbox: # si la casilla de verificación está seleccionada
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    st.plotly_chart(hist_fig, use_container_width=True, key='chart_hist_cbox')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(hist_fig, use_container_width=True, key='chart_hist_btn')

disp_checkbox = st.checkbox('Construir un gráfico de dispersión')
disp_button = st.button('Construir un gráfico de dispersión') # crear un botón

if disp_checkbox:
    st.write('Construir un gráfico de diespersión entre el odómetro y precio')
    st.plotly_chart(disper_fig, use_container_width=True, key='chart_dis_cbox')

if disp_button:
    st.write('Construir un gráfico de diespersión entre el odómetro y precio')
    st.plotly_chart(disper_fig, use_container_width=True, key='chart_but_cbox')    
