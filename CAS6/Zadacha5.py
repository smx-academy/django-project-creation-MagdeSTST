"""5. Da se kreira dictionary koj vo eden index ke ima eden broj, vo drug index ke ima vtor broj. Vo nov index da se zacuva zbirot na broevite, 
i vo drug index razlikata na broevite"""

x = {"PrvBroj": 8,
     "VtorBroj": 6}

x["Zbir"] = x["PrvBroj"]+x["VtorBroj"]
x["Razlika"]= x["PrvBroj"]-x["VtorBroj"]

print(x)