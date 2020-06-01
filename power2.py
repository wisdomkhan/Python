#python 3.7.1
c=0
N=input("enter a number ")
print("you entered ",N)
n=int(N)
while n%2==0:
  c=c+1
  n=n/2
if n==1:
  print(N," is ",c," times raised to 2")
else:
  print("Not a multiple of 2")
    