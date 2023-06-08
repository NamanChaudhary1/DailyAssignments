import random as r
Set         = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
SetSize     = 5
ResultList  = set()    
Iterations  = 1000   
r.seed(42)
for i in range(Iterations):
    Chromosome = r.sample(Set,SetSize)
    Chromosome.sort()
    if sum(Chromosome) == 0:
        ResultList.add(tuple(Chromosome))
for r in ResultList:
	print (r)
print ("\nTotal Sets: ", len(ResultList))
