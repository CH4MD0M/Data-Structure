def factorial(n):
    assert n>=0 and int(n)==n, "숫자는 정수이어야 합니다."
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
