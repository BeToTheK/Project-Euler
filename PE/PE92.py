#Square Digit Chains
l=[]
def f(x):
    sum=0
    min=1
    max=89
    s=str(x)
    for i in s:
        sum=int(i)**2+sum
        #print(x,sum)
        cnt=sum
    if cnt==max:
        l.append(sum)
    elif cnt==min:
        pass
    else:
        return f(cnt)
    return l

for i in range(1,10000000):
    f(i)

print(len(l))