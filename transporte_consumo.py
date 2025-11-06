import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("Regresión múltiple - Transporte - Ing Aguirre")
archivo = st.sidebar.file_uploader("Busca el archivo a subir")

if archivo is not None:
    # leer csv
    df = pd.read_csv(archivo)

    # definir variables
    x = df[["Velocidad_prom_kmh", "Peso_carga_kg", "Pasajeros"]]
    y = df["Consumo_l_100km"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # entrenar modelo
    model = LinearRegression()
    model.fit(x_train, y_train)

    # entrada de datos
    velocidad_prom_kmh = st.number_input("Ingrese la velocidad promedio (kmh): ", min_value=0.0, step=1.0)
    peso_carga_kg = st.number_input("Ingrese el peso de la carga (kg): ", min_value=0.0, step=1.0)
    pasajeros = st.number_input("Ingrese el número de pasajeros: ", min_value=0.0, step=1.0)

    if st.button("Predecir el consumo de combustible"):
        nuevo_dato = [[velocidad_prom_kmh, peso_carga_kg, pasajeros]]
        prediccion = model.predict(nuevo_dato)
        st.write("El consumo de combustible de un vehículo: ", prediccion[0], "litros/100 km")

    # ---- Gráfica de regresión múltiple ----
    # Crear figura
    fig, ax = plt.subplots()

    # Dispersión de los datos reales (usando velocidad como referencia)
    ax.scatter(x["Velocidad_prom_kmh"], y, color="blue", label="Datos reales")

    # Línea de tendencia para visualizar la relación
    predicciones = model.predict(x)
    ax.scatter(x["Velocidad_prom_kmh"], predicciones, color="red", label="Predicciones del modelo")

    # Etiquetas y título
    ax.set_xlabel("Velocidad promedio (kmh)")
    ax.set_ylabel("Consumo (litros/100km)")
    ax.set_title("Regresión múltiple")
    ax.legend()

    # Mostrar en Streamlit
    st.pyplot(fig)