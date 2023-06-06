""" Da se kreiraat 4 funkcii za osnovnite matematicki operacii koi primaat 2 broevi. 
Korisnikot da vnese dva broevi, da ja vnese operacijata sto saka da se izvrsi i da se povika soodvetnata funkcija"""

def zbir (x, y):
    z = x + y
    print(f'Збирот на броевите {x} и {y} е {z}:')

def razlika (x, y):
    z = x - y
    print(f'Разликата на броевите {x} и {y} е {z}:')


def proizvod (x, y):
    z = x * y
    print(f'Производот на броевите {x} и {y} е {z}:')

def kolochnik (x, y):
    z = x / y
    print(f'Количникот на броевите {x} и {y} е {z}:')

x = int(input('Внесете го првиот број: '))
y = int(input('Внесете го вториот број: '))

c = input('Внесете која операција сакате да се изврши соодвтено: \n Z - Збир \n R - Разлика \n P - Множење \n D - Делење \n Избирате:')
##print(c)

if c == 'Z':
    zbir(x,y)
elif c== 'R':
    razlika(x,y)
elif c== 'P':
    proizvod(x,y)
elif c== 'D':
    kolochnik(x,y)
else:
    print('Корсиникот внесе погрешен параметар')
