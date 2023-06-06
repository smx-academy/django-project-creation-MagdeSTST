x_string = 'Kolku karakteri ima ovaj string'

# dolzina na string
x_dolzina = len(x_string)
print(f"Ovaj string ima {x_dolzina} karakter")

# samoglaski

x_samoglaski_a = x_string.count('a')
x_samoglaski_e = x_string.count('e')
x_samoglaski_o = x_string.count('o')
x_samoglaski_y = x_string.count('y')
x_samoglaski_i = x_string.count('i')

print(f"Vo ovaj string soodvetno samoglaskite se pojavuvaat  \n a - {x_samoglaski_a} , \n e - {x_samoglaski_e},\n i - {x_samoglaski_i}, \n o - {x_samoglaski_o} \n y  - {x_samoglaski_y} pati ")


# mestoto na  na bukvite "t" i "g"(ako gi ima)
x_pozicija_t = x_string.index('t')
x_pozicija_g = x_string.index('g')

print(f"Vo ovaj string bukvata t se naoga na pozicija {x_pozicija_t}, a bukvata g na pozicija {x_pozicija_g }")