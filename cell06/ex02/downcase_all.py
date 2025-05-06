#!/usr/bin/python3 

import sys

def main() :
    n = len(sys.argv)
    if n == 1 :
        print("none")
    else :
        for i in range( 1 , n ) :
            print(sys.argv[i].lower())
main()