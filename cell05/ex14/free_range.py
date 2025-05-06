import sys

def main() :
    n = len(sys.argv)
    if n == 1 :
        print("none")
    elif n == 3 :
        lnum = []
        for i in range( int(sys.argv[1]) , int(sys.argv[2]) + 1 ) :
            lnum.append(i)
        print(lnum)
main()