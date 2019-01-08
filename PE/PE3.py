l=[]
def trial_div(p):
    n = 2
    while p>1:
        if p%n==0:
            l.append(p)
            p=p/n
        else:
            n=n+1
    return l

print trial_div(107)

            
            
    
