from tkinter import *
import time
import random

# Inițializare aplicație
app = Tk()
app.geometry("900x700")  # Dimensiunea ferestrei
canvas = Canvas(app, width=900, height=400, bg="white")  # Crearea canvas-ului pentru desenare
canvas.pack()

# Variabila globală pentru lista aleatorie
rand_list = []

# Funcție pentru generarea unei liste de numere aleatorii
def lista_random(n):
    global rand_list  # Declarăm lista ca fiind globală pentru a putea fi utilizată în altă parte
    rand_list = [random.randint(1, 99) for _ in range(n)]  # Generăm o listă cu n numere aleatorii

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

# Funcție pentru sortarea cu Bubble Sort
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

# Funcție pentru sortarea cu Selection Sort
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

# Funcție pentru generarea unei noi liste aleatorii
def reset_lista():
    n = num_elements.get()  # Obținem numărul de elemente selectat
    lista_random(n)  # Generăm o nouă listă aleatorie
    afisare_sortare(rand_list)  # Afișăm lista actualizată

# Buton pentru a porni sortarea cu vizualizare Bubble Sort
B = Button(app, text="Arată vizualizarea Bubble Sort", command=bubbleSort)
B.place(x=50, y=50)  # Poziționarea butonului în fereastră

# Buton pentru a porni sortarea cu vizualizare Selection Sort
C = Button(app, text="Arată vizualizarea Selection Sort", command=selectionSort)
C.place(x=250, y=50)  # Poziționarea butonului în fereastră

# Buton pentru a genera o nouă listă aleatorie
reset_button = Button(app, text="Generează listă aleatorie", command=reset_lista)
reset_button.place(x=450, y=50)  # Poziționarea butonului în fereastră

# Scale pentru a selecta numărul de elemente de sortat (între 5 și 100)
num_elements = Scale(app, from_=5, to=100, orient=HORIZONTAL, label="Număr de elemente", length=200)
num_elements.set(10)  # Setăm valoarea implicită la 10
num_elements.place(x=250, y=450)  # Poziționarea scale-ului în fereastră

# Inițializare listă aleatorie cu numărul de elemente selectat
reset_lista()  # Generăm și afișăm lista inițială

app.mainloop()

