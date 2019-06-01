#anju
a=input()
b=input()
t=[]
for x,y in zip(a,b):
    t.append(chr(ord('a')+((ord(x)-ord('a')+ord(y)-ord('a'))%26)+1))
print("".join(t))   
