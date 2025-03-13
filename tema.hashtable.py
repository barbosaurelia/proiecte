import csv
import random
from datetime import datetime, timedelta

# ---------------------------
# 1. Date statistice (aproximative)
# Distribuţia populaţiei pe judeţe – codurile sunt cele folosite în CNP (valorile sunt aproximative)
populatie_judete = {
    '01': 300000,  # Alba
    '02': 400000,  # Arad
    '03': 600000,  # Argeș
    '04': 600000,  # Bacău
    '05': 700000,  # Bihor
    '06': 250000,  # Bistrița-Năsăud
    '07': 400000,  # Botoșani
    '08': 550000,  # Brașov
    '09': 300000,  # Brăila
    '10': 400000,  # Buzău
    '11': 300000,  # Caraș-Severin
    '12': 700000,  # Cluj
    '13': 1000000,  # Constanța
    '14': 220000,  # Covasna
    '15': 500000,  # Dâmbovița
    '16': 700000,  # Dolj
    '17': 500000,  # Galați
    '18': 250000,  # Giurgiu
    '19': 400000,  # Gorj
    '20': 250000,  # Harghita
    '21': 500000,  # Hunedoara
    '22': 350000,  # Ialomița
    '23': 800000,  # Iași
    '24': 700000,  # Ilfov (include și București, după cum se foloseşte în CNP)
    '25': 500000,  # Maramureș
    '26': 300000,  # Mehedinți
    '27': 600000,  # Mureș
    '28': 400000,  # Neamț
    '29': 500000,  # Olt
    '30': 800000,  # Prahova
    '31': 250000,  # Satu Mare
    '32': 200000,  # Sălaj
    '33': 400000,  # Sibiu
    '34': 600000,  # Suceava
    '35': 400000,  # Teleorman
    '36': 800000,  # Timiș
    '37': 200000,  # Tulcea
    '38': 400000,  # Vaslui
    '39': 400000,  # Vâlcea
    '40': 900000  # București (se poate folosi un cod separat, după convenție)
}

age_groups = [
    ('0-19', datetime(2006, 1, 1), datetime(2025, 12, 31), 0.24),
    ('20-39', datetime(1986, 1, 1), datetime(2005, 12, 31), 0.28),
    ('40-59', datetime(1966, 1, 1), datetime(1985, 12, 31), 0.26),
    ('60+', datetime(1900, 1, 1), datetime(1965, 12, 31), 0.22)
]

sex_choices = ['M', 'F']
sex_weights = [48, 52]

# Liste de prenume și nume (exemplu simplificat)
prenume_masculine = ['Andrei', 'Mihai', 'Ion', 'George', 'Vasile', 'Marian']
prenume_feminine = ['Maria', 'Elena', 'Ioana', 'Ana', 'Gabriela', 'Andreea']
nume_familie = ['Popescu', 'Ionescu', 'Stan', 'Dumitrescu', 'Georgescu', 'Pop']

# Funcție pentru generarea cifrei de control a CNP-ului
def calculeaza_cifra_control(cnp):
    sc = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma = sum(int(cnp[i]) * sc[i] for i in range(12))
    rest = suma % 11
    return '1' if rest == 10 else str(rest)


# Funcție pentru generarea unui CNP valid
def genereaza_cnp(data_nasterii, cod_judet, sex):
    secol = data_nasterii.year // 100
    if secol == 19:
        s = '1' if sex == 'M' else '2'
    elif secol == 20:
        s = '5' if sex == 'M' else '6'

    aa = f'{data_nasterii.year % 100:02d}'
    ll = f'{data_nasterii.month:02d}'
    zz = f'{data_nasterii.day:02d}'
    nnn = f'{random.randint(0, 999):03d}'

    cnp_partial = s + aa + ll + zz + cod_judet + nnn
    c = calculeaza_cifra_control(cnp_partial)
    return cnp_partial + c


# Funcție pentru generarea unei date de naștere în intervalul specificat
def genereaza_data_nasterii(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


# ---------------------------
# Implementare "hash table" cu hashing personalizat
TABLE_SIZE = 1_000_003  # număr prim pentru reducerea coliziunilor
hash_table = [[] for _ in range(TABLE_SIZE)]


def custom_hash(cnp):
    """
    Calculează hash-ul pentru un CNP pe baza metodei polinomiale,
    folosind multiplicarea cu 31 și operația modulo TABLE_SIZE.
    """
    hash_val = 0
    for ch in cnp:
        if ch.isdigit():
            hash_val = (hash_val * 31 + int(ch)) % TABLE_SIZE
    return hash_val


total_populatie = sum(populatie_judete.values())
total_cnp = 1_000_000

# Vom păstra o listă cu toate CNP-urile generate pentru a le putea selecta ulterior
cnp_list = []

# Salvăm și în fișierul CSV
with open('cnp_nume.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['CNP', 'Nume', 'Prenume'])

    for cod_judet, pop_judet in populatie_judete.items():
        proportie = pop_judet / total_populatie
        numar_cnp_judet = int(proportie * total_cnp)

        for _ in range(numar_cnp_judet):
            sex = random.choices(sex_choices, weights=sex_weights, k=1)[0]
            prenume = random.choice(prenume_masculine) if sex == 'M' else random.choice(prenume_feminine)
            nume = random.choice(nume_familie)

            group = random.choices(age_groups, weights=[grp[3] for grp in age_groups], k=1)[0]
            data_nasterii = genereaza_data_nasterii(group[1], group[2])

            cnp = genereaza_cnp(data_nasterii, cod_judet, sex)

            record = (
                cnp,
                nume,
                prenume
            )

            writer.writerow(record)
            cnp_list.append(cnp)  # salvăm CNP-ul pentru căutări ulterioare

            # Inserăm în hash table în bucket-ul corespunzător
            index = custom_hash(cnp)
            hash_table[index].append(record)
print(
    "Generarea a fost finalizată. Fișierul 'cnp_nume.csv' a fost creat și toate CNP-urile au fost inserate în hash table.")

# ---------------------------
# Partea 2: Selecția aleatorie a 1.000 de CNP-uri și căutarea secvențială în hash table
num_searches = 1000
selected_cnp = random.sample(cnp_list, num_searches)

# Vom număra iterațiile efectuate la căutarea fiecărui CNP
total_iterations = 0
max_iterations = 0
search_iterations = []  # stochează numărul de iterații pentru fiecare căutare

for cnp in selected_cnp:
    iterations = 0
    index = custom_hash(cnp)
    bucket = hash_table[index]


    # Căutare secvențială în bucket-ul corespunzător
    for record in bucket:
        iterations += 1
        if record[0] == cnp:
            break
    total_iterations += iterations
    search_iterations.append(iterations)
    if iterations > max_iterations:
        max_iterations = iterations

average_iterations = total_iterations / num_searches

print("\nRezultate căutare secvențială în hash table:")
print(f"Total căutări efectuate: {num_searches}")
print(f"Număr total iterații: {total_iterations}")
print(f"Număr mediu de iterații per căutare: {average_iterations:.2f}")
print(f"Număr maxim de iterații într-o căutare: {max_iterations}")
