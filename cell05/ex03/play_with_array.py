def main():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    sArr = set()

    print(arr)

    for i in range(len(arr)) :
        arr[i] += 2
    
        if arr[i] > 5 :
            sArr.add(arr[i])
        
    print(sArr)
main()