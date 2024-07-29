n=eval(input("enter the year"))
if n%400==0:
    print(n,"leaf year")
elif n%100==0:
    print(n,"not leaf year")
elif n%4==0:
    print(n,"leap year")
else:
    print(n,"it is not leaf year")
