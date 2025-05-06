import sys
import re

def main() :
    n = len(sys.argv)
    if n == 1 :
        print("none")
    else :
        for i in range(1, n) :
            if re.search(r'ism$', sys.argv[i]) :
                pass
            else :
                print(sys.argv[i] + "ism")
main()