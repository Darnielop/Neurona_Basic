import streamlit as st
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import json
import numpy as np

st.image("img/neurona.png", width=250)
st.title("¡Hola Neurona!")
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])
salida = 0
with tab1:
    st.header("Una neurona con una entrada y un peso")
    peso = st.slider(
    'Peso',  # Etiqueta del slider
    min_value=0.0,            # Valor mínimo
    max_value=5.0,          # Valor máximo
    value=1.0,               # Valor inicial
    step=0.01                  # Incremento del valor
)
    entrada = st.number_input("Introduzca el valor de la entrada", min_value=0.00,value=0.00)
    if st.button("Calcular la salida", key="1"):
    # Realizar la multiplicación de peso y entrada
        salida = peso * entrada
        # Mostrar el resultado de la multiplicación
        st.write(f"La salida de la neurona es: {salida}")

with tab2:
    st.header("Una neurona con 2 entradas y 2 pesos")
    columns = st.columns(2)  # Esto crea un número de columnas igual al número de entradas
    
    #Crear los inputs dinámicamente en función del número de entradas seleccionadas
    pesos_values = []
    for i, col in enumerate(columns):
        with col:
            pesos_value = st.slider(f'Peso {i}', key=f"peso_{i}", min_value=0.0, max_value=5.0, value=1.0, step=0.01)
            pesos_values.append(pesos_value)
        
    columns_2 = st.columns(2)  # Esto crea un número de columnas igual al número de entradas

    # Crear los inputs dinámicamente en función del número de entradas seleccionadas
    entradas_values = []
    for i, col in enumerate(columns_2):
        with col:
            entrada_value = st.number_input(f'Entrada {i}', value=0.0, key=f"entrada_{i}")  # Entrada para cada peso
            entradas_values.append(entrada_value)


    if st.button("Calcular la salida", key="2"):
    # Realizar la multiplicación de peso y entrada
        salida = np.dot(pesos_values, entradas_values)
        # Mostrar el resultado de la multiplicación
        st.write(f"La salida de la neurona es: {salida}")
   
with tab3:
    st.header("Una neurona con 3 entradas y sesgo")
    columns = st.columns(3)  # Esto crea un número de columnas igual al número de entradas
    
    #Crear los inputs dinámicamente en función del número de entradas seleccionadas
    pesos_values = []
    for i, col in enumerate(columns):
        with col:
            pesos_value = st.slider(f'Peso {i}', key=f"pesos_{i}", min_value=0.0, max_value=5.0, value=1.0, step=0.01)
            pesos_values.append(pesos_value)
        
    columns_2 = st.columns(3)  # Esto crea un número de columnas igual al número de entradas

    # Crear los inputs dinámicamente en función del número de entradas seleccionadas
    entradas_values = []
    for i, col in enumerate(columns_2):
        with col:
            entrada_value = st.number_input(f'Entrada {i}', value=0.0, key=f"entradas_{i}")  # Entrada para cada peso
            entradas_values.append(entrada_value)

    sesgo = st.number_input("Introduzca el valor del sesgo", min_value=0.00,value=0.00)

    if st.button("Calcular la salida", key="3"):
    # Realizar la multiplicación de peso y entrada
        salida = np.dot(pesos_values, entradas_values) + sesgo
        # Mostrar el resultado de la multiplicación
        st.write(f"La salida de la neurona es: {salida}")

    
st.write("© Darío Nievas López")