#anju
num=int(input())
m1=list(map(int,input().split()))
m1.sort()
sin=0
c1=0
for i in range(len(m1)):
    if m1[i]>=s:
        c1=c1+1
    s=s+m1[i]
print(c1)