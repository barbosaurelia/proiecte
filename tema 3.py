from numpy.ma.core import append

meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

while len(comenzi) > 0:
    comanda = comenzi.pop(0)
    student = studenti.pop(0)
    meniu.remove(comanda)
    tavi.pop()
    istoric_comenzi.append(comanda)
    print(f"{student} a comandat {comanda}")

print(f"S-au comandat {istoric_comenzi.count('guias')} guias, "
      f"{istoric_comenzi.count('ceafa')} ceafa, "
      f"{istoric_comenzi.count('papanasi')} papanasi.")

print(f"Mai sunt {len(tavi)} tavi")

print(f"Mai este ceafa: {'ceafa' in meniu}")
print(f"Mai este guias: {'guias' in meniu}")
print(f"Mai este papanasi: {'papanasi' in meniu}")

pret_total = 0
produse_sub_7_lei = []
for pret in preturi:
    nr_comenzi = istoric_comenzi.count(pret[0])
    pret_total += pret[1] * nr_comenzi
    if pret[1] <= 7:
        produse_sub_7_lei.append(pret)

print(f"Cantina a încasat: {pret_total}")
print (f"Produse care costă cel mult 7 lei: {produse_sub_7_lei}")

