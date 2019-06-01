#anju
s,r=input().split()
s=int(s)
r=int(r)
ar=[int(i) for i in input().split()]

w=[]
z=[]
for i in range(0,r):
    x,y=input().split()
    w.append(x)
    z.append(y)


for i in range(0,r):
    s=int(w[i])-1

    t=int(z[i])-1


    for j in range(1,ar[s]+1):
        if (ar[s]%j==0 and ar[t]%j==0):
            gcd=j
    print(gcd)