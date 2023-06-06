lista_ovoshje = list(("banani","jabolka","krushi","portokali"))
## razlikata so lista e se zagradite 
nov_tuple = tuple()
nov_tuple_so_podatoci = ("banani","jabolka","krushi","portokali")

print(nov_tuple_so_podatoci)

lista_ovoshje = list(nov_tuple_so_podatoci)
lista_ovoshje.append("lubenica")
nov_tuple_so_podatoci= tuple(lista_ovoshje)

print(nov_tuple_so_podatoci)
