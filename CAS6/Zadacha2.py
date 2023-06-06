""" 2. Da se kreira tuple od 10 broevi sto ke gi vnese korisnikot. 
Parnite broevi da se dodadat vo eden tuple a ne parnite vo drug tuple"""

lista_parni = []
lista_neparni = []

for i in range(1,11):
    x = int(input(f'Внесете го {i} број:'))
    if x%2 == 0:
        lista_parni.append(x)
    else:
        lista_neparni.append(x)

tuple_parni = tuple(lista_parni)
tuple_neparni= tuple(lista_neparni)

print(f'Тупле со парни броеви {tuple_parni}')
print(f'Тупле со непарни броеви {tuple_neparni}')
