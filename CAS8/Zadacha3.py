#3 Zadaca: Da se napravi programa koja ke go cita fajlot i ke gi pecati site podatoci za licata vo novi redovi

try:
    fajl = open("CAS8\Podatoci_za_korisnici.txt", "r",encoding='utf-8')
except FileNotFoundError:
    print("Фајлот не постои")

for i in fajl.readlines():
    print(i)
