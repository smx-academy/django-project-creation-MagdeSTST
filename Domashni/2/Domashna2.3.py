""" Вежба 3: Напиши програма за печатење на квадратите на броевите од 1 до 10."""

x = 1
lista = []
for i in range(1,11):
    x = i ** 2
    lista.append(x)
print(lista)