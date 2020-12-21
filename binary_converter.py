n=input("enter a number: ")
f=0 # a flag varibale to check if the input value is a whole number or fraction
if '.' not in n:
  exp=int(n)
  man=0
else:
  f=1
  exp,man=n.split(".")
  exp=int(exp)
  man=float(man)
  while man>1:
    man/=10

#to convert the whole number part
w=[]
while(exp>0):
    dig=exp%2
    w.append(dig)
    exp=exp//2
w.reverse()

#to convert the decimal part
d=[]
for i in range(10):
  if man>0:
    temp=man*2
    dig=int(temp)
    d.append(dig)
    man=temp-dig
  else :
    break
#to print the value
for i in w:
    print(i,end="")
# if f is 1 then input value is a fraction and we need to print the mantissa after .
if f==1: 
  print(end=".")
  for i in d:
    print(i,end="")
