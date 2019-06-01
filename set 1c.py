#anju
x,y=input().split()
z=abs(len(x)-len(y))
for i in range(len(x)):
	if len(y)==1 and y[i] in x:
		break
	if x[i]!=y[i]:
		z=z+1
print(z)