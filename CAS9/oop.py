"""class Dog:

    ime = "Noa"
    rasa = "French Bulldog"
    pol = "masko"
    godini = 2
    boja = "crna

kuche = Dog()
##print(type(kuche))
print(kuche.pol)"""


class Dog:

    def __init__(self,ime,rasa,pol,godini,boja):
        self.ime = ime
        self.rasa = rasa
        self.pol = pol
        self.godini = godini
        self.boja = boja

    def get_name(self):
        return self.ime
    
    def set_name(self, new_name):
        self.ime = new_name

    def presmetaj_godina_na_raganje(self):
        godina_rag = 2023 - self.godini
        return godina_rag
    


       
      
kuche = Dog("Noa","French Bulldog","masko",2,"crna")
##print(type(kuche))
##print(kuche.pol)
print(kuche.get_name())
kuche.set_name("Bosko")
print(kuche.get_name())

godina_raganje = kuche.presmetaj_godina_na_raganje()
print (godina_raganje)

kuche1 = Dog("Beti","Schnauzer","zenski",5,"bela")
##print(type(kuche))
print(kuche1.pol)