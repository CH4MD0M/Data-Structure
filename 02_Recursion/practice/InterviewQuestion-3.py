def gcd(a,b):
    assert int(a)==a and int(b)==b, 'The number must be integer only!'

    if a<b:
        a,b=b,a

    if a&b==0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(48,60))
