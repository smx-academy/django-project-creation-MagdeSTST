"""fajl = open("CAS8\lorem.txt",mode="r") ## ako fajlot i programata e vo istiot folder
fajl = open("C:\Users\DELL\Desktop\Python SMX\Learning\CAS8\lorem.txt",mode="r",encoding='utf-8')## Целата патека ако не сме во истиот фолдер
tekst = fajl.read()
tekst1 = fajl.readlines()
print(tekst1[1].upper())
fajl.close()"""
#read -> celiot tekst
#readline -> eden red  so sekoe naredno povtoruvanje sleden red
#readlines -> lista od redovi
#w - write -> brise sto imalo vo fajlot i zapisuva novi podatoci
#a - append -> dodava tekst vo vekepostoecki fajl