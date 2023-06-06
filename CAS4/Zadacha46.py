""" 6. Da se napravi programa vo koja korisnikot ke moze da vnesuva kolku saka parni broevi i tie da se mnozat megju sebe. 
    Otkako ke zavrsi cuklusot da se proveri dali zbirot e delliv so 5 ili ne"""

proizvod = 1
zbir = 0
broj = 0

while broj%2 == 0:
    broj = int(input('Внеси парен број: '))
    if broj%2 == 0:
        proizvod = proizvod * broj
        zbir = zbir + broj
        print(f'Вкупниот производ е {proizvod}')
    
print(f'Вкупниот производ е {proizvod}')
if zbir%5 == 0:
    print(f'Збирот {zbir} е делив со 5')
else:
    print(f'Збирот {zbir} не е делив со 5')