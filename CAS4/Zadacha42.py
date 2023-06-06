""" Da se napravi programa vo koja korisnikot ke vnese 10 broevi i da se proveri dali sekoj broj e paren ili ne paren"""

for i in range(9):
    x1 = int(input('Внесете број:'))
    if x1%2 == 0:
        print(f'Бројот {x1} е парен број')
    else:
        print(f'Бројот {x1} е непарен број')
