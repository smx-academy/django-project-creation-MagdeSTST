licnost = { "Ime": "Magdalena",
      "Prezime": "Mitrovska",
      "email": "magdestst@gmail.com",
      "phone_number": "077772200"
     }

##print(licnost["Ime"])

## ciklusi za minuvanje niz indeks
for i in licnost:
    print(i) ## gi printame samo indeksite
    print(licnost[i])## vrednostite na indeksot 

for index in licnost.keys():
    print(licnost[index])

for value in licnost.values():
    print(value)

for i in licnost.items():
    print(i)

for i ,j in licnost.items():
    print(f'index: {i}, vrednost:{j}')

## dodavnje na elemnti 

licnost1 = { "FirstName" : "Magdalena",
            "LastName": "Mitrovska"}

licnost1["gender"] = "Female"

print(licnost1)
licnost1.update({"eye color": "brown"})
print(licnost1)

## brishenje

licnost1.pop("eye color")
print(licnost1)

licnost1.popitem() ## posledniot dodaden element (na postara verzija na python brishe random)
print(licnost1)

del licnost1["gender"] ## ne postoi
licnost1.clear () ##gi brishe podatocite , no toj fizicki ostanuva 
del licnost1 ## go brishe fizicki