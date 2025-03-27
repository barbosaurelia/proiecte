import hashlib
import string

# Funcția de criptare
def calculeaza_hash(parola):
    return hashlib.sha256(parola.encode()).hexdigest()

# Hash-ul parolei reale (dat în problema)
hash_parola_reală = '0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad'

# Seturi de caractere posibile
litere_mici = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

litere_mari =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

cifre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simboluri = ['!', '@', '#', '$']

# Variabile globale
parola_gasita = False
numar_apeluri = 0
parole_verificate = set()

# Verifică toate permutările unice ale unei combinații valide
def verifica_permutari(parola_lista, index):
    global parola_gasita, numar_apeluri, parole_verificate

    if parola_gasita:
        return

    if index == len(parola_lista):
        parola = ''.join(parola_lista)
        if parola in parole_verificate:
            return
        parole_verificate.add(parola)

        numar_apeluri += 1
        if calculeaza_hash(parola) == hash_parola_reală:
            print(f"Parola găsită: {parola}")
            print(f"Număr apeluri recursive: {numar_apeluri}")
            parola_gasita = True
        return

    for i in range(index, len(parola_lista)):
        parola_lista[index], parola_lista[i] = parola_lista[i], parola_lista[index]
        verifica_permutari(parola_lista, index + 1)
        parola_lista[index], parola_lista[i] = parola_lista[i], parola_lista[index]

# Funcție recursivă de backtracking care construiește candidate valide
def construieste_candidate(parola_curenta, nr_litere_mici, nr_litere_mari, nr_cifre, nr_simboluri):
    global parola_gasita

    if parola_gasita:
        return

    if len(parola_curenta) == 6:
        if nr_litere_mici == 3 and nr_litere_mari == 1 and nr_cifre == 1 and nr_simboluri == 1:
            verifica_permutari(parola_curenta, 0)
        return

    if nr_litere_mici < 3:
        for litera in litere_mici:
            construieste_candidate(parola_curenta + [litera], nr_litere_mici + 1, nr_litere_mari, nr_cifre, nr_simboluri)

    if nr_litere_mari < 1:
        for litera in litere_mari:
            construieste_candidate(parola_curenta + [litera], nr_litere_mici, nr_litere_mari + 1, nr_cifre, nr_simboluri)

    if nr_cifre < 1:
        for cifra in cifre:
            construieste_candidate(parola_curenta + [cifra], nr_litere_mici, nr_litere_mari, nr_cifre + 1, nr_simboluri)

    if nr_simboluri < 1:
        for simbol in simboluri:
            construieste_candidate(parola_curenta + [simbol], nr_litere_mici, nr_litere_mari, nr_cifre, nr_simboluri + 1)

#Pornirea programului
construieste_candidate([], 0, 0, 0, 0)
