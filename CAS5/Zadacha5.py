""" 5. Da se napravi prazna lista vo koja korisnikot ke moze da gi vnese otcenite na nekoj ucenik. Da se soberat otcenite, 
       da se presmeta prosek i da se ispecati kakov e uspehot na ucenikot
0-1.5 - ne dovolen ,1.5-2.5 dovolen,2.5-3.5 dobar,3.5-4.5 mnogu dobar,4.5- 5 odlicen"""
lista=[]
zbir = 0
i = 1
while True:
    ocena = int(input(f'Внесете ја {i}  оцена на ученикот: '))
    if ocena >= 1 and ocena<=5:
        lista.append(ocena)
        zbir = zbir + ocena        
        i= i+1

    if ocena <1 or ocena >5:
        break
dolzina_lista = len(lista)
prosek = zbir / dolzina_lista

print(f'Листата со оцени на ученикот е :{lista}')
print(zbir)
print(prosek)
if prosek > 0 and prosek<1.5:
    print('Не Доволен')
if prosek >= 1.5 and prosek<1.5:
    print('Доволен')
if prosek >= 2.5 and prosek<3.5:
    print('Добар')     
if prosek >= 3.5 and prosek<4.5:
    print('Многу Добар')
if prosek >= 4.5 and prosek<5:
    print('Одличен')   
