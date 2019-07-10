#anju
num=input()
lum=len(num)
dum=0
for lo in range(0,lum):
    s=num[0:lo]+num[lo+1::]
    if int(s)%8==0:
        dum=1
        break
if dum==1:
    print("yes")
else:
    print("no")