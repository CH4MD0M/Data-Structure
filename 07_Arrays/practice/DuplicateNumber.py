def removeDuplicates(myList):
    # TODO
    result=[]
    for i in myList:
        if i not in result:
            result.append(i)
    return result

print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))
