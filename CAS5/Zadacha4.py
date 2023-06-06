""" 4. Da se kreira lista vo koja korisnikot ke moze da dodade 5 broevi.
 Da se pomina neiz celata lista i da se ispecatat samo parnite broevi sto se vneseni"""

lista1 = []

for i in range(5):
    broj = int(input('Внесете број: '))
    lista1.append(broj)

for i1 in lista1:
    if i1%2 ==0:
        print(i1)