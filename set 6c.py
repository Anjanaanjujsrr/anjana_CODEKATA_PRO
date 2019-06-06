#anju
a=str(input())
a=a.lower()
l=len(a)
x=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,l):
	if(a[i] in x):
		x.remove(a[i])
if(len(x)==0):
	print("yes")
else:
	print("no")
