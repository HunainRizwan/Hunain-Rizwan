 
def square_set(numbers):
    return {n**2 for n in numbers}
x = {1, 2, 3, 4, 5}
print(square_set(x))
print(type(x))
