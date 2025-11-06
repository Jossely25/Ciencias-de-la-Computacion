# Clasificador - arbol de desiciones
# clasificacion de imagenes

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
ruta_imagenes = r"C:\clases\imagenes"
img_size = (100, 100)
ruta_modelo = "modelo_caricaturas.pkl"

# entrenamiento del modelo

if not os.path.exists(ruta_modelo):
    X, Y = [], []

    for etiqueta in os.listdir(ruta_imagenes): # toma la ruta y el nombre de cada carpeta
        carpeta = os.path.join(ruta_imagenes, etiqueta) # construye la ruta parala carpeta union
        if not os.path.isdir(carpeta): # si no encuentra la informacion incial, se salte y prosiga con el resto
            continue

        # Recorrer la carpetaque hace la union, para evaluar los contenidos de las subcarpetas
        for archivo in os.listdir(carpeta):
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                ruta = os.path.join(carpeta, archivo) # recorride de la capreta Join para evaluar los archivos
                imagen = cv2.imread(ruta)
                imagen = cv2.resize(imagen, img_size)
                imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
                X.append(imagen.flatten())
                Y.append(etiqueta)

# ESTE CODIGO DIVIDE LOS DATOS EN ENTRENAMIENTO Y TEST
    X_train, X_test, Y_traint, Y_test = train_test_split(X, Y, test_size=0.2, random_state= 40)
    

# creacion del arbol de deicion y entrenamiento
    clasificador = DecisionTreeClassifier() #crea el modelo Arbol de desiciones paraclasificacion

    clasificador.fit(X_train, Y_traint)
    # REALIZA LA PREDICCION CON LOS DATOS DE X
    Y_pred = clasificador.predict(X_test)

    precision =  accuracy_score(Y_test, Y_pred)

    print(f"La precision de este modelo es de: {precision * 100: .2f}%")

    # Guarda el modelo pre-entrenado    
    joblib.dump(clasificador, ruta_modelo)


else:
    clasificador = joblib.load(ruta_modelo)

# Entorno grafico
ventana = tk.Tk()
ventana.title("Clasificador de caricaturas")
ventana.geometry("400x400")

# esta etiqueta mostrarar la imagen cargada para que sea clasificada
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady= 10)

etiqueta_resultado = tk.Label(ventana, text = "", font=("Arial", 14))
etiqueta_resultado.pack(pady = 10)

#Funcion para cargar y clasificar imagenes
def cargar_y_predecir():
    ruta_archivo = filedialog.askopenfilename(title = "Seleccione una nueva imagen", 
                                                filetypes =[("Imagenes", "*.jpg; *.png; *.jpeg")])


    if not ruta_archivo:
        return


    imagen_pil = Image.open(ruta_archivo)
    imagen_pil.thumbnail((200, 200))
    imagen_tk = ImageTk.PhotoImage(imagen_pil)
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk

    # procesamiento de la nueva imagen

    imagen_cv = cv2.imread(ruta_archivo)
    imagen_cv = cv2.resize(imagen_cv, img_size)
    imagen_cv = cv2.cvtColor(imagen_cv, cv2.COLOR_BGR2GRAY)
   
    # nueva prediccion en base a clasificacion
    prediccion = clasificador.predict([imagen_cv.flatten()])[0]

    etiqueta_resultado.config(text=f"Prediccion: {prediccion}")
                                          



# Boton de cargue y clasificacion
boton = tk.Button(ventana, text="Cargar y clasificar nueva imagen", command=cargar_y_predecir)
boton.pack(pady=10)




ventana.mainloop()






        




