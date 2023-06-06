""" 
WHILE
  se pravi proverka dali uslovot se ispolnuva
   ako se ispolnuva kodot se izvrshuva """

""" DO WHILE 
   kodot se izvrshuva 
   potoa se pravi proverka

   ova se koristi koga barem ednash sakame da se izvrshi kodot 
"""
i = 11
while i < 18:
    i = int(input('Внесете ги вашите години:'))
    print(i)

print(i)

##do while

zbir = 0
broj = 0

while True:
    godini = int(input('Внесете години:'))
    broj = broj + godini
    print(godini)

    if broj <=18:
        break