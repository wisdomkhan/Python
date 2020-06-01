#python 3.7.1
c=0
n=input("Enter a number ")
N=int(n)
p=input("Enter base ") #user inputs no. whose power he wants
p=int(p)
if N%p!=0:
  print("Oh oh! ", n ," is not a multiple of ", p)
  quit()
while N%p==0:
  c+=1
  N/=p
if N==1:
  print(n," is ", c ," times raised to ", p)
else:
  print(n," is ", c ," times raised to ", p, " and ", N, " is left as remainder")