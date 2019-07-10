#anju
t1,t2=map(int,input().split())
li=list(map(int,input().split()))
if t2==1:
  print(min(li))
elif t2==2:
  print(max(li[0],li[t1-1]))
else:
  print(max(li))