#anju
t1 = int(input())
a1 = list(map(int,input().split()))
s,l = 0,[]
b1 = [x for x in range(1,t1+1)]
for i in a1:
  if i in b1:
    b1.remove(i)
kh = 0
for i in range(0,t1-1):
  p = a1[i]
  for j in range(i+1,th):
    if p == a1[j]:
      if p < b1[kh]:
        a1[j] = b1[kh]
        s += 1
      else:
        a1[i] = b1[kh]
        s += 1
      kh += 1
print(s)
print(*a1)