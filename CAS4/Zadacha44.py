""". Da se napravi programa vo koja korisnikot ke vnese strani na 6 pravoagolnici.  
Da se presmeta plostina i perimetar i da se proveri sto e pogolemo"""
x = 1
for i in range(6):
    a = int(input("Внеси ја ширинат на правоаголникот:"))
    b = int(input("Внеси ја должината на правоаголникот:"))
    #perimetar 
    L = 2*a+2*b 
    P= a*b 
    x = i+1
    print(f"Периметарот на {x} правоаголникот е {L}")
    print(f"Плоштината на {x} правоаголникот е {P}")

    if L > P:
        print(f"Периметарот на {x} правоаголник е поголем од плоштината")     
    else:
        print(f"Плоштината е {x} правоаголник e поголема од периметарот")
       