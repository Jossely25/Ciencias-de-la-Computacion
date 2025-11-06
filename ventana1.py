import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("800x600")
ventana.configure(bg="lightblue")

# Etiquetas
#etiqueta1 = tk.Label(ventana, text="Mi primera Etiqueta", bg="red", font=("Arial", 16))#
#etiqueta1.grid(row=1, column=1, padx=10, pady=10)

#etiqueta2 = tk.Label(ventana, text="Mi segunda Etiqueta", bg="green", font=("Arial", 16))
#etiqueta2.grid(row=2, column=1, padx=10, pady=10)

#boton1 = tk.Button(ventana, text="Cerrar ventana", bg="yellow", font=("Arial", 16), command=ventana.destroy)
#boton1.grid(row=3, column=1, padx=10, pady=10)

def sumar():
    num1 = float(caja_texto1.get())
    num2 = float(caja_texto2.get())
    num3 = float(caja_texto3.get())
    resultado = num1 + num2 + num3
    etiqueta_resultado.config(text=f"Resultado: {resultado}")  

def restar():
    num1 = float(caja_texto1.get())
    num2 = float(caja_texto2.get())
    num3 = float(caja_texto3.get())
    resultado = num1 - num2 - num3
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

def multiplicar():
    num1 = float(caja_texto1.get())
    num2 = float(caja_texto2.get())
    num3 = float(caja_texto3.get())
    resultado = num1 * num2 * num3
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

def dividir():
    num1 = float(caja_texto1.get())
    num2 = float(caja_texto2.get())
    num3 = float(caja_texto3.get())
    if num2 != 0 and num3 != 0:
        resultado = num1 / num2 / num3
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    else:
        etiqueta_resultado.config(text="Error: División por cero")

###############ETIQUETA#################
etiqueta = tk.Label(ventana, text="Digite numero uno")
etiqueta.grid(row=10, column=5, padx=20, pady=10)

etiqueta2 = tk.Label(ventana, text="Digite numero dos")
etiqueta2.grid(row=11, column=5, padx=20, pady=10)

etiqueta3 = tk.Label(ventana, text="Digite numero tres")
etiqueta3.grid(row=12, column=5, padx=20, pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=30, column=10, padx=20, pady=10)

################CAJA DE TEXTO#################
caja_texto1 = tk.Entry(ventana, font=("Arial", 12))
caja_texto1.grid(row=10, column=6, padx=20, pady=10)

caja_texto2 = tk.Entry(ventana, font=("Arial", 12))
caja_texto2.grid(row=11, column=6, padx=20, pady=10)

caja_texto3 = tk.Entry(ventana, font=("Arial", 12))
caja_texto3.grid(row=12, column=6, padx=20, pady=10)

################BOTON#################
boton1 = tk.Button(ventana, text="Sumar", font=("Arial", 12), command=sumar)
boton1.grid(row=20, column=6, padx=20, pady=10)

boton2 = tk.Button(ventana, text="Restar", font=("Arial", 12), command=restar)
boton2.grid(row=20, column=8, padx=20, pady=10)

boton3 = tk.Button(ventana, text="Multiplicar", font=("Arial", 12), command=multiplicar)
boton3.grid(row=20, column=10, padx=20, pady=10)

boton4 = tk.Button(ventana, text="Dividir", font=("Arial", 12), command=dividir)
boton4.grid(row=20, column=12, padx=20, pady=10)

ventana.mainloop()
