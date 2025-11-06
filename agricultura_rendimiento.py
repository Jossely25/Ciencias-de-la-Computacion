import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("Regresión múltiple - Agricultura - Ing Aguirre")
archivo = st.sidebar.file_uploader("Busca el archivo a subir")

if archivo is not None:
    # leer csv
    df = pd.read_csv(archivo)

    # definir variables
    x = df[["Fertilizante_kg_ha", "Riego_mm", "Horas_sol_diarias"]]
    y = df["Rendimiento_kg_ha"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # entrenar modelo
    model = LinearRegression()
    model.fit(x_train, y_train)

    # entrada de datos
    fertilizante = st.number_input("Ingrese la cantidad de fertilizante (kg/ha): ", min_value=0.0, step=0.1)
    riego = st.number_input("Ingrese la cantidad de riego (mm): ", min_value=0.0, step=0.1)
    horas_sol = st.number_input("Ingrese la cantidad de horas de sol diarias: ", min_value=0.0, step=0.1)

    if st.button("Predecir el rendimiento"):
        nuevo_dato = [[fertilizante, riego, horas_sol]]
        prediccion = model.predict(nuevo_dato)
        st.write("El rendimiento estimado de la cosecha es: ", prediccion[0], "kg/ha")

    # ---- Gráfica de regresión múltiple ----
    # Crear figura
    fig, ax = plt.subplots()

    # Dispersión de los datos reales (usando una variable como referencia)
    ax.scatter(x["Fertilizante_kg_ha"], y, color="blue", label="Datos reales")

    # Línea de tendencia para visualizar la relación
    predicciones = model.predict(x)
    ax.scatter(x["Fertilizante_kg_ha"], predicciones, color="red", label="Predicciones del modelo")

    # Etiquetas y título
    ax.set_xlabel("Fertilizante (kg/ha)")
    ax.set_ylabel("Rendimiento (kg/ha)")
    ax.set_title("Regresión múltiple")
    ax.legend()

    # Mostrar en Streamlit
    st.pyplot(fig)