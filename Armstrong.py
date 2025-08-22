import math
def num_len(num):
    return len(str(num))
    
    
def arm(num,len):
    sum=0;temp=num
    while num>0:
        digit=num%10
        sum=sum+math.pow(digit,len)
        num=int(num/10)
    return temp==sum

num=int(input("Enter the number"))
len=num_len(num)
print(len)

if(arm(num,len)):
    print("Armstrong")
else:
    print("Not Armstrong")

