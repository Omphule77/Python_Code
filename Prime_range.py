
def isPrime(num):
    if num<2:
        return False
    else:
        mid=int(num/2)
        for i in range(2,mid+1):
            if num%i==0:
                return False
    return True

lower=int(input("Enter the Number"))
upper=int(input("Enter the Number"))
for i in range(lower,upper+1):
    if isPrime(i):
        print(f"{i} is prime")


