def main():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    NewArr = []
    print(arr)
    for i in range(len(arr)) :
        arr[i] += 2
    
        if arr[i] > 5 :
            NewArr.append(arr[i])
    print(NewArr)
main()