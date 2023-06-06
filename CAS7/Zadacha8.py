"""8. Da se napravi programa vo koja korisnikot ke vnese ime, prezime, 
klas na nekoj ucenik i  ke se zacuvaat vo dictionary.
Vo index otceni sto ke bide lista da se vnesat otcenite na ucenikot.
Da se napravi funkcija koja ke go presmetuva prosekot na ucenik i ke go vraka kako rezultat. 
Prosekot da se zacuva vo index prosek. 
Da se napravi druga funkcija koja ke go odreduva uspehot na ucenikot a kako parametar ke se dava prosekot
0-1.5 - ne dovolen
1.5-2.5 dovolen
2.5-3.5 dobar
3.5-4.5 dobar
4.- 5 odlicen"""

def prosek (lista):
    zbir = 0
    c_lista= len(lista)
    for i in lista:
        zbir = zbir + i
    prosek = zbir / c_lista
    return prosek

def uspeh (prosek):
    if prosek < 1.5:
        uspeh = 'Ne dovolen'
    elif prosek >= 1.5 and prosek<2.5:
        uspeh = 'Dovolen'
    elif prosek >= 2.5 and prosek<3.5:
        uspeh = 'Dobar'
    elif prosek >= 3.5 and prosek<4.5:
        uspeh = 'Mnogu dobar'
    elif prosek >= 4.5 and prosek<=5:
        uspeh = 'Odlichen'
    return uspeh

ucenik = {"Ime" : "Alek",
          "Prezime": "Mitrovski",
          "Oddelenie": "4"
        }

ucenik["Otceni"] = [4,2,3,5,5,3,4,4]

ucenik["Prosek"] = prosek(ucenik["Otceni"])
ucenik["Uspeh"] = uspeh(ucenik["Prosek"])
print(str(ucenik).replace('{', '{\n').replace(' {', '\n{').replace('}', '\n }').replace('''', ''''',',\n '))

