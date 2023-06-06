"""Da se napravi programa vo koja korisnikot ke go vnese svoeto ime. 
Dokolku imeto e pokratko od 5 karakteri da ispecati “Zdravo {ime}”,
 dokolku e podolgo da ispecati dobredojdovte"""

ime = input('Внесете го вашето име:')
 
if len(ime) < 5:
    print(f'Здраво {ime}')
else:
    print(f'Добредојдовте')
