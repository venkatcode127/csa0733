n=int(input("enter the value of n"))
temp=n
sum=0
while n!=0:
    r=n%10
    sum=sum+r*r*r
    n=n//10
if sum==temp:
    print("armstro number")
else:
    printf("not armstrong")
    
