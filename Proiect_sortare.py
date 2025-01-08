from tkinter import *
import time
import random

# Inițializare aplicație
app = Tk()
app.geometry("900x700")  # Dimensiunea ferestrei
canvas = Canvas(app, width=900, height=400, bg="white")  # Crearea canvas-ului pentru desenare
canvas.pack()

# Variabile globale
rand_list = []
anim_speed = 0.5  # Viteza animației implicită
is_paused = False  # Flag pentru pauză
is_stopped = False  # Flag pentru oprire

# Funcție pentru generarea unei liste de numere aleatorii
def lista_random(n):
    global rand_list  # Declarăm lista ca fiind globală pentru a putea fi utilizată în altă parte
    rand_list = [random.randint(1, 99) for _ in range(n)]  # Generăm o listă cu n numere aleatorii

# Funcție pentru desenarea dreptunghiurilor care reprezintă lista
def afisare_sortare(lista, highlight_indices=None):
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

        # Evidențiem barele care sunt comparate sau schimbate
        color = "pink"
        if highlight_indices and i in highlight_indices:
            color = "yellow" if highlight_indices.index(i) == 0 else "red"

        canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, width=2)

    app.update()  # Actualizăm fereastra pentru a afișa modificările

# Funcție pentru sortarea cu Bubble Sort
def bubbleSort():
    global is_paused, is_stopped
    l = rand_list[:]  # Copiem lista aleatorie generată
    n = len(l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if is_stopped:  # Dacă sortarea a fost oprită, ieșim din funcție
                return
            while is_paused:  # Dacă sortarea este pe pauză, așteptăm
                time.sleep(0.1)
            afisare_sortare(l, highlight_indices=[j, j + 1])  # Evidențiem barele comparate
            time.sleep(anim_speed)
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]  # Le schimbăm dacă sunt în ordine greșită
                afisare_sortare(l, highlight_indices=[j, j + 1])  # Evidențiem schimbarea
                time.sleep(anim_speed)

# Funcție pentru sortarea cu Selection Sort
def selectionSort():
    global is_paused, is_stopped
    l = rand_list[:]  # Copiem lista aleatorie generată
    n = len(l)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if is_stopped:  # Dacă sortarea a fost oprită, ieșim din funcție
                return
            while is_paused:  # Dacă sortarea este pe pauză, așteptăm
                time.sleep(0.1)
            afisare_sortare(l, highlight_indices=[min_index, j])  # Evidențiem barele comparate
            time.sleep(anim_speed)
            if l[j] < l[min_index]:
                min_index = j
        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]  # Schimbăm elementele
            afisare_sortare(l, highlight_indices=[i, min_index])  # Evidențiem schimbarea
            time.sleep(anim_speed)

# Funcție pentru sortarea cu Insertion Sort
def insertionSort():
    global is_paused, is_stopped
    l = rand_list[:]  # Copiem lista aleatorie generată
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:  # Mutăm elementele care sunt mai mari decât key
            if is_stopped:  # Dacă sortarea a fost oprită, ieșim din funcție
                return
            while is_paused:  # Dacă sortarea este pe pauză, așteptăm
                time.sleep(0.1)
            l[j + 1] = l[j]  # Mutăm elementul
            afisare_sortare(l, highlight_indices=[j, j + 1])  # Evidențiem schimbarea
            j -= 1
            time.sleep(anim_speed)
        l[j + 1] = key  # Inserăm key la poziția corectă
        afisare_sortare(l, highlight_indices=[j + 1])  # Evidențiem inserarea
        time.sleep(anim_speed)

# Funcție pentru generarea unei noi liste aleatorii
def reset_lista():
    n = num_elements.get()  # Obținem numărul de elemente selectat
    lista_random(n)  # Generăm o nouă listă aleatorie
    afisare_sortare(rand_list)  # Afișăm lista actualizată

# Funcție pentru ajustarea vitezei animației
def ajustare_viteza(val):
    global anim_speed
    anim_speed = float(val)

# Funcție pentru a pune sortarea pe pauză
def pauza_sortare():
    global is_paused
    is_paused = True

# Funcție pentru a opri sortarea
def oprire_sortare():
    global is_stopped
    is_stopped = True

# Funcție pentru a porni sortarea aleasă
def start_sortare():
    global is_paused, is_stopped
    method = sort_method.get()  # Obținem metoda aleasă din meniul drop-down
    is_stopped = False  # Resetăm flag-ul de oprire
    if method == "Bubble Sort":
        bubbleSort()  # Pornește Bubble Sort
    elif method == "Selection Sort":
        selectionSort()  # Pornește Selection Sort
    elif method == "Insertion Sort":
        insertionSort()  # Pornește Insertion Sort

# Crearea meniului pentru alegerea metodei de sortare
sort_method = StringVar()
sort_method.set("Bubble Sort")  # Setăm Bubble Sort ca valoare implicită
sort_menu = OptionMenu(app, sort_method, "Bubble Sort", "Selection Sort", "Insertion Sort")
sort_menu.place(x=50, y=50)  # Poziționarea meniului de alegere a metodei de sortare

# Buton pentru a porni sortarea aleasă
start_button = Button(app, text="Pornește sortarea", command=start_sortare)
start_button.place(x=250, y=50)  # Poziționarea butonului de start

# Buton pentru a genera o nouă listă aleatorie
reset_button = Button(app, text="Generează listă aleatorie", command=reset_lista)
reset_button.place(x=450, y=50)  # Poziționarea butonului în fereastră

# Buton pentru a pune sortarea pe pauză
pauza_button = Button(app, text="Pauză", command=pauza_sortare)
pauza_button.place(x=650, y=50)  # Poziționarea butonului pentru pauză

# Buton pentru a opri sortarea
oprire_button = Button(app, text="Oprire", command=oprire_sortare)
oprire_button.place(x=650, y=100)  # Poziționarea butonului pentru oprire

# Scale pentru a selecta numărul de elemente de sortat (între 5 și 100)
num_elements = Scale(app, from_=5, to=100, orient=HORIZONTAL, label="Număr de elemente", length=200)
num_elements.set(10)  # Setăm valoarea implicită la 10
num_elements.place(x=250, y=450)  # Poziționarea scale-ului în fereastră

# Scale pentru ajustarea vitezei animației
speed_scale = Scale(app, from_=0.1, to=2, resolution=0.1, orient=HORIZONTAL, label="Viteză animație", length=200, command=ajustare_viteza)
speed_scale.set(0.5)  # Setăm viteza implicită
speed_scale.place(x=500, y=450)  # Poziționarea scale-ului în fereastră

# Inițializare listă aleatorie cu numărul de elemente selectat
reset_lista()  # Generăm și afișăm lista inițială

app.mainloop()
