# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
from operator import index

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []
print("Bun venit la jocul „Spânzurătoarea”.")
print("Trebuie sa ghicesti cuvantul de mai jos. Have fun!")
print("Progresul initial este:"," ".join(progres))

while incercari_ramase != 0 and "_" in progres:
    litera = input("Introdu o litera: ")
    if len(litera) > 1:
        print("Introdu o singura litera")
        continue

    if litera in litere_incercate:
        print("Aceasta litera a fost deja introdusa")
        continue
    litere_incercate.append(litera)
    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if litera == cuvant_de_ghicit[i]:
                progres[i] = litera

    else:
        incercari_ramase -=1
        print(f"Litera gresita, incercarile tale ramase sunt: {incercari_ramase} ")

    print("Progresul este: ", " ".join(progres))
    print("Literele incercate sunt: ", " ".join(litere_incercate))

if incercari_ramase == 0:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
else:
    print(f"Felicitări! Ai ghicit cuvântul, {''.join(progres)} ")