import sys

def main():
    try :
        print(sys.argv[1].lower())
    except :
        print("none")
main()