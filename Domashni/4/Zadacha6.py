""" Задача 6: Напиши програма која прашува корисникот да внесе реченица и креирај функција која 
го пресметува бројот на гласни (a, e, i, o, u) во реченицата."""

def broi_samoglaski(rec):
    cnt = 0
    lista_zbor=[]
    lista_zbor = rec.split(' ')
    for i in lista_zbor:
        for n in i:
            if n.lower() in ('a', 'e', 'i', 'o', 'u'):
                cnt = cnt + 1

    print(f'Бројот на самогласки (a, e, i, o, u) во реченицата е {cnt}')

rec = input('Внесете една реченица:')
broi_samoglaski(rec)