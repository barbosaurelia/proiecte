import json
import random

def incarca_date_din_fisier(nume_fisier):
    try:
        with open(nume_fisier, 'r', encoding='utf-8') as fisier:
            return json.load(fisier)
    except FileNotFoundError:
        print(f"Eroare: fișierul '{nume_fisier}' nu a fost găsit.")
        return None

def calculeaza_rest_optim(suma_de_dat, bancnote_disponibile):

    max_suma = suma_de_dat
    numar_tipuri_bancnote = len(bancnote_disponibile)

    # dp[i] = (nr minim de bancnote pentru suma i, lista de cantitati din fiecare bancnota)
    dp= [(float('inf'), None)] * (max_suma + 1)
    dp[0]= (0, [0] * numar_tipuri_bancnote)

    for suma_curenta in range(1, max_suma + 1):
        for index, bancnota in enumerate(bancnote_disponibile):
            valoare = bancnota["valoare"]
            stoc = bancnota["stoc"]

            for numar_bucati in range(1, stoc + 1):
                suma_anterioara = suma_curenta - valoare * numar_bucati
                if suma_anterioara < 0:
                    break

                numar_total_bancnote, configuratie_anterioara = dp[suma_anterioara]

                if configuratie_anterioara is not None and configuratie_anterioara[index] + numar_bucati <= stoc:
                    configuratie_noua = configuratie_anterioara.copy()
                    configuratie_noua[index] += numar_bucati
                    total_bancnote_nou = numar_total_bancnote + numar_bucati

                    if total_bancnote_nou < dp[suma_curenta][0]:
                        dp[suma_curenta] = (total_bancnote_nou, configuratie_noua)

    return dp[suma_de_dat][1] if dp[suma_de_dat][0] != float('inf') else None

def simuleaza_clienti(date_initiale):

    bancnote = date_initiale["bancnote"]
    produse = date_initiale["produse"]
    numar_client = 1

    while True:
        # Alegem un produs aleator
        produs = random.choice(produse)
        nume_produs = produs["nume"]
        pret_produs = produs["pret"]

        # Alegem o suma de plata (pret + 1) și (pret + 20)
        suma_platita = pret_produs + random.randint(1, 20)
        suma_de_rest = suma_platita - pret_produs

        print(f"Clientul {numar_client}")
        print(f"Produs cumpărat: {nume_produs}")
        print(f"Preț produs: {pret_produs} RON")
        print(f"Suma plătită: {suma_platita} RON")
        print(f"Rest de oferit: {suma_de_rest} RON")

        rest_obtinut = calculeaza_rest_optim(suma_de_rest, bancnote)

        if rest_obtinut is None:
            print("\n Nu se poate oferi restul cu bancnotele disponibile.")
            break

        print("Rest oferit cu următoarele bancnote:")
        for index, numar_bancnote in enumerate(rest_obtinut):
            if numar_bancnote > 0:
                valoare = bancnote[index]["valoare"]
                print(f"  - {numar_bancnote} x {valoare} RON")
                bancnote[index]["stoc"] -= numar_bancnote

        numar_client += 1


#Punct de pornire
if __name__ == "__main__":
    date = incarca_date_din_fisier("date.json")
    simuleaza_clienti(date)
