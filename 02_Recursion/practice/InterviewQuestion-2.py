def power(base,exp):
    assert exp>=0 and int(exp)==exp,'The exponent must be integer only!'
    if exp==0:
        return 1
    else:
        return base * power(base,exp-1)

print(power(5,2))
