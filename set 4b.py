#anju
te=input()
dum=0
for i in range(0,len(te)-1):
  for j in range(i+1,len(te)):
    if te[i]<te[j]:
      dum=1
      print(te[j:])
      break
  if dum==1:
    break
  else:
    print(te)
