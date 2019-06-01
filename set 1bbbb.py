#anju
from itertools import combinations
N,K=map(int,input().split())
S=len(str(N))
L=list(combinations(str(N),S-K))
L=sorted(L)
print("".join(L[0]))
