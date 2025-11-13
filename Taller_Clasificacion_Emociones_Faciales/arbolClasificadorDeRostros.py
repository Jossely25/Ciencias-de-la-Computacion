# Clasificador - arbol de decisiones
# clasificacion de emociones faciales por género
# librerias requeridas
import os 
import tkinter as tk
from tkinter import Tk, Label, Button, filedialog
from sklearn.tree import DecisionTreeClassifier
import cv2
import joblib
from PIL import Image, ImageTk

# SE AGREGO ESTE CODIGO ADICIONAL: IMPORTA LIBRERIA PARA DIVIDIR DATOS DE ENTRENAMIENTO Y TEST
from sklearn.model_selection import train_test_split

# SE AGREGO ESTE CODIGO ADICIONAL: PERMITE MEDIR LA PRECISION DEL MODELO
from sklearn.metrics import accuracy_score

# Ruta de imagenes, tamaño de imagenes, guardar .plk entrenado
ruta_imagenes = r"C:\clases\Taller_Clasificacion_Emociones_Faciales\imagenes"
img_size = (100, 100)
ruta_modelo = r"C:\clases\Taller_Clasificacion_Emociones_Faciales\modelo_emociones_faciales.pkl"

# entrenamiento del modelo
if not os.path.exists(ruta_modelo):
    X, Y = [], []

    # Recorrer las carpetas de género (mujeres y hombres)
    for genero in os.listdir(ruta_imagenes):
        carpeta_genero = os.path.join(ruta_imagenes, genero)
        if not os.path.isdir(carpeta_genero):
            continue
        
        # Recorrer las carpetas de emociones (feliz, triste, enojada/enojado)
        for emocion in os.listdir(carpeta_genero):
            carpeta_emocion = os.path.join(carpeta_genero, emocion)
            if not os.path.isdir(carpeta_emocion):
                continue
            
            # Crear etiqueta combinada: genero_emocion
            etiqueta = f"{genero}_{emocion}"
            
            # Recorrer los archivos de imagen en cada carpeta de emoción
            for archivo in os.listdir(carpeta_emocion):
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    ruta = os.path.join(carpeta_emocion, archivo)
                    imagen = cv2.imread(ruta)
                    imagen = cv2.resize(imagen, img_size)
                    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
                    X.append(imagen.flatten())
                    Y.append(etiqueta)

    # ESTE CODIGO DIVIDE LOS DATOS EN ENTRENAMIENTO Y TEST
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=40)

    # creacion del arbol de decision y entrenamiento
    clasificador = DecisionTreeClassifier() # crea el modelo Arbol de decisiones para clasificacion

    clasificador.fit(X_train, Y_train)
    # REALIZA LA PREDICCION CON LOS DATOS DE X
    Y_pred = clasificador.predict(X_test)

    precision = accuracy_score(Y_test, Y_pred)

    print(f"La precision de este modelo es de: {precision * 100:.2f}%")

    # Guarda el modelo pre-entrenado    
    joblib.dump(clasificador, ruta_modelo)

else:
    clasificador = joblib.load(ruta_modelo)

# Entorno grafico
ventana = tk.Tk()
ventana.title("Clasificador de Emociones Faciales")
ventana.geometry("450x500")

# Título principal
titulo = tk.Label(ventana, text="Clasificador de Género y Emoción", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# esta etiqueta mostrará la imagen cargada para que sea clasificada
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

# Etiqueta para mostrar el género
etiqueta_genero = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_genero.pack(pady=5)

# Etiqueta para mostrar la emoción
etiqueta_emocion = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_emocion.pack(pady=5)

# Etiqueta para mostrar el resultado completo
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), fg="blue")
etiqueta_resultado.pack(pady=10)

# Funcion para cargar y clasificar imagenes
def cargar_y_predecir():
    ruta_archivo = filedialog.askopenfilename(title="Seleccione una imagen de rostro", 
                                                filetypes=[("Imagenes", "*.jpg;*.png;*.jpeg;*.webp")])

    if not ruta_archivo:
        return

    imagen_pil = Image.open(ruta_archivo)
    imagen_pil.thumbnail((250, 250))
    imagen_tk = ImageTk.PhotoImage(imagen_pil)
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk

    # procesamiento de la nueva imagen
    imagen_cv = cv2.imread(ruta_archivo)
    imagen_cv = cv2.resize(imagen_cv, img_size)
    imagen_cv = cv2.cvtColor(imagen_cv, cv2.COLOR_BGR2GRAY)

    # nueva prediccion en base a clasificacion
    prediccion = clasificador.predict([imagen_cv.flatten()])[0]
    
    # Separar género y emoción
    partes = prediccion.split('_')
    genero = partes[0].capitalize()
    emocion = partes[1].capitalize()

    # Mostrar resultados
    etiqueta_genero.config(text=f"Género: {genero}")
    etiqueta_emocion.config(text=f"Emoción: {emocion}")
    etiqueta_resultado.config(text=f"Clasificación: {genero} - {emocion}")

# Boton de cargue y clasificacion
boton = tk.Button(ventana, text="Cargar y clasificar imagen de rostro", 
                  command=cargar_y_predecir, 
                  font=("Arial", 12),
                  bg="#4CAF50",
                  fg="white",
                  padx=20,
                  pady=10)
boton.pack(pady=20)

ventana.mainloop()