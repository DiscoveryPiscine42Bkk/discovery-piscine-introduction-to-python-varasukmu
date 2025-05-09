#!/usr/bin/python3 

def greetings(name ="noble stranger"):
    try :
        x = int(name)
        print("Error! It wasnot a name.")
    except :
        print(f"Hello. {name}.")
    

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)