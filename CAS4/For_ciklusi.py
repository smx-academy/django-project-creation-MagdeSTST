#ciklus za povtoruvawe so broenje (for ciklus)

"""for i in range(5): #range(5) ni pravi lista od 0 do 4
    print(i)"""

"""for i in range(2): #range(5) ni pravi lista od 0 do 4
    ime = input('Внесете го вашето име:')
    print(f'Здраво {ime}')"""

zbir = 0
for i in range(2,6):
    broj = int(input('Внесете број:'))
    zbir = zbir + broj
    
print(f'Вкупниот збир е {zbir}')