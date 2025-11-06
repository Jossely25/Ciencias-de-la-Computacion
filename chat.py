# Importar las librerías necesarias
import pandas as pd
from sentence_transformers import SentenceTransformer, util

#Codigo adicional para cargar archivos txt si es necesario
def cargar_txt(ruta):
    preguntas = []
    respuestas = []

#Codigo adicinal para abrir archivos txt base de conocimiento
    with open(ruta, 'r', encoding='utf-8') as file:
        contenido = file.read().split('---')

# Codigo adicinal para recorrer los bloques y encuentre la respuesta correspondiente a cada pregunta
        for bloque in contenido:
            if 'PREGUNTA:' in bloque and 'RESPUESTA:' in bloque:

# Codigo adicional para separar los bloque en lineas independientes
                partes = bloque.strip().split('\n')

# Codigo adicional para limpiar y ampliar los prefijos para una mejor intrepretacion de las preguntas y mejor calidad de respuestas
                pregunta = partes[0].replace('PREGUNTA:','').strip()
                respuesta = partes[1].replace('RESPUESTA:','').strip()
                preguntas.append(pregunta)
                respuestas.append(respuesta)

# Codigo adicional para crear un DataFrame con pandas para mantener temporalmente las preguntas y respuestas como unas columnas
    return pd.DataFrame({'Preguntas': preguntas, 'Respuestas': respuestas})

# Fuente de datos pre-entrenados (se cambia la ruta y el tipo de archivo si es necesario)
df = cargar_txt("Base de conocimiento.txt")
#df = pd.read_excel("conocimiento.xlsx")

modelo = SentenceTransformer('LaBSE')

embedding_preguntas = modelo.encode(df['Preguntas'].tolist(), convert_to_tensor=True)

while True:
    pregunta = input("\n Amor: ")
    if pregunta.lower() in ['salir', 'exit', 'quit', 'adiós', 'chao', 'bye']:
        print("¡Hasta luego!")
        break

    embedding_pregunta = modelo.encode(pregunta, convert_to_tensor=True)

    similitudes = util.semantic_search(embedding_pregunta, embedding_preguntas, top_k=1)

    idx = int(similitudes[0][0]['corpus_id'])

    print("\n Cariño: " + df['Respuestas'].iloc[idx])