num=int(input("Enter the Number"))
isPrime=True
if num<2:
    isPrime=False
else:
    mid=int(num/2)
    for i in range(2,mid+1):
        if num%i==0:
            isPrime=False
            break

if isPrime:
    print("Prime")
else:
    print("Not Prime")
