from tkinter import *
import json
from tkinter.ttk import Treeview
from tkinter import messagebox

# Citeste inventarul din fisier
inventar = []
with open('inventar.json', 'r') as json_file:
    content = json_file.read().strip()
    if content:
        inventar = json.loads(content)
    else:
        inventar = []

# Fereastra principala
fereastra_principala = Tk()
fereastra_principala.geometry("400x400")
fereastra_principala.configure(bg="lightpink")
fereastra_principala.title("Florarie")

def deschidere_adaugare():
    fereastra_secundara = Tk()
    fereastra_secundara.geometry("400x400")
    fereastra_secundara.configure(bg="lightpink")
    fereastra_secundara.title("Adaugare produs")
    # Etichete si campuri de introducere
    Label(fereastra_secundara, text='Denumire floare').grid(row=0, column=0, padx=10, pady=5)
    Label(fereastra_secundara, text='Stoc').grid(row=1, column=0, padx=10, pady=5)
    e1 = Entry(fereastra_secundara)
    e2 = Entry(fereastra_secundara)
    e1.grid(row=0, column=1, padx=10)
    e2.grid(row=1, column=1, padx=10)

    # Functie pentru adaugare
    def adauga():
        nou = {
            "denumire": e1.get().strip(),
            "stoc": e2.get().strip()
        }

        if not nou["denumire"] or not nou["stoc"]:
            messagebox.showerror("Eroare", "Toate câmpurile sunt obligatorii!")
            return

            # Verificare duplicate
        for produs in inventar:
            if produs["denumire"].lower() == nou["denumire"].lower():
                messagebox.showerror("Eroare", f"Produsul '{nou['denumire']}' există deja în inventar!")
                return

        inventar.append(nou)
        salvare_in_fisier()
        actualizeaza_tabel()
        e1.delete(0, END)
        e2.delete(0, END)
        fereastra_secundara.destroy()
        messagebox.showinfo("Succes", "Produsul a fost adaugat")

    # Buton de adaugare
    button = Button(fereastra_secundara, text='Adauga', width=15, command=adauga, bg="hotpink")
    button.grid(row=2, column=1, pady=5)



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


# Functie pentru stergerea liniei după index
def sterge_linie():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Avertisment", "Selectati o linie")
        return

    index = int(selected[0])  # iid este indexul în listă
    del inventar[index]
    salvare_in_fisier()
    actualizeaza_tabel()
    messagebox.showinfo("Succes", "Produsul a fost sters")

def editare_linie():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Avertisment", "Selectati o linie")
        return

     #Preluare linie din tabel in functie de index
    values = tree.item(selected[0])["values"]
    fereastra_secundara = Tk()
    fereastra_secundara.geometry("400x400")
    fereastra_secundara.configure(bg="lightpink")
    fereastra_secundara.title("Editare produs")

    Label(fereastra_secundara, text='Denumire floare').grid(row=0, column=0, padx=10, pady=5)
    Label(fereastra_secundara, text='Stoc').grid(row=1, column=0, padx=10, pady=5)
    e1 = Entry(fereastra_secundara)
    e1.insert(0,values[0])
    e2 = Entry(fereastra_secundara)
    e2.insert(0, values[1])
    e1.grid(row=0, column=1, padx=10)
    e2.grid(row=1, column=1, padx=10)

    def salvare_editare():
        nou_denumire = e1.get().strip()
        nou_stoc = e2.get().strip()
        if not nou_denumire or not nou_stoc:
            messagebox.showerror("Eroare", "Toate câmpurile sunt obligatorii!")
            return
            # Actualizează în lista inventar
        inventar[int(selected[0])] = {
            "denumire": nou_denumire,
            "stoc": nou_stoc
        }

        # Salvează în fișier și actualizează tabelul
        salvare_in_fisier()
        actualizeaza_tabel()
        fereastra_secundara.destroy()

        messagebox.showinfo("Succes", "Produsul a fost modificat")

    # Buton pentru a salva editarea
    editare_linie = Button(fereastra_secundara, text='Salveaza', width=15, command=salvare_editare, bg="PaleVioletRed")
    editare_linie.grid(row=2, column=0, pady=5)


# Buton pentru a sterge
sterge_button = Button(fereastra_principala, text='Sterge linie', width=15, command=sterge_linie, bg="red")
sterge_button.grid(row=0, column=0, pady=5)

# Buton pentru a adaugare ferestra
deschidere_adaugare = Button(fereastra_principala, text='+', width=15, command=deschidere_adaugare, bg="lightblue")
deschidere_adaugare.grid(row=1, column=0, pady=5)

# Buton pentru a edita
editare_linie = Button(fereastra_principala, text='Editare linie', width=15, command=editare_linie, bg="green")
editare_linie.grid(row=2, column=0, pady=5)


# Tabel cu Treeview
columns = ("denumire", "stoc")
tree = Treeview(fereastra_principala, columns=columns, show="headings")
tree.heading("denumire", text="Denumire")
tree.heading("stoc", text="Stoc")
tree.column("denumire", width=200)
tree.column("stoc", width=100)

tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Inițializare tabel
actualizeaza_tabel()

# Redimensionare flexibila
fereastra_principala.grid_rowconfigure(3, weight=1)
fereastra_principala.grid_columnconfigure(1, weight=1)

fereastra_principala.mainloop()
