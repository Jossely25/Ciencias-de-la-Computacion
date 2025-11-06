import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("Regresión múltiple - Economía - Ing Aguirre")
archivo = st.sidebar.file_uploader("Busca el archivo a subir")

if archivo is not None:
    # leer csv
    df = pd.read_csv(archivo)

    # definir variables
    x = df[["Tipo_cambio", "Tasa_interes_pct", "Importaciones_millones"]]
    y = df["Inflacion_pct"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # entrenar modelo
    model = LinearRegression()
    model.fit(x_train, y_train)

    # entrada de datos
    tipo_cambio = st.number_input("Ingrese el tipo de cambio: ", min_value=0.0, step=0.01)
    tasa_interes_pct = st.number_input("Ingrese la tasa de interés en decimal: ", min_value=0.0, step=0.01)
    importaciones_millones = st.number_input("Ingrese el nivel de importaciones: ", min_value=0.0, step=1.0)

    if st.button("Predecir la inflación"):
        nuevo_dato = [[tipo_cambio, tasa_interes_pct, importaciones_millones]]
        prediccion = model.predict(nuevo_dato)
        st.write("La inflación mensual de un país: ", prediccion[0])

    # ---- Gráfica de regresión múltiple ----
    # Crear figura
    fig, ax = plt.subplots()

    # Dispersión de los datos reales (usando tipo de cambio como referencia)
    ax.scatter(x["Tipo_cambio"], y, color="blue", label="Datos reales")

    # Línea de tendencia para visualizar la relación
    predicciones = model.predict(x)
    ax.scatter(x["Tipo_cambio"], predicciones, color="red", label="Predicciones del modelo")

    # Etiquetas y título
    ax.set_xlabel("Tipo de cambio")
    ax.set_ylabel("Inflación (%)")
    ax.set_title("Regresión múltiple")
    ax.legend()

    # Mostrar en Streamlit
    st.pyplot(fig)