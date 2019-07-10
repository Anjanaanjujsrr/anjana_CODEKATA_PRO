#anju
y=int(input())
x=2**y
a=[]
for i in range(0,x):
    l=bin(i)[2:].zfill(y)
    if(len(l)<len(bin(2**y-1)[2:])):
        a.append([l.count("1"),l])
    else:
        a.append([l.count("1"),l])
a.sort()
for i in range(len(a)):
    print(a[i][1])