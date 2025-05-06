#!/usr/bin/python3 

def mult() :
    num1 = int(input("Enter the first number:\n"))
    num2 = int(input("Enter the second number:\n"))
    sumnum = num1 * num2
    print(f"{num1} x {num2} = {sumnum}")

    if sumnum == 0 :
        print("The result is positive and negative.")
    elif sumnum <0 :
        print("The result is negative.")
    elif sumnum > 0 :
        print("The result is positive.")
mult()