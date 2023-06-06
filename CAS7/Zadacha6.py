""" 6. Da se napravi funkcija koga ke prima lista od broevi(vneseni od korisnikot), 
listata da gi najde i da gi vrati kako rezultat samo parnite broevi t.e. lista od parni broevi"""
##Задача 6
def lista_parni(lista):
    lista_parni = []
    for i in lista:
        if i%2 == 0:
            lista_parni.append(i)
    return lista_parni

lista_in = []
x = int(input('Колку броеви сакате да внесете во листата: '))
cnt = 1
for i in range(x):
    y = int(input(f'Внесет го {cnt} број:'))
    cnt = cnt +1
    lista_in.append(y)

nova_lista = lista_parni(lista_in)

print(f'Листат со парни броеви е {nova_lista}')


