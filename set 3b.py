#anju
a=int(input())
b=list(map(int,input().split()))
su=0
se=0
for i in range(a):
	if i%2==0:
		su=su+b[i]
	else:
		se+=b[i]
print(max(su,se))