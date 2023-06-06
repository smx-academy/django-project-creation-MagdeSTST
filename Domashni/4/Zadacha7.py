""" Задача 7: Напиши програма која прашува од корисникот да внесе реченица и креирај функција која го 
пресметува бројот на појавувања на секоја буква во реченицата.
 Игнорирај големината на буквите."""

def broi_bukvi(rec):
    
    lista_zbor=[]  
    distinct_bukvi = set()
    lista_zbor = rec.split(' ')
    for i in lista_zbor:
        for n in i:
            distinct_bukvi.add(n.lower())  ## Креираме еден сет со сите букви што ги содржи реченицата

    for i in distinct_bukvi:  ## имаме еден фор кој ги зема сите букви од сетот и поминува низ секој збор од листата и проверува колку пати се појавува таа буква 
        cnt = 0
        for n in lista_zbor:
            cnt = cnt + n.lower().count(i)
        print(f'Буквата {i} се појавува {cnt}')

rec = input('Внесете една реченица:')
broi_bukvi(rec)