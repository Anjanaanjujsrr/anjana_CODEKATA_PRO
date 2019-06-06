#anju
Num=int(input())
l1=list(map(int,input().split()))
l2=[]
for i in l1:
	s=bin(i)[2::]
	l2.append(([s.count("1"),i]))
l2.sort(reverse=True)
for i in range(0,len(l2)):
	print(l2[i][1])