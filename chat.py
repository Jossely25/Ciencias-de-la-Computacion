import pandas as pd
from sentence_transformers import SentenceTransformer, util

df = pd.read_excel("conocimiento.xlsx")

modelo = SentenceTransformer('distilus-base-multilingual-cased-v2')

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

