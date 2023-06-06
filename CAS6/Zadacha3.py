""" . Da se kreira lista vo koja korisnikot ke moze da vnese 5 stringovi, porgramata da go prasa dali saka da se izbrisaat duplikati vrednosti, dokolku korisnikot saka - da se izbrisaat,
 dokolku ne da se ispecati samo listata"""
lista_grad = []
for i in range(1,6):
    grad = input(f'Внесете називи на 5 града, {i} :')
    lista_grad.append(grad)

x = input('Дали сакате ако има дупли градови да се избришат Y/N :')

if x == 'Y':
    set_grad = set(lista_grad)
    print(set_grad)
else:
    print(lista_grad)