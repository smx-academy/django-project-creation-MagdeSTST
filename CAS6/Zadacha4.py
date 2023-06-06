""" Da se kreira set so unikatni broevi vneseni od korisnikot.
 Da se ispecati setot i da se prasa korisnikot koj element saka da bide izbrisan i toj element da se izbrise od setot"""

set_br = set()
cnt = 1
x = int(input('Колку броеви сакате да внесете: '))

for i in range(x):
    br = int(input(f'Внесете гo {cnt} број :'))
    set_br.add(br)
    cnt = cnt + 1

print(set_br)

y = int(input(f'Кој елементите сакате да го избришете: '))

set_br.discard(y)
print(set_br)
