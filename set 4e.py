#anju
asd = int(input())
qwe = [ int(x) for x in input().split()]
asd = len(qwe)
uu = 0
for i in range(0,asd-2):
    for j in range(i+1, asd-1):
        for k in range(j+1, asd):
            if qwe[i] > qwe[j] > qwe[k] :
                uu =uu+ 1
print(uu)