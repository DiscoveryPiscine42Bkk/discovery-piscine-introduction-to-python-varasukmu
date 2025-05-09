#!/usr/bin/python3 

def passW(x) :
    password = "Python is awesome"
    if x == password :
        print("ACCESS GRANTED")
    else :
        print("ACCESS DENIED")
passW(input())