import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt   # <-- importante, usa pyplot
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("Regresión lineal - Ing. Aguirre")
archivo = st.sidebar.file_uploader("Busca el archivo a subir")

if archivo is not None:
    # leer csv
    df = pd.read_csv(archivo)
    df
    # definir variables
    x = df[["Tecnicos_asignados"]]
    y = df["Tiempo_resolucion_horas"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # entrenar modelo
    modelo = LinearRegression()
    modelo.fit(x_train, y_train)

    # entrada de datos
    nuevos_ta = st.number_input("Digite la cantidad de técnicos: ", min_value=1, step=1)

    if st.button("Predecir el tiempo de respuesta"):
        prediccion = modelo.predict([[nuevos_ta]])
        st.write("El tiempo estimado es: ", prediccion[0])

    # ---- Gráfica de dispersión ----
    # Crear figura
    fig, ax = plt.subplots()

    # Dispersión de los datos reales
    ax.scatter(x, y, color="blue", label="Datos reales")

    # Recta de regresión
    x_linea = pd.DataFrame({"Tecnicos_asignados": range(int(x.min()), int(x.max())+1)})
    y_linea = modelo.predict(x_linea)
    ax.plot(x_linea, y_linea, color="red", label="Modelo")

    # Etiquetas y título
    ax.set_xlabel("Técnicos asignados")
    ax.set_ylabel("Tiempo de resolución (horas)")
    ax.set_title("Regresión lineal")
    ax.legend()

    # Mostrar en Streamlit
    st.pyplot(fig)

