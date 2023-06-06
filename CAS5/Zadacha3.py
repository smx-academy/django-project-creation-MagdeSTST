""" 3. Da se kreira lista so 5 broevi, da se dodadat 3 novi broevi sto ke bidat vneseni od korisnikot. 
Da se ispecatat poslednite elementite od index 3 do kraj"""

lista_broevi = [2, 4, 6, 8, 10]

for i in range(3):
    broj = int(input('Внесете број: '))
    lista_broevi.append(broj)

print(lista_broevi[3:])