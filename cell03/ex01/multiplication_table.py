#!/usr/bin/python3 

def table() :
    num = int(input("Enter a number\n"))

    for i in range(0, 10) :
        print(f"{i} x {num} = {i*num}")
table()