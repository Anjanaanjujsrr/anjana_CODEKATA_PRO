#anju
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
	u,v=map(int,input().split())
	c=l[u-1:v]
	print(sum(c))
