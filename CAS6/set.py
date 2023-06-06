lista_ovoshje = ("banani","jabolka","krushi","portokali","mandarini")

nov_set = set()

vtor_set = set(("banani","jabolka","krushi","portokali","mandarini"))
print(vtor_set)


tret_set = {"banani","jabolka","krushi","portokali","mandarini","lubenica"}
print(tret_set)
tret_set.add("limon")
print(tret_set)

tret_set.update(("jagoda","malina"))
print(tret_set)

tret_set.pop()
print(tret_set)##ne znaeme sto ke ni se izbrishi
tret_set.remove("jabolka")
print(tret_set)
tret_set.discard("krusi")## so discard ako elemnetot ne postoi ne vraka greska 
print(tret_set)