import json

fajl = open("CAS8\employees.json", mode = "r")

x = json.load(fajl)
print(x)

##nov_dict = {"id": 4, "name": "Alsa Jons", "position": "Developer", "salary": 43000}
##x['employees'].append(nov_dict)
##fajl = open("CAS8\employees.json", mode = "w")
##json.dump(x,fajl)

