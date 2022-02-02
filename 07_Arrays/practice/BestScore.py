def firstSecond(givenList):
    result=sorted(givenList,reverse=True)
    return tuple(result[0:2])


myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(firstSecond(myList))
