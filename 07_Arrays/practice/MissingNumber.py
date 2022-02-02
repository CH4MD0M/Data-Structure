def missingNumber(myList,totalCount):
    for i in range(totalCount):
        if myList[i]!=i+1:
            break
    
    return i+1



print(missingNumber([1,2,3,4,6],6))

