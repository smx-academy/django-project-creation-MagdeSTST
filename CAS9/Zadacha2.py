""" 2. Da se kreira klasa Pravoagolnik so konstrukot sto ke gi prima 2te strani na pravogolniot.
Da se kreiraat metodi koi ke ja presmetuvaat plostinata i perimetarot na pravogolnik. 
Da se kreira objekt i da se presmeta plostinata i perimetarot na pravogoalnikot"""

class Pravoagolnik:

    def __init__(self,sirina,dolzina):
        self.sirina = sirina
        self.dolzina = dolzina

    def plostinata(self):
        plostinata = self.sirina * self.dolzina
        return plostinata
    
    def perimetar(self):
        perimetar = 2*self.sirina + 2*self.dolzina
        return perimetar
    
Presmetaj = Pravoagolnik(3,4)
P = Presmetaj.plostinata()
L= Presmetaj.perimetar()
print(f'Плоштината на правоаголникот е :{P}')
print(f'Периметарот на правоаголникот е :{L}')