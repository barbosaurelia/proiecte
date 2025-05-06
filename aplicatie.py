from tkinter import *
import json
from tkinter.ttk import Treeview

# Citeste inventarul din fisier
inventar = []
with open('inventar.json', 'r') as json_file:
    content = json_file.read().strip()
    if content:
        inventar = json.loads(content)
    else:
        inventar = []

# Fereastra principala
master = Tk()
master.geometry("400x400")
master.configure(bg="lightpink")
master.title("Florarie")

# Etichete si campuri de introducere
Label(master, text='Denumire floare').grid(row=0, column=0, padx=10, pady=5)
Label(master, text='Stoc').grid(row=1, column=0, padx=10, pady=5)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1, padx=10)
e2.grid(row=1, column=1, padx=10)

# Functie pentru salvare în fisier
def salvare_in_fisier():
    with open("inventar.json", "w") as outfille:
        outfille.write(json.dumps(inventar, indent=2))

# Functie pentru actualizarea intregului tabel
def actualizeaza_tabel():
    for row in tree.get_children():
        tree.delete(row)
    for index, item in enumerate(inventar):
        tree.insert("", END, iid=index, values=(item["denumire"], item["stoc"]))

# Functie pentru adaugare
def adauga():
    nou = {
        "denumire": e1.get().strip(),
        "stoc": e2.get().strip()
    }
    if nou["denumire"] and nou["stoc"]:
        inventar.append(nou)
        salvare_in_fisier()
        actualizeaza_tabel()
        e1.delete(0, END)
        e2.delete(0, END)

# Functie pentru stergerea liniei după index
def sterge_linie():
    selected = tree.selection()
    if selected:
        index = int(selected[0])  # iid este indexul în listă
        del inventar[index]
        salvare_in_fisier()
        actualizeaza_tabel()

# Buton de adaugare
button = Button(master, text='Adauga', width=15, command=adauga, bg="hotpink")
button.grid(row=2, column=1, pady=5)

# Buton pentru a sterge
sterge_button = Button(master, text='Sterge linie', width=15, command=sterge_linie, bg="red")
sterge_button.grid(row=2, column=0, pady=5)

# Tabel cu Treeview
columns = ("denumire", "stoc")
tree = Treeview(master, columns=columns, show="headings")
tree.heading("denumire", text="Denumire")
tree.heading("stoc", text="Stoc")
tree.column("denumire", width=200)
tree.column("stoc", width=100)

tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Inițializare tabel
actualizeaza_tabel()

# Redimensionare flexibila
master.grid_rowconfigure(3, weight=1)
master.grid_columnconfigure(1, weight=1)

master.mainloop()
