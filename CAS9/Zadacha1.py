"""  Da se kreira klasa Lice, so konstrukto koj ke treba da gi prima slednive parametri, Ime, prezime, godini, email, mesto na ziveenje.
Kreirajte 3 lica( objekti)i ispecatete gi iminjata i godinite na sekoe od licata"""

class lice:
    def __init__(self,ime,prezime,godini,email,addresa) -> None:
        self.ime = ime
        self.prezime = prezime
        self.godini = godini
        self.email = email
        self.addresa = addresa


lice1 = lice ("Magde","Mitrovska",40,"magde@gmail.com","Skopje")
lice2 = lice ("Trajko","Trajkovski",27,"trajko@gmail.com","Bitola")
lice3 = lice ("Ivan","Ivanov",36,"ivani@gmail.com","Veles")

print(f"Името на првото лице е {lice1.ime} и тоа има {lice1.godini} години")
print(f"Името на второто лице е {lice2.ime} и тоа има {lice2.godini} години")
print(f"Името на третото лице е {lice3.ime} и тоа има {lice3.godini} години")

