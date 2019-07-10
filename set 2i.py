#anju
a=int(input())
b=[]
for i in range(0,a):
    l=list(map(int,input().split()))
    for j in l:
        b.append(j)
print(*sorted(b),end="")
