import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("Regresión múltiple - Ambiente - Ing Aguirre")
archivo = st.sidebar.file_uploader("Busca el archivo a subir")

if archivo is not None:
    # leer csv
    df = pd.read_csv(archivo)

    # definir variables
    x = df[["Vehiculos_en_circulacion", "Vel_viento_m_s", "Temp_C"]]
    y = df["PM2_5_ug_m3"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # entrenar modelo
    model = LinearRegression()
    model.fit(x_train, y_train)

    # entrada de datos
    vehiculos_en_circulacion = st.number_input("Ingrese la cantidad de vehículos en circulación: ", min_value=0.0, step=1.0)
    vel_viento_m_s = st.number_input("Ingrese la velocidad del viento: ", min_value=0.0, step=0.1)
    temp_C = st.number_input("Ingrese la temperatura promedio (°C): ", min_value=-50.0, step=0.1)

    if st.button("Predecir el nivel de contaminación"):
        nuevo_dato = [[vehiculos_en_circulacion, vel_viento_m_s, temp_C]]
        prediccion = model.predict(nuevo_dato)
        st.write("El nivel de contaminación del aire: ", prediccion[0], "(PM2.5)")

    # ---- Gráfica de regresión múltiple ----
    # Crear figura
    fig, ax = plt.subplots()

    # Dispersión de los datos reales (usando vehículos como referencia)
    ax.scatter(x["Vehiculos_en_circulacion"], y, color="blue", label="Datos reales")

    # Línea de tendencia para visualizar la relación
    predicciones = model.predict(x)
    ax.scatter(x["Vehiculos_en_circulacion"], predicciones, color="red", label="Predicciones del modelo")

    # Etiquetas y título
    ax.set_xlabel("Vehículos en circulación")
    ax.set_ylabel("PM2.5 (μg/m³)")
    ax.set_title("Regresión múltiple")
    ax.legend()

    # Mostrar en Streamlit
    st.pyplot(fig)