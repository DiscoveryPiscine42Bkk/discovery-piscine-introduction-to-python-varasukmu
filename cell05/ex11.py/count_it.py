import sys
def main() :
    n = len(sys.argv)
    if n == 1 :
        print("none")
    else :
        print("parameters:", n-1)

        for i in range(1, n) :
            print(f"{sys.argv[i]}: {len(sys.argv[i])}")
main()