import sys

def main():
    n = len(sys.argv) - 1
    for i in range(n, 0, -1):
        print(sys.argv[i])
        
main()