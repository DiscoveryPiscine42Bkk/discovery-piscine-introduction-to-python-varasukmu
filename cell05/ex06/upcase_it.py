import sys

def main():
    try :
        print(sys.argv[1].upper())
    except :
        print("none")
main()