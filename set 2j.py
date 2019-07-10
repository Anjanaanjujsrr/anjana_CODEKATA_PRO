#anju
a=input().split()
total=int(a[0])
coin=int(a[1])
l=input().split()
l=[int(i) for i in l]
l=sorted(l,reverse=True)
temp=0
count=0
for i in range(0,len(l)):
  while True:
    if(temp==coin):
      break
    elif(temp>coin):
      count-=1
      temp-=l[i]
      break
    elif(temp<coin):
      temp+=l[i]
      count+=1
print(count)