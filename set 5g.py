#anju
AA=input().split()
BB=int(AA[1])
CC=int(AA[0])
DD=[int(P) for P in AA[0]]
X=0
y=1;
while(X==0):
	prod=y*CC
	l=[ int(P) for P in str(prod)]
	k=0
	j=len(l)-1
	while(l[j]==0):
		k=k+1
		j=j-1
	if(k>=BB):
		print(prod)
		X=1
	y=y+1