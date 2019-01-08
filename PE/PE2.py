fibo=[0,1]
for i in range (1000):
    x=fibo[i-1]+fibo[i-2]
    fibo.append(fibo[i-1]+fibo[i-2])
    if x>4000000:
        break
result = list(filter(lambda x: (x % 2 == 0), fibo))
print(result)
print(sum(result))
