from Akter import Akter

try:   
    x = int(input("Колку актери сакате да внесете: ")) 
    akteri = []
    for i in range(x):
        
        Ime = input('Внеси име на актер: ')
        Prezime  = input('Внеси презиме на актер: ')
        Godina_ragjanje = int(input('Внеси година на раѓање на актерот: '))
        Broj_filmovi  = int(input('Внеси број на филмови во кои играл актерот: '))
        Broj_nagradi = int(input('Внеси број на награди кои ги добил актерот: '))
        Oskar = input('Внеси Y ако актерот добил оскар, во спротивно N:')

        akter = Akter(Ime, Prezime,Godina_ragjanje,Broj_filmovi,Broj_nagradi,Oskar  )
        akteri.append(akter)

    najmnogu_nagradi =0
    acter_so_najmnogu_nagradi = None

    for akter in akteri:
        if akter.get_Br_nagradi() > najmnogu_nagradi:
            najmnogu_nagradi = akter.get_Br_nagradi()
            acter_so_najmnogu_nagradi = akter

    
    if acter_so_najmnogu_nagradi:
        print("\nАктер со најмногу награди е:")
        print("Име:", acter_so_najmnogu_nagradi.get_Ime())
        print("Презиме:", acter_so_najmnogu_nagradi.get_Prezime())
        print("Број на награди:", acter_so_najmnogu_nagradi.get_Br_nagradi())
    else:
        print("No actors found.")



    
        

except ValueError:
    print('Внесовте стринг наместо број.')
