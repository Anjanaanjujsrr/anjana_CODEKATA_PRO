A,B=map(int,input().split())
C=list(map(int,input().split()))
P=list(map(int,input().split()))
Q=[]
r=0
for i in range(A):
    x=P[i]/C[i]
    Q.append(x)
while B>=0 and len(Q)>0:
    mindex=Q.index(max(Q))
    if B>=C[mindex]:
        r=r+p[mindex]
        B=B-C[mindex]
    C.pop(mindex)
    P.pop(mindex)
    Q.pop(mindex)
print(r)