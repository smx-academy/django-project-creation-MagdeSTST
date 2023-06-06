""" Da se napravi programa so klasa Akter .
Klasata akter da gi slednive podatoci:
1.Ime 2.Prezime 3.Godina na ragjanje 4.Broj na filmovi 5.Broj na nagradi 6.Dali ima dobieno oskar
Da ima get i set metodi za site podatoci
So pomos na ciklus da se napravat objekti kolku sto saka korisnikot, i da se najde koj akter dobieno najveke nagradi
"""
class Akter:
    def __init__(self,Ime,Prezime,Godina_Raganje,Br_Filmovi,Br_nagradi,Oskar ):
        self.Ime = Ime
        self.Prezime = Prezime
        self.Godina_Ragjanje = Godina_Raganje
        self.Br_Filmovi = Br_Filmovi
        self.Br_nagradi = Br_nagradi
        self.Oskar = Oskar


    def get_Ime(self):
        return self.Ime
    
    def get_Prezime(self):
        return self.Prezime
    
    def get_Godina_Raganjee(self):
        return self.Godina_Raganje
    
    def get_Br_Filmovi(self):
        return self.Br_Filmovi
    
    def get_Br_nagradi(self):
        return self.Br_nagradi
    
    def get_Oskar(self):
        return self.Oskar
    
    def set_Ime(self, new_ime):
        self.Ime = new_ime

    def set_Prezime(self, new_prezime):
        self.Prezime = new_prezime

    def set_Godina_Raganje(self, new_godina_raganje):
        self.Godina_Raganje = new_godina_raganje

    def set_Br_Filmovi(self, new_br_filmovi):
        self.Br_Filmovi = new_br_filmovi

    def set_Br_nagradi(self, new_br_nagradi):
        self.Br_nagradi = new_br_nagradi

    def set_Oskar(self, new_oskar):
        self.Oskar = new_oskar

    """def presmetaj_najmnogu_oskari(self):
        najmnogu_oskari = self.godini.max
        return najmnogu_oskari"""
