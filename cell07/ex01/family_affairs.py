#!/usr/bin/python3 

def find_the_redheads(persons) :
    myRed = []
    
    for name, color in persons.items() :
        if color == "red" :
            myRed.append(name)
    
    return myRed

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
    }

print(find_the_redheads(dupont_family))