n = int(input("Enter total number of seconds: "))
hours = n//(60*60)
n = n%(60*60)
minutes = n//60
n = n%60
print("Hours : ",hours)
print("Minutes : ",minutes)
print("Seconds : ",n)
