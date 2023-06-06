x_string='Hello World'


print(x_string)

#konverzacija vo golemi
x_upper = x_string.upper()
print(x_upper)

#konverzacija vo mali
x_lower = x_string.lower()
print(x_lower)

#od golemi vo mali i obratno 
x_swap = x_string.swapcase()
print(x_swap)

#samo prva golema 
x_capitalize = x_string.capitalize()
print(x_capitalize)

#dolzina na string 
x_dolzina = len(x_string)
print(f"Dolzinata na stringot e: {x_dolzina}")

# kolku pati se pojavuva eden karakter vo eden funkcia

x_count = x_string.count('l')
print(f"Bukvata l se pojavuva {x_count}")

# na koja se pozicija se naoga odreden karakter 

x_pozicija = x_string.index('l')
print(f"Bukvata l se naoga na pozicija {x_pozicija}")