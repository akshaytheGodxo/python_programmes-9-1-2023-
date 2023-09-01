n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

c1 = n1>n2
c2 = n1<n2
c3 = n1==n2

print("Larger is "*c1+str(n1)*c1 + "Larger is "*c2+str(n2)*c2 + "Both are equal "*c3)

