from Banka.lice import Lice

class TransakciskaSmetka(Lice):
    def __init__(self, ime, prezime, embg, addresa,br_na_smetka, suma, datum_na_kreiranje):
        super().__init__(ime, prezime, embg, addresa)
        self.br_na_smetka = br_na_smetka
        self.suma = suma
        self.datum_na_kreiranje = datum_na_kreiranje

    def Povlechni_suma(self,suma_za_povlekuvanje):
        if self.suma - suma_za_povlekuvanje < 0:
            print(f'Немате доволно средства на сметката, на вашата сметка има {self.suma} ')
        else:
            self.suma = self.suma - suma_za_povlekuvanje
            print(f'Успешно повлечена сума, на вашата сметка се преостанати {self.suma}')
           
    def Vnesi_suma(self,vnesena_suma):
        self.suma = self.suma + vnesena_suma
        print(f"Успешно внесена сума, на вашата сметка сега има {self.suma}")
        