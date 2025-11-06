import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("Regresión múltiple - Deportes - Ing Aguirre")
archivo = st.sidebar.file_uploader("Busca el archivo a subir")

if archivo is not None:
    # leer csv
    df = pd.read_csv(archivo)

    # definir variables
    x = df[["Edad", "Porc_grasa", "Horas_entrenamiento_sem"]]
    y = df["Distancia_km_por_partido"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # entrenar modelo
    model = LinearRegression()
    model.fit(x_train, y_train)

    # entrada de datos
    edad = st.number_input("Ingrese la Edad: ", min_value=0.0, step=1.0)
    porc_grasa = st.number_input("Ingrese el porcentaje de grasa corporal: ", min_value=0.0, step=0.1)
    horas_entrenamiento_sem = st.number_input("Ingrese las horas de entrenamiento semanal: ", min_value=0.0, step=0.1)

    if st.button("Predecir el rendimiento físico"):
        nuevo_dato = [[edad, porc_grasa, horas_entrenamiento_sem]]
        prediccion = model.predict(nuevo_dato)
        st.write("El rendimiento físico de un futbolista es: ", prediccion[0], "distancia recorrida en km por partido")

    # ---- Gráfica de regresión múltiple ----
    # Crear figura
    fig, ax = plt.subplots()

    # Dispersión de los datos reales (usando edad como referencia)
    ax.scatter(x["Edad"], y, color="blue", label="Datos reales")

    # Línea de tendencia para visualizar la relación
    predicciones = model.predict(x)
    ax.scatter(x["Edad"], predicciones, color="red", label="Predicciones del modelo")

    # Etiquetas y título
    ax.set_xlabel("Edad")
    ax.set_ylabel("Distancia km por partido")
    ax.set_title("Regresión múltiple")
    ax.legend()

    # Mostrar en Streamlit
    st.pyplot(fig)