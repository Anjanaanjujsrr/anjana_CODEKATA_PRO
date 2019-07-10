a,b = input().split()
b = int(b)
c = False
l = list(map(int,input().split()))
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j] == b:
            c = True
print("yes" if c else "no")   