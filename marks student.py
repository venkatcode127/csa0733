m=int(input("enter the mark of dsubject"))
if m>=90:
    grade='f'
elif m>=80 and m<90:
    grade='a'
elif m>=70 and m<80:
    grade='b'
elif m>=60 and m<70:
    grade='c'
else:
    grade='s'
print(m,"grade=",grade)
