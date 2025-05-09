count = {
        "K" : 0, "Q" : 0, "B" : 0, "R" : 0, "P" : 0 
    }

# if all(x == 0 for x in count):
#     print("Now you have just only board, How do u play? Hmmm")
# else :
#     print("not")

for x in count.values() :
    print(x, x==0)