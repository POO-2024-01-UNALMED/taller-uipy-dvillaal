from tkinter import Tk, Button, Entry
x = 1

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("500x250")

#Eventos
def intertar_numero(numero):
    current = pantalla.get()
    pantalla.delete(0, "end")
    pantalla.insert("end", str(current) + str(numero))

def suma():
    primer_numero = pantalla.get()
    global primer_num
    global math
    math = "+"
    primer_num = int(primer_numero)
    pantalla.delete(0, "end")

def resta():
    primer_numero = pantalla.get()
    global primer_num
    global math
    math = "-"
    primer_num = int(primer_numero)
    pantalla.delete(0, "end")

def multiplicacion():
    primer_numero = pantalla.get()
    global primer_num
    global math
    math = "x"
    primer_num = int(primer_numero)
    pantalla.delete(0, "end")

def division():
    primer_numero = pantalla.get()
    global primer_num
    global math
    math = "/"
    primer_num = int(primer_numero)
    pantalla.delete(0, "end")

def igual():
    segundo_numero = pantalla.get()
    pantalla.delete(0, "end")

    if math == "+":
        pantalla.insert(0, str(primer_num + int(segundo_numero)))
    elif math == "-":
        pantalla.insert(0, str(primer_num - int(segundo_numero)))
    elif math == "x":
        pantalla.insert(0, str(primer_num * int(segundo_numero)))
    elif math == "/":
        pantalla.insert(0, str(primer_num / int(segundo_numero)))

# Configuración pantalla de salida
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(1))
boton_1.grid(row=1, column=0, padx=x, pady=x)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(2))
boton_2.grid(row=1, column=1, padx=x, pady=x)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(3))
boton_3.grid(row=1, column=2, padx=x, pady=x)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(4))
boton_4.grid(row=2, column=0, padx=x, pady=x)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(5))
boton_5.grid(row=2, column=1, padx=x, pady=x)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(6))
boton_6.grid(row=2, column=2, padx=x, pady=x)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(7))
boton_7.grid(row=3, column=0, padx=x, pady=x)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(8))
boton_8.grid(row=3, column=1, padx=x, pady=x)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: intertar_numero(9))
boton_9.grid(row=3, column=2, padx=x, pady=x)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command = igual)
boton_igual.grid(row=4, column=0, columnspan=2, padx=x, pady=x)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=x, pady=x)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=suma)
boton_mas.grid(row=1, column=3, padx=x, pady=x)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=resta)
boton_menos.grid(row=2, column=3, padx=x, pady=x)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=multiplicacion)
boton_multiplicacion.grid(row=3, column=3, padx=x, pady=x)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=division)
boton_division.grid(row=4, column=3, padx=x, pady=x)





root.mainloop()