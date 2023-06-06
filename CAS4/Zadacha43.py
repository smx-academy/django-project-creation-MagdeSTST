""" 3. Da se napravi programa vo koja korisnikot ke vnese 5 iminja i da se proveri dali dolzinata na imeto e parna ili ne. 
    Dali dolzinata na imeto e pomala od 5 ili pogolema"""
for i in range(5):
    ime = input('Внесете име:')
    dolzina_ime = len(ime)
    if dolzina_ime%2 == 0:
        print(f'Должината на името {ime} е {dolzina_ime} и е парен број')
    else:
        print(f'Должината на името {ime} е {dolzina_ime} и е непарен број')
    if dolzina_ime<5:
        print(f'Должината на името {ime} е {dolzina_ime} и е помала од 5')
    else:
        print(f'Должината на името {ime} е {dolzina_ime} и е поголема или еднаква на  5')