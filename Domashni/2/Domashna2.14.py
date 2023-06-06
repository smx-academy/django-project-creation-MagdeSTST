""" Вежба 14: Напиши програма што ќе бара од корисникот да внесе реченица.
    Раздели ја реченицата на зборови и зачувај ги во листа. Потоа, испечати ги зборовите во обратен редослед."""

lista_zbor = []
lista_order = []
rec = input('Внесете една реченица: ')
lista_zbor = rec.split(" ")
print(lista_zbor)

x = len(lista_zbor)
y = -1

## ova del e dodaden samo da ja pecati listat vo obraten redosled bidejki opcijata sort ja pecati po rastecki , a ne po obraten 
for i in range(x):
    lista_order.append(lista_zbor[y])
    y= y-1


lista_zbor.sort(reverse=True)
print(lista_zbor)
print(lista_order)