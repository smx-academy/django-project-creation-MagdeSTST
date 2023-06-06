""" Da se kreira dictionary so 3 elementi po vas izbor i da se ispecati posledniot elemen"""

lichni_podatoci = {
                    "Ime" : "Magdalena",
                    "Prezime" : "Mitrovska",
                    "Email" : "magdestst@gmail.com"
}

print(lichni_podatoci["Email"]) ## ako go znaeme posledniot element 
print (list(lichni_podatoci.values())[-1]) ## dictionary go konvertirame vo lista i go printamme posledniot element

