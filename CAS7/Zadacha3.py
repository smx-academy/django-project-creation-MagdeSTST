"""  Da se napravat funkcii koi ke primaat 2 parametri i ke presmetuvaat plostina i perimetar na pravoagolnik"""

def pravoagolnik(a,b):
    L = 2*a+2*b
    P = a*b
    print(f'Плоштината на правоаголникот е {P}, а периметарот {L}')

a = int(input('Внесија ја должината на правоаголникот: '))
b = int(input('Внесија ја ширината на правоаголникот: '))
pravoagolnik(a,b)