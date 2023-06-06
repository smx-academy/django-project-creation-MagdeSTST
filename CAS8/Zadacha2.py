"""  Da se napravi programa vo koja korisnikot ke moze da vnesuva ime prezime, pol i godini na 10 lica i sekoj toj podatok da se zapise vo txt
fajl.
3. Da se napravi programa koja ke go cita fajlot i ke gi pecati site podatoci za licata vo novi redovi
*BONUS: napravete go da bide za kolku lica saka korisnikot tolku"""

broj_lica = int(input("За  колку лица сакате да внесете податоци:"))

try:
    fajl = open("CAS8\Podatoci_za_korisnici.txt", "x")
except FileExistsError:
    fajl = open("CAS8\Podatoci_za_korisnici.txt", "w").close()

fajl = open("CAS8\Podatoci_za_korisnici.txt", "w",encoding='utf-8')
fajl.write("Корсиникот ги внесе следниве податоци:\nИме Презиме Пол Години")
fajl.close()

for i in range(1,broj_lica+1):
    Ime = input(f"Внесте Име на {i} корисник:")
    Prezime = input(f"Внесте Презиме на {i} корисник:")
    Pol = input(f"Внесте пол на {i} корисник:")
    try:
        Godini = int(input(f"Внесте години на {i} корисник:"))
    except ValueError:
        Godini = int(input(f"Внесовте стринг,Внесте години на {i} корисник како бројка:"))

    lichni_podatoci = f'{Ime} {Prezime} {Pol} {Godini}'
    fajl = open("CAS8\Podatoci_za_korisnici.txt", "a",encoding='utf-8')
    fajl.write(f"\n{lichni_podatoci}")
    fajl.close()

