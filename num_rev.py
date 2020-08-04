n=int(input("enter a number"))
while n!=0:
    d=n%10
    n-=d
    n=n/10
    print( int(d),end="")