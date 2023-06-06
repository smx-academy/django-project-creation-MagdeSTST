""" БОНУС: Напиши програма која генерира листа со случајни броеви помеѓу 1 и 100. Испечати го најголемиот број во листата."""

import random

lista_sl = []
for i in range(1,10):
    lista_sl.append(random.randint(1,100))

y = max(lista_sl)
print(f'Во листата со рандом броеви {lista_sl} , најголем е {y}')