from itertools import permutations
def countways(n,k):
    comb = permutations([i for i in range(1,n+1)],k)
    ans = []
    for i in list(comb):
        ans.append(i)
        
    return ans