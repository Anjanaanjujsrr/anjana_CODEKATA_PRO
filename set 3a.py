#anju
v1=int(input())
v2=list(map(int,input().split()))
ans=int(v1/2)
r1=v2[:ans]
r2=v2[ans::]
if ((sum(r1)//len(r1))==(sum(r2)//len(r2))):
    print("yes")
else:
    print("no")