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
for i in range(4):
  if man>1:
    man=str(man)
    a,b=man.split(".")
    man=float(b)
    while man>1:
      man/=10
    dig=int(man*2)
    d.append(dig)
    man=float(man*2)
  elif man==0 or man==1:
    break
  else:
    dig=int(man*2)
    d.append(dig)
    man=float(man*2)
#to print the value
for i in w:
    print(i,end="")
# if f is 1 then input value is a fraction and we need to print the mantissa after .
if f==1: 
  print(end=".")
  for i in d:
    print(i,end="")
