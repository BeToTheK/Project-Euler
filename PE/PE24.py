import time
import itertools
start=time.time()
k=sorted(list(itertools.permutations(range(10),10)))
print "".join(map(str,k[1000000-1]))
end=time.time()
print end-start
