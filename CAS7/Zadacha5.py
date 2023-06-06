"""5. Da se napravat funkcii koi ke presmetuvaat plostina i perimetar na kvadrat,
 rezultati ke gi vrakaat nazad i da se sporedi dali plositnata ili perimetarot se pogolemi"""
## Задача 5
def plostina_kvadrat(a):
    P = a ** 2
    return P

def perimetar_kvadrat(a):
    L = 4 * a 
    return L

a = int(input('Внеси ја страната на квадратот : '))

Plostina = plostina_kvadrat(a)
Perimetar = perimetar_kvadrat(a)

print(f' Плоштината =  {Plostina} \n Периметарот =  {Perimetar}')

if Plostina > Perimetar:
    print('Плоштината е поголема')
elif Plostina < Perimetar:
    print('Периметарот е поголема')
else:
    print('Периметарот и плоштината се еднакви')