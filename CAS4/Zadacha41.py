""" Da se napravi programa vo koja korisnikot ke vnese 5 broevi, broevite megju sebe da se pomnozat"""

proizvod = 1

for i in range(5):
    broj = int(input('Внесете број:'))
    proizvod = proizvod * broj
print(proizvod)