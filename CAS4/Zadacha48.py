""" 8. Da se napravi programa vo koja korisnikot ke moze da vnesuva iminja i se 
dodeka bukvata "a" se naogja vo imeto korisnikot da moze da vnesuva novi iminja"""

zbor = 'a'

while True:
    zbor = input('Внесете еден збор кој ја содржи буквата а: ')
 
    if zbor.count('a') == 0:
        break