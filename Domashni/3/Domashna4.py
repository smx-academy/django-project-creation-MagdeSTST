""" Da se kreira programa koja ke bide za potrebide vo nekoja prodavnica. 
Da se kreira dictionary koj ke ima 2 indexi, produkti, ceni koi kkao podatoci ke imaat prazni listi. 
Koristnikot da moze da vnesuva produkti i ceni na produktite se dodeka ne izbere deka poveke ne saka da vnese. 
Koga ke prestane da vnesuva produkti da se presmeta kolku treba da plati i da se zacuva vo nov index. 
Da mu se dade opcija na korisnikot da plati, d a se presmeta dali treba da se vrati kusur ili ne. 
Ako treba da se zacuva vo dictionary kolku kusur treba da se vrati. 
Ako ne treba da se zacuva deka smetkata e platena."""
prodavnica={"Product":"",
            "Ceni":""}
Producti=[]
Ceni = []
Zbir = 0
prodavnica["Product"] = Producti
prodavnica["Ceni"] = Ceni

print(prodavnica)

while True:
    a = input('Внесете го продуктот што сакте да го купите:')
    Producti.append(a)
    b = int(input('Внесете ја цената на  продуктот што сакте да го купите:'))
    Ceni.append(b)
    Zbir = Zbir + b
    x= input('Ако сакаш да завршиш со плаќање избери Y, ако не притиснете Enter: ')

    if x == 'Y':
        break

prodavnica["Product"] = Producti
prodavnica["Ceni"] = Ceni
print(prodavnica)

prodavnica["Vkupno za plakanje"] = Zbir

plati = int(input('Внесете го износот што ќе го платите: '))

if plati > prodavnica["Vkupno za plakanje"]:
    prodavnica["Kusur"] = plati - prodavnica["Vkupno za plakanje"]
else:
    prodavnica["Smetkata e platena"] = 'Y'

print(prodavnica)
