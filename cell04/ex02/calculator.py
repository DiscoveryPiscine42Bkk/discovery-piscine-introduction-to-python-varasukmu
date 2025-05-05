def main():
    n1 = int(input("Give me the first number: "))
    n2 = int(input("Give me the second number: "))
    print("Thank you!")

    x = n1/n2

    if not x%1 : 
        x = int(x)
    else : x = f"{x:.2f}"

    print(f"{n1} + {n2} = {n1+n2}")
    print(f"{n1} - {n2} = {n1-n2}")
    print(f"{n1} / {n2} = {x}")
    print(f"{n1} * {n2} = {n1*n2}")
main()