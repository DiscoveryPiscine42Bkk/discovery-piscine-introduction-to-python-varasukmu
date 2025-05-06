#!/usr/bin/python3 

def famous_births(bd) :
    newD = dict()
    for n in bd.values() :
        newD[n["name"]] = n["date_of_birth"]
    
    newD = sorted(newD.items(), key=lambda x:x[1])
    
    for x in newD :
        print(f"{x[0]} is a great scientist born in {x[1]}.")


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)