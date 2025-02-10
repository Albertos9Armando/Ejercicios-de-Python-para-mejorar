from tkinter import *

def almas(nivel: int) -> int:
    y = (0.02 * nivel ** 3) + (3.06 * nivel ** 2) + (105.6 * nivel) - 895
    return y

ventana1 = Tk()

# Sumar todos los valores de Y para X desde 300 hasta 700*
suma_total = sum(almas(x) for x in range(300,605))
tiempo = (suma_total/3000000)
dias2 = (tiempo/8)
meses3 = (dias2/30)
print("       DARK SOULS NIVLES       ")
print("Total de Almas desde nivel 300 hasta 705 es: ", suma_total,"almas")
print("***",tiempo, "horas ***")
print("**",dias2, "dias **")
print("*",meses3,"mes*")
print(" ",meses3/12,"años")

ventana1.title(string="Calculadora de niveles")
#ventana1.geometry("400x300+50+50")
ventana1.iconbitmap("C:\\Users\\Colibecas\\Downloads\\sol.ico")

t1 = Label(text="Tiempo = " + str(tiempo) + " horas")
t1.grid(column=1, row=3)
#t1.place(x=10, y=30)
t3 = Label(text="dias = " + str(dias2))
t3.grid(column=1, row=2)
#t3.place(x=10, y= 50)
t2 = Label(text="Total de Almas desde nivel 300 hasta 705 es: " + str(suma_total) + " almas")
t2.grid(column=0, row=1)
#t2.place(x=10, y =10)
t4 = Label(text="meses = " + str(meses3))
t4.grid(column=1, row=4)

#t4.place(x=10, y = 70)

ventana1.mainloop()