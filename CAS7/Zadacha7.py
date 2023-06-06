""" . Da se napravi funkcija koja ke prima lista od broevi,
 da gi kvadrira site broevi i da gi vrati samo broevite koi se dellivi so 5 nazad kako rezultat"""
## Задача 7
def dev5(lista):
    lista_kva = []
    lista_div5 = []
    for i in lista:
        lista_kva.append(i**2)
    for n in lista_kva:
        if  n%5 == 0:
            lista_div5.append(n)
    return lista_div5

##lista_int = [2,8,10,14,25,30,36]

lista_re = dev5([2,8,10,14,25,30,36])

print(f'Листа на бреови деливи со 5 е {lista_re}')