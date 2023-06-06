"""fajl = open("CAS8\lorem.txt",mode="w")
fajl.write("Ova e nov tekst - stariot e izbrishan")
fajl.close()"""

"""fajl = open("CAS8\lorem.txt",mode="a")
fajl.write("\nNov tekst - dodaden vo stariot")
fajl.close()"""

import os

os.remove("CAS8\lorem.txt")
