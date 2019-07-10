#anju
aa = int(input())
while aa%10==0:
    aa=aa//10
aa=str(aa)
b=aa[::-1]
if aa==b:
    print("yes")
else:
    print("no")