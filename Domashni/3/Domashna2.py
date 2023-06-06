""" Da se kreiara prazen dictionary, korisnikot da vnese 2 broevi koi ke se dodadt vo dictionary. 
Da se izvrsat 4te osnovni matematicki operacii i da se dodadat rezultatite vo dictionary vo razlicni keys"""

mat_operacii = {}

mat_operacii["Prv Broj"] = int(input('Внесет го првиот број: '))
mat_operacii["Vtor Broj"] = int(input('Внесет го вториот број: '))

mat_operacii["Zbir"] = mat_operacii["Prv Broj"] + mat_operacii["Vtor Broj"]
mat_operacii["Razlika"] = mat_operacii["Prv Broj"] - mat_operacii["Vtor Broj"]
mat_operacii["Proizvod"] = mat_operacii["Prv Broj"] *  mat_operacii["Vtor Broj"]
mat_operacii["Kolicnik"] = mat_operacii["Prv Broj"] / mat_operacii["Vtor Broj"]

print(str(mat_operacii).replace('{', '{\n').replace('}', '\n}').replace(', ',',\n '))