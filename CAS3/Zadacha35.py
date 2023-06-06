""" Da se napravi programa vo koja korisnikot ke vnese zbor i 
dokolku nekoja samoglaska se pojavuva vo zborot da se ispecati kolku pati se pojavuva"""

x1 = input('Внесете збор:')

samoglaska_a =  x1.count('а')
samoglaska_e =  x1.count('е')
samoglaska_i =  x1.count('и')
samoglaska_o =  x1.count('о')
samoglaska_u =  x1.count('у')

if samoglaska_a > 0:
    print(f'Буквата А се појавува {samoglaska_a}')
else:
    print(f'Буквата А не се појавува ')    
if samoglaska_e > 0:
    print(f'Буквата Е се појавува {samoglaska_e}')
else:
    print(f'Буквата Е не се појавува ')  
if samoglaska_i > 0:
    print(f'Буквата И се појавува {samoglaska_i}')
else:
    print(f'Буквата И не се појавува ')      
if samoglaska_o > 0:
    print(f'Буквата О се појавува {samoglaska_o}')
else:
    print(f'Буквата О не се појавува ')  
if samoglaska_u > 0:
    print(f'Буквата У се појавува {samoglaska_u}') 
else:
    print(f'Буквата У не се појавува ')                 