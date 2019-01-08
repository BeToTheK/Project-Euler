l=[]
def f(n):
    f1=1
    f2=1
    k=3
    c=3
    while n>2:
        fn=f1+f2
        f1=f2
        f2=fn
        if len(str(fn))<1000:
            if k==n:
                return fn
            else:
                n=n-1
                c=c+1
        else:
            l.append(c)
            break
    return fn

print f(1000000),l
print len(str(f(4782)))
