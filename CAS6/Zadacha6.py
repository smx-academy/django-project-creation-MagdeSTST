"""  Da se kreira programa vo koja korisnikot ke vnese stranite na pravogaolnik i ke se zacuvaat vo dictionary. Da se presmeta plostinata i perimetarot, rezultatite isto taka da se zacuvaat vo dictionary vo razlicni indexi. 
 Da se napravi sporedba koj rezultat e pogolem i da se zacuva toa vo index "pogolem"""
 
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
    pravoagolnik["Pogolem"] = 'Ednakvi'

print(pravoagolnik)