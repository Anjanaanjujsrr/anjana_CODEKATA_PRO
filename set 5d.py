#anju
t1,t2,t3,t4=map(int,input().split())
li=list(map(int,input().split()))
xi=[]
for i in range(0,len(li)):
    for j in range(i,len(li)):
        for k in range(j,len(li)):
            xi.append(t2*li[i]+t3*li[j]+t4*li[k])
print(max(xi))