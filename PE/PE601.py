def streak(n):
    i=1
    while n%i==0:
        n+=1
        i+=1
    return i-1

def p(s,capn):
    count=0
    l=[]
    for a in xrange(2,capn):
        l.append(streak(a))
    for el in l:
        if el==s:
            count+=1
        else:
            el+=1
    return count

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)
print lcm(6,5)


