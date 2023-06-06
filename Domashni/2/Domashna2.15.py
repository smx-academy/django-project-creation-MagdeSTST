""" Вежба 15: Напиши програма што ќе бара од корисникот да внесе реченица. 
Раздели ја реченицата на зборови и зачувај ги во листа. Потоа, испечати го бројот на зборови кои започнуваат со самогласка."""

lista_zbor = []
rec = input('Внесете една реченица: ')
lista_zbor = rec.replace(',',' ').split(" ") 
## тестирав со ваква реченица - Da proveram dali Recenicata ke vrati i samoglaski i soglaski,ako ne e Greshna и затоа додадов replace за да ми ги одели и soglaski,ako 
print(lista_zbor)

cnt = 0
cnts = 0
x = len(lista_zbor)
lista_upper = []
lista_samoglaski = []

for i in lista_zbor:
    if i[0].isupper():  ## прво ја решив со проверка дали е голема буква и затоа ќе го оставам овај дел 
        lista_upper.append(i)
        cnt = cnt+1
    if  i[0] in ('a' ,'A' ,'e','E','i','I','o','O','u','U'): ## тука проверувам дали започнува со самогласка 
        lista_samoglaski.append(i)
        cnts = cnts +1


print(f'Вкупниот број на зборови кои започнуваат со голема буква се {cnt},и тие зборови се {lista_upper}')

print(f'Вкупниот број на зборови кои започнуваат со самогласка се {cnts},и тие зборови се {lista_samoglaski}')

