AAA,BBB=map(int,input().split())
CCC=list(map(int,input().split()))
pp=list(map(int,input().split()))
qq=[]
rr=0
for i in range(AAA):
    x=pp[i]/CCC[i]
    qq.append(x)
while BBB>=0 and len(qq)>0:
    mindex=qq.index(max(qq))
    if BBB>=CCC[mindex]:
        rr=rr+pp[mindex]
        BBB=BBB-CCC[mindex]
    CCC.pop(mindex)
    pp.pop(mindex)
    qq.pop(mindex)
print(rr)
