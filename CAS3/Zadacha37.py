""" 7. Da se napravi programa vo koja korisnikot ke vnese stranite na pravoagolnik,
da se presmeta plostinata i perimetarot na pravoagolnikot.
Da se sporedat koj rezultat e pogolem i da se odredi dali pogolemiot broj e pomal od 10, 
pogolem od 10 a pomal od 50, pomal od 100 ili pogolem od 100"""

a = int(input("Внеси ја ширинат на правоаголникот:"))
b = int(input("Внеси ја должината на правоаголникот:"))
#perimetar 
perimetar = 2*a+2*b 
plostina= a*b 


print(f"Периметарот на правоаголникот е {perimetar}")
print(f"Плоштината на правоаголникот е {plostina}")

if perimetar > plostina and perimetar < 10:
    print(f"Периметарот е поголем од плоштината и периметарот е помал од 10")
elif perimetar > plostina and (perimetar >= 10 and perimetar < 50):
        print(f"Периметарот е поголем од плоштината и периметарот е поголем од 10 и помал од 50")
elif perimetar > plostina and perimetar <100:
        print(f"Периметарот е поголем од плоштинатаи и периметарот е помал од 100")
elif perimetar > plostina and perimetar >100:
        print(f"Периметарот е поголем од плоштината и периметарот е поголем од 100")
elif plostina > perimetar and  plostina < 10:
        (f"Плоштината е поголема од периметарот и плоштината е помалa од 10")
elif plostina > perimetar and (plostina >= 10 and plostina < 50):
        print(f"Плоштината е поголема од периметарот и плоштината е поголемa од 10 и помалa од 50")
elif plostina > perimetar and plostina <100:
        print(f"Плоштината е поголема од периметарот и плоштината е помалa од 100")
elif plostina > perimetar and plostina >100:
        print(f"Плоштината е поголема од периметарот и плоштината е поголема од 100")        