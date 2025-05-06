import sys

def main() :
    n = len(sys.argv)
    if n == 1 :
        print("none")
    else :
        txt = input("What was the parameter? ")

        if txt == sys.argv[1] :
            print("Good job!")
        else :
            print("Nope, sorry...")
main()


