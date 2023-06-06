""" 4. Da se napravi programa vo koja korisnikot ke vnese dva broevi, ke se zacuvaat vo dictionary, ke se izvrsat osnovnite matematicki operacii i isto taka ke se zacuvaat vo dictionary. 
Celiot toj dictionary da se zapise vo nov json fajl"""
import json

def osn_operacii(x,y):
    mat_operacii = {}

    mat_operacii["Prv Broj"] = x
    mat_operacii["Vtor Broj"] = y

    mat_operacii["Zbir"] = mat_operacii["Prv Broj"] + mat_operacii["Vtor Broj"]
    mat_operacii["Razlika"] = mat_operacii["Prv Broj"] - mat_operacii["Vtor Broj"]
    mat_operacii["Proizvod"] = mat_operacii["Prv Broj"] *  mat_operacii["Vtor Broj"]
    try:
        mat_operacii["Kolicnik"] = mat_operacii["Prv Broj"] / mat_operacii["Vtor Broj"]
    except ZeroDivisionError:
        mat_operacii["Kolicnik"] = 0
    return mat_operacii

x = int(input('Внесет го првиот број: '))
y = int(input('Внесет го вториот број: '))

presmetaj_osn = osn_operacii(x,y)

try:
    fajl = open("CAS8\mat_operacii.json", 'x')
except:
    fajl = open("CAS8\mat_operacii.json", 'w').close()

fajl = open("CAS8\mat_operacii.json", 'w')
json.dump(presmetaj_osn,fajl)
fajl.close()

fajl = open("CAS8\mat_operacii.json", 'r',encoding='utf-8')
json_str = json.load(fajl)
json_formatted_str = json.dumps(json_str, indent=1)
print(json_formatted_str)

