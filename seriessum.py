n=int(input("Enter number : "))
total=0
for i in range(1,n+1):
    print(1/i,end='+')
    total=total+1/i
print("Total is",total)   
