""" Da se napravi prazna lista vo koja korisnikot ke vnese 10 elementi. 
Programata da go prasa korisnikot da izbere koj element da se izbrise i toj element da se izbrise.  
Bonus: Da se prasa korisnikot dali i kako saka da se podredi listata (rastecki ili opagjcki redosled"""

lista = []

for i in range(1,10):
    broj = int(input(f'Внесете {i} број: '))
    lista.append(broj)
print(lista)
br_br = int(input('Внесете кој од внесените броеви скаате да се избрише:'))
lista.remove(br_br)
print(lista)
redosled = int(input(f'Внесете 1 ако сакате листат да се подреди  по растечки или 2 по опаѓачки редослед:'))

if redosled == 1:
    lista.sort()
    print(lista)
if redosled == 2:   
    lista.sort(reverse=True)
    print(lista)
else:
    print(lista)    