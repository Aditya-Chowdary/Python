l1 = [2,4,3]
l2 = [5,6,4]

result=[]
quotient = 0

for a,b in zip(l1,l2):
 if((a+b)//10 == 0):
   c=((a+b)%10)+quotient
 else:
   c=(a+b)%10
   quotient = (a+b)//10

 result.append(c)

print(result)