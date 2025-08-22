num=int(input("Enter the Number"))
if year%400==0:
    print(f"{year} is leap")
elif year%4==0 and year%100!=0:
    print(f"{year} is leap")
else:
    print(f"{year} is not leap")
