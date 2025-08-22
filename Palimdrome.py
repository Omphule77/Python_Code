num=int(input("Enter the number"))
rev=0
num1=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=int(num/10)
print(f"rev: {rev}")
if num1==rev:
    print("Palindrome")
else:
    print("Not Palimdrome")
