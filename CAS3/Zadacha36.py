"""6.Da se napravi programa vo koja korisnikot ke vnese broj i da se proveri dali toj broj e pomal od 10, 
pomal od 100, 
pomal od 1000 ili pogolem od 1000"""

x1 = int(input('Внесете цел број:'))

if x1 < 10:
    print('Бројот е помал од 10')
elif x1<100:
    print('Бројот е поголем од 10 и помал од 100')
elif x1<1000:
    print('Бројот е поголем од 100 и помал од 1000')
else:
    print('Бројот е поголем од 1000') 

