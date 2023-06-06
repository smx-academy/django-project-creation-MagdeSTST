"""prva_lista = list()
vtora_lista = []


lista_ovoshje = ["banani","jabolka","krushi","portokali"]

print(lista_ovoshje)
print(lista_ovoshje[2])
print(lista_ovoshje[-1])

##lista_ovoshje1 = list(("banani","jabolka","krushi","portokali"))

##print(lista_ovoshje1)"""

lista_broevi =[0,1,2,3,4,5,6,7,8,9]

##print(lista_broevi[0:4]) ## gi pechatime site broevi od prvata pozicija do vtorata brojka
##print(lista_broevi[0:15:3])## ke ni se ispechati kolku sto ima vo listata
##print(lista_broevi[:15:3]) ## pochnuva od pocetok ako nemame navedeno prva pozicija
##print(lista_broevi[0::2])## od pocetok do kraj

lista_ovoshje1 = list(("banani","jabolka","krushi","portokali"))
## use for in list
"""for ovosje in lista_ovoshje1[2]:
    print(ovosje)"""

## dodavanje na element vo listata

"""lista_ovoshje1.append(1)
## so append noviot podatok se dodava sekogash na kraj 

print(lista_ovoshje1)


lista_ovoshje1.insert(1,"nov podatok so inser")
##so inser dodavame dva podatoci kade da se dodade i koj element

print(lista_ovoshje1)

a1 = input('Внесете ново овошје: ')
lista_ovoshje1.insert(2,a1)
##so inser dodavame dva podatoci kade da se dodade i koj element

print(lista_ovoshje1)"""

##brisenje na elemnti od lista
##remove bris[e spored vrednosta na elemnetot 
## pop brishe spored index

"""lista_ovoshje1.remove("banani")
print(lista_ovoshje1)
lista_ovoshje1.pop(2)
print(lista_ovoshje1)"""

print(len(lista_ovoshje1)) ## dolzina na lista
print(lista_ovoshje1.index("krushi")) ## pozicija na elemnt
print(lista_ovoshje1.count("c"))## broi kolku pati s epojaviva elemntot
lista_ovoshje1.sort()
print(lista_ovoshje1)


lista_broevi1 =[0,9,2,5,4,11,6,17,20,3]
lista_broevi1.sort()
print(lista_broevi1)
lista_broevi1.sort(reverse=True)
print(lista_broevi1)


zbor = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"

lista_string = zbor.split(" ")
print(lista_string)

nov_zbor = " ".join(lista_string)
print(nov_zbor)

##https://www.lipsum.com/

