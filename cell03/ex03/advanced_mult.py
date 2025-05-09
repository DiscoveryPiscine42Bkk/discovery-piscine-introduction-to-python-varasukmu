#!/usr/bin/python3 

# def main() :
#     for i in range(0, 11):
#         print(f"Table de {i}:", end=" ")
#         for j in range(0, 11) :
#             print(f"{i * j}", end=" ")
#         print()

# main()


import sys

def main() :
        i = 0
        while i < 11 :
            print(f"Table de {i}:", end=" ")
            j = 0
            while j < 11 :
                print(f"{i * j}", end=" ")
                j += 1
            print()

            i += 1


if len(sys.argv) == 1 :
    main()
    
else :
    print("none")


