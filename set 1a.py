#anju
a=input()
a=int(a)
L=[]
for i in range(0,a):  
    a1=input()
    L.append(a1)
Z=[]
for i in zip(*L):
    if i.count(i[0])==len(i): 
        Z.append(i[0])
    else:
        break
print(''.join(Z))