""" Задача 4: Напиши програма која го прашува корисникот да внесе текст и го креирај функција која испишува текстот во обратен редослед."""

def reorder(recenica):
    lista_zbor = []
    lista_order = []
    lista_zbor = recenica.split(" ")

    x = len(lista_zbor)
    y = -1

## ova del e dodaden samo da ja pecati listat vo obraten redosled bidejki opcijata sort ja pecati po rastecki , a ne po obraten 
    for i in range(x):
        lista_order.append(lista_zbor[y])
        y= y-1
    nova_recenica =  " ".join(lista_order)
    print(f'Реченицата во обратен редослед е : {nova_recenica}')

   

recenica = input('Внесете една реченица: ')
reorder(recenica)
