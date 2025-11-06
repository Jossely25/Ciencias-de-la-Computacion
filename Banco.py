import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

st.title("KNN - Clasificación Banco - Ing Aguirre")
archivo = st.sidebar.file_uploader("Busca el archivo a subir")

if archivo is not None:
    # leer csv con punto y coma como separador
    data = pd.read_csv(archivo, sep=';')

    # definir variables
    x = data[["Monto", "Hora", "Intentos_PIN", "Operacion"]]
    y = data["Resultado"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42
    )

    # escalar datos
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # entrenar modelo
    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(x_train, y_train)

    # mostrar precisión
    accuracy = knn.score(x_test, y_test)
    st.write("Precisión del modelo:", round(accuracy, 2))

    # entrada de datos
    monto = st.number_input("Ingrese el monto: ", min_value=0, step=1)
    hora = st.number_input("Ingrese la hora: ", min_value=0, max_value=23, step=1)
    intentos_pin = st.number_input("Ingrese los intentos de PIN: ", min_value=0, step=1)
    operacion = st.number_input("Ingrese la operacion (0 para consulta y 1 para retiro): ", min_value=0, max_value=1, step=1)

    if st.button("Clasificar usuario"):
        nuevo_usuario = [[monto, hora, intentos_pin, operacion]]
        nuevo_usuario = scaler.transform(nuevo_usuario)
        prediccion = knn.predict(nuevo_usuario)
        st.write("El nuevo usuario se clasifica como:", prediccion[0])

    # ---- Gráfica de dispersión ----
    # Crear figura
    fig, ax = plt.subplots()

    # Dispersión de los datos por clase (usando monto vs hora)
    for clase in data["Resultado"].unique():
        mask = data["Resultado"] == clase
        ax.scatter(data.loc[mask, "Monto"], data.loc[mask, "Hora"], 
                  label=f"Clase {clase}", alpha=0.6)

    # Etiquetas y título
    ax.set_xlabel("Monto")
    ax.set_ylabel("Hora")
    ax.set_title("Clasificación KNN")
    ax.legend()

    # Mostrar en Streamlit
    st.pyplot(fig)