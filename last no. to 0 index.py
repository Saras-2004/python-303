a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    x = int(input("Enter a number: "))
    a.append(x)
last_number = a.pop()  
a.insert(0, last_number)  
print(a)
