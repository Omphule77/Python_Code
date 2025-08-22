num=int(input("Enter the number"))
a=0;b=1
print(a,b,end=" ")
for i in range(2,num):
    temp=a+b
    print(temp,end=" ")
    a=b
    b=temp
