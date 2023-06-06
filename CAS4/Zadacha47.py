""" 7. Da se napravi programa vo koja korisnikot ke moze da vnesuva kolku saka broevi i 
se dodeka brojot koj e vnesen e pomegju 100 i 500 da moze da se vnusa nov i da se sobiraat broevite"""

zbir = 0
broj = 0

while True:
    broj = int(input('Внесете број: '))
    zbir = zbir + broj
    print(f'Збирот на внесените броеви е {zbir}')

    if broj<100 or broj>500:
        break