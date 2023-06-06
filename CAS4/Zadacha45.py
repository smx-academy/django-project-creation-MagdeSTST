"""5. Da se napravi programa vo koja korisnikot ke moze da vnese licni podatoci(ime, prezime, godini) na proizvolen broj
 na lica i da se proveri dali sekoe od licata se polnoletni ili maloletni"""

x = int(input('Внесете број на лица за колку сакате да внесете податоци:'))

for i in range(x):
    ime = input('Внесето го имате на корисникот:')
    prezime = input('Внесето го презимето на корисникот:')
    br_godini = int(input('Внесето го имате на корисникот:'))

    if br_godini > 17:
        print(f'Лицето {ime} {prezime} е полнолетно')
    else:
        print(f'Лицето {ime} {prezime} е малолетно')