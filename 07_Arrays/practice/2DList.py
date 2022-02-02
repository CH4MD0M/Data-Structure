def sumDiagonal(a):
    result=0
    for i in range(len(a)):
        result+=a[i][i]
    return result



myList2D= [[1,2,3],[4,5,6],[7,8,9]]

print(sumDiagonal(myList2D))
