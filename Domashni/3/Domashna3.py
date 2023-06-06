""" Da se kreira programa vo koja korisnikot ke moze da vnese strani na pravoagolnik, da se vnesat vo dictionary,
 da se presmeta plostina i perimetar koja ke bide zacuvana vo dictinary.
 Da se proveri dali plostinata ili perimetarot se pogolemi."""

pravoagolnik = {}

pravoagolnik["Dolzina"] = int(input('Внесија ја должината на правоаголникот: '))
pravoagolnik["Shirina"] = int(input('Внесија ја ширината на правоаголникот: '))

pravoagolnik["Parametar"] = 2*pravoagolnik["Dolzina"] + 2*pravoagolnik["Shirina"]
pravoagolnik["Plostina"] = pravoagolnik["Dolzina"]*pravoagolnik["Shirina"]

print(pravoagolnik)

if pravoagolnik["Parametar"] > pravoagolnik["Plostina"]:
    pravoagolnik["Pogolem"] = 'Perimetar'
elif pravoagolnik["Parametar"] < pravoagolnik["Plostina"]:
    pravoagolnik["Pogolem"] = 'Plostina'
else:
    pravoagolnik["Pogolem"] = 'Ednakvi' ## ako ednata strana e 6 ,a drugata 3 se ednakvi zatoa e ovaj uslov dodaden

print(pravoagolnik)