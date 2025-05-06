import sys

def main() :
    n = len(sys.argv)
    if n == 1 :
        print("none")
    else :
        cou = 0
        cou += sys.argv[1].count("z")

        if not cou :
            print("none")
        else :
            print("z" * cou)
main()