""" Moja:Da se kreira progama vo koja korisnikot ke gi vnese licnite podatoci vo dictionary, adresata vo pod dictionary """
licni_podatoci = {}

licni_podatoci["Ime"] = input('Внесете го вашето име:')
licni_podatoci["Презиме"] = input('Внесете го вашето презиме:')

addressa = {}

addressa["Grad"] = input('Внесете го градот:')
addressa["Zip_Code"] = input('Внесете го поштенскиот број:')
addressa["Ulica"] = input('Внесете ја улицата:')
addressa["Broj"] = input('Внесете го бројот:')

phone = {}

phone["home"] = input('Внесете го бројот на фиксниот телефон:')
phone["mob"] = input('Внесете го бројот на мобилниот телефон:')


licni_podatoci["Адреса"] = addressa
licni_podatoci["Телефонски Броеви"] = phone

print(str(licni_podatoci).replace('{', '{\n').replace(' {', '\n{').replace('}', '\n }').replace(', ',',\n '))
