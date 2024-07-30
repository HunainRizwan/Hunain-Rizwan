def max_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif  b>=a and b>=c:
        return b
    else:
        return c
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
d=int(input("Enter 3rd number:"))

print(max_of_three(a,b,c))