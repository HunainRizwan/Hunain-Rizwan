a=float(input("Enter a side length:"))
b=float(input("Enter b side length:"))
c=float(input("Enter c side length:"))

if a == b == c:
    print("Equilateral Triangle")
elif a==b or b==c or c==a:
    print("Isosceles Triangle ")
else:
    print("Scalene Triangle")