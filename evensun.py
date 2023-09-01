n = int(input("Enter the range : "))
sum = 0
for i in range(1,n+1):
    if i%2 == 0:
        sum = sum + i
    else:
        pass
print("Total sum : ",sum)
