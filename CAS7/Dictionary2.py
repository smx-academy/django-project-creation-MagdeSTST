nov_dictionary = {
    "ime":"Nenad",
    "prezime":"ristov",
    "email":["ristovn18@gmail.com", "ristovn17@gmail.com"],
    "tel_broj":{
        "privaten":0000,
        "sluzben":1345,
        "operator":{

        }
    } 
}


# kako da go ispecatime vtoriot email
# kako da go ispecatime sluzbeiot telefonski broj

print(nov_dictionary["email"][1])
print(type(nov_dictionary["email"]))

print(nov_dictionary["tel_broj"]['sluzben'])
print(type(nov_dictionary["tel_broj"]))

