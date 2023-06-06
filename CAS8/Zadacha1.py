""" Da se napravi programa vo koja korisnikot ke vnese 2 broevi. Da se izvrsat osnovnite matematicki operacii i da izrazite da se zapisaat vo
txt fajl
broj1+broj2 = zbir"""

broj1 = int(input("Внеси го првиот број: "))
broj2 = int(input("Внеси го вториот број: "))

z = broj1 + broj2
r = broj1 - broj2
p = broj1 * broj2
try:
    d = broj1 / broj2
except ZeroDivisionError:
    d = 0

try:
    fajl = open("CAS8\Operacii.txt", "x")
except FileExistsError:
    fajl = open("CAS8\Operacii.txt", "w").close()

fajl = open("CAS8\Operacii.txt", "w",encoding='utf-8' )
fajl.write(f"Ги внесовте следните два број број1 =  {broj1} и број2 = {broj2}, нивните основни математички операции се: ")
fajl.close()

fajl = open("CAS8\Operacii.txt", "a" ,encoding='utf-8')
fajl.write(f"\nЗбир: {z} ")
fajl.close()

fajl = open("CAS8\Operacii.txt", "a" ,encoding='utf-8')
fajl.write(f"\nРазлика: {r} ")
fajl.close()

fajl = open("CAS8\Operacii.txt", "a" ,encoding='utf-8')
fajl.write(f"\nПроизвод: {p} ")
fajl.close()

fajl = open("CAS8\Operacii.txt", "a" ,encoding='utf-8')
fajl.write(f"\nКоличник: {d} ")
fajl.close()

