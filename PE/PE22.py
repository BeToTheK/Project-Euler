import time
start=time.time()
ans=0
nxt=0
sm=0
for x in xrange(0,5163):
    new=0
    with open('names.txt', "r") as word_list:
        words = word_list.read().split('","')
        words=sorted(words)[x]
        for word in words:
            c=str(word)
            for s in c:
                i=1
                while i<=len(c):
                    k=ord(s)-64
                    sm=k+new
                    new=sm
                    #print sm
                    i+=1
        #print words,sm,"*",x+1
        #print words,"=",sm*(x+1)
    ans=sm*(x+1)+nxt
    nxt=ans
print "tot:",ans
end=time.time()
print end-start
        
