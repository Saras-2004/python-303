n=int(input("enter the no of apples: "))
m=int(input("enter the no of flowers: "))
counti=0
countj=0
for i in range(n):
    for j in range(m):
        countj+=1
    counti=counti+1
print("apples delivered are:",counti,",flowers delivered are:",countj)
        
        
