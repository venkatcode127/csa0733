p=eval(input("enter the amount"))
t=eval(input("time"))
r=eval(input("rate"))
n=eval(input("value of n"))
compound_intrest=p*(1+r/n)**n*t-p
print("compund interest=",compound_intrest)
