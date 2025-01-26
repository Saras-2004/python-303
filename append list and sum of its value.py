a=[]
sum=0
n=int(input("number of times to be executed= "))
for i in range(n):
    x=int(input("enter the no " + str(i+1) +  "= "))
    a.append(x)
    sum=sum+x
print(a)
print(sum)
