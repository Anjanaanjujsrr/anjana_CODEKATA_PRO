#anju
inp=int(input())

i=0

a=0

b=[]

while i<90 and i<inp:

  s=0

  for j in str(inp-i):

    s+=int(j)

  if s+(inp-i)==inp:

    a+=1

    b.append(inp-i)

  i+=1

print(a)

for i in b:

  print(i)