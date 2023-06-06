x_ime = 'MAGDALENA'
x_prezime = 'mitrovska'
x_addresa = 'Koce Metalec - SkoPjE'

#konverzacija vo golemi

x_prezime_golemi = x_prezime.upper()
x_addresa_golemi = x_addresa.upper()

print(f"{x_ime} {x_prezime_golemi} , {x_addresa_golemi}")

#konverzacija vo mali

x_ime_mali = x_ime.lower()
x_addresa_mali = x_addresa.lower()

print(f"{x_ime_mali} {x_prezime} , {x_addresa_mali}")

#konverzacija vo mali i golemi

x_ime_swap = x_ime.swapcase()
x_prezime_swap = x_prezime.swapcase()
x_addresa_swap = x_addresa.swapcase()

print(f"{x_ime_swap} {x_prezime_swap} , {x_addresa_swap}")