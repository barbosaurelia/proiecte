from tkinter import *
import time
import random

# Inițializare aplicație
app = Tk()
app.geometry("900x700")  # Dimensiunea ferestrei
canvas = Canvas(app, width=900, height=400, bg="white")  # Crearea canvas-ului pentru desenare
canvas.pack()

# Generare listă aleatorie
rand_list = []
n = 10  # Numărul de elemente din listă

# Funcție pentru generarea unei liste de numere aleatorii
def lista_random():
    for i in range(n):
        rand_list.append(random.randint(1, 99))  # Adăugăm numere între 1 și 99

lista_random()

# Funcție pentru desenarea dreptunghiurilor care reprezintă lista
def afisare_sortare(lista):
    canvas.delete("all")  # Ștergem conținutul anterior de pe canvas
    width = 20  # Lățimea fiecărui dreptunghi
    spacing = 5  # Spațiul dintre dreptunghiuri
    x_start = 10  # Coordonata x inițială
    for i, height in enumerate(lista):  # Iterăm prin lista de valori
        # Calculăm coordonatele dreptunghiului
        x1 = x_start + i * (width + spacing)
        y1 = 400 - height * 3
        x2 = x1 + width
        y2 = 400
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="pink", width=2)
    app.update()  # Actualizăm fereastra pentru a afișa modificările

def bubbleSort():
    l = rand_list  # Luăm lista aleatorie generată
    sorted = False  # Indicator pentru a verifica dacă lista este sortată
    while not sorted:  # Continuăm până când lista este sortată complet
        sorted = True  # Presupunem că este sortată
        for i in range(len(l) - 1):  # Iterăm prin listă
            if l[i + 1] < l[i]:  # Comparăm două elemente consecutive
                l[i], l[i + 1] = l[i + 1], l[i]  # Le schimbăm dacă sunt în ordine greșită
                afisare_sortare(l)  # Afișăm lista actualizată
                time.sleep(0.5)  # Pauză pentru a vizualiza schimbarea
                sorted = False  # Marcăm că lista nu este încă sortată

# Buton pentru a porni sortarea cu vizualizare
B = Button(app, text="Arată vizualizarea Bubble Sort", command=bubbleSort)
B.place(x=50, y=50)  # Poziționarea butonului în fereastră

def selectionSort():
    l = rand_list  # Luăm lista aleatorie generată
    size = len(l)  # Determinăm dimensiunea listei
    for i in range(size - 1):  # Iterăm prin listă
        # Presupunem că elementul curent este cel mai mic
        min_index = i
        for j in range(i + 1, size):  # Căutăm cel mai mic element din restul listei
            if l[j] < l[min_index]:
                min_index = j  # Actualizăm indexul celui mai mic element găsit
        if min_index != i:  # Dacă am găsit un element mai mic decât cel curent
            l[i], l[min_index] = l[min_index], l[i]  # Le schimbăm între ele
            afisare_sortare(l)  # Afișăm lista actualizată
            time.sleep(0.5)  # Pauză pentru a vizualiza schimbarea

C = Button(app, text="Arată vizualizarea Selection Sort", command=selectionSort)
C.place(x=100, y=100)  # Poziționarea butonului în fereastră

app.mainloop()
