import json
import os
# Obtinem calea absoluta catre directorul curent (adica directorul in care se afla acest fisier)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construieste calea catre fisierul JSON aflat in folderul ../data/items.json
file_path = os.path.join(current_dir, '..', 'data', 'items.json')

# Normalizeaza calea (pentru a fi compatibila pe orice sistem de operare)
file_path = os.path.normpath(file_path)

# Functie care returneaza intreaga lista de produse din fisierul JSON
def get_items():
    with open(file_path, 'r') as json_file:
        content = json_file.read().strip()
        if content:
            inventar = json.loads(content)
        else:
            inventar = []

    return inventar
# Functie care returneaza un singur produs dupa denumire
def get_item(denumire):
    with open(file_path, 'r') as json_file:
        content = json_file.read().strip()
        if content:
            inventar = json.loads(content)
        else:
            inventar = []
    # Cautam produsul in lista si il returnam daca il gasim
    for item in inventar:
        if item.get('denumire') == denumire:
            return item
    return None
# Functie care adauga un nou produs in fisier
def save_item(item):
    items = get_items()
    items.append(item)
    with open(file_path, "w") as outfille:
        outfille.write(json.dumps(items, indent=2))
# Functie care editeaza un produs deja existent
def edit_item(denumire, data):
    items = get_items()
    for item in items:
        if item.get('denumire') == denumire:
            item.update(data)
            break
    with open(file_path, "w") as outfille:
        outfille.write(json.dumps(items, indent=2))
# Functie care sterge un produs din lista dupa denumire
def delete_item(denumire):
    items = get_items()
    # Cream o lista noua fara produsul respectiv
    new_items = [item for item in items if item.get('denumire') != denumire]

    with open(file_path, "w") as outfille:
        outfille.write(json.dumps(new_items, indent=2)) # Scriem lista filtrata in fisier


