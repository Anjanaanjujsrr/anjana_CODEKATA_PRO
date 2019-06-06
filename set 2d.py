#anju
a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b):
	u,v=map(int,input().split())
	c=l[u-1:v]
	a=c[0]
	for j in range(1,len(c)):
		a=a^c[j]
	print(a)