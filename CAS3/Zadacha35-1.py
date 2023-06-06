""" Da se napravi programa vo koja korisnikot ke vnese zbor i 
dokolku nekoja samoglaska se pojavuva vo zborot da se ispecati kolku pati se pojavuva"""

x1 = input('Внесете еден збор:')

if 'a' in x1:
    samoglaska_a =  x1.count('a')
    print(f'Буквата А се појавува {samoglaska_a}')
else:
    print(f'Буквата А не се појавува ')    
if 'i' in x1:
    samoglaska_i =  x1.count('i')
    print(f'Буквата И се појавува {samoglaska_i}')
else:
    print(f'Буквата И не се појавува ')  
if 'o' in x1:
    samoglaska_o =  x1.count('o')
    print(f'Буквата О се појавува {samoglaska_o}')
else:
    print(f'Буквата О не се појавува ')      
if 'e' in x1:
    samoglaska_e =  x1.count('e')
    print(f'Буквата Е се појавува {samoglaska_e}')
else:
    print(f'Буквата Е не се појавува ')  
if 'y' in x1:
    samoglaska_y =  x1.count('y')
    print(f'Буквата У се појавува {samoglaska_y}') 
else:
    print(f'Буквата У не се појавува ')                 