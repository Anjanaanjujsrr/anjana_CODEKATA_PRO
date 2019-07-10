#anju
vf,vk=map(int,input().split())
sk=[]
for i in range(0,vf):
    mm=[int(sv) for sv in input().split()]
    sk.append(sorted(mm))
for i in range(0,len(sk[0])):
  for j in range(0,len(sk)-1):
    if sk[j][i]>sk[j+1][i]:
      sk[j][i],sk[j+1][i]=sk[j+1][i],sk[j][i]
for i in sk:
  print(*i)