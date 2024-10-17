text_articol = (" „Il Luce” a avut cuvinte de laudă la adresa lui Radu Drăgușin (22 de ani)"
                " și a lui Denis Drăguș (25 de ani)."
                " Apărătorul a realizat o fază superbă la golul victoriei marcat de Drăguș,"
                " iar selecționerul României a comentat evoluția acestora.")


lungime_sir = len(text_articol)

l_prima_parte = lungime_sir // 2 if lungime_sir % 2 == 0  else lungime_sir // 2 + 1
l_a_doua_parte = lungime_sir // 2

prima_parte = text_articol[:l_prima_parte]
a_doua_parte = text_articol[l_a_doua_parte:]

prima_parte = prima_parte.upper()

prima_parte = prima_parte.strip()

a_doua_parte = a_doua_parte[::-1]

a_doua_parte = a_doua_parte.capitalize()

a_doua_parte = (a_doua_parte
                .replace(",", "")
                .replace(".", "")
                .replace("!", "")
                .replace("?", ""))

print(prima_parte + a_doua_parte)