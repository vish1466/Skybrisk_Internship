# Week 2 : Data Structures and Functions

# List
x = [3,4,2,1]

# Tuples
y = (1,2,3)

# Dictionaries
z = {
    1:'a',
    2:'c',
    3:'e'
}

# Sets
s = {1,2,3,1,3,4,4,4,5,3}

# Functions
def even_odd(num):
    # True if even, False if odd
    return (num/2 == 0)

# Lambda Functions
sqr_x = lambda x: x**2

a = int(input("Enter number to calculate squared value: "))
print(f"Square of the number {a}: ", sqr_x(a))

# Recursion - calling the function itself multiple times
def factorial(n):
    if n == 0:
        return 1
    else :
        return n * factorial(n-1)
    
n = int(input("Enter number to calculate factorial: "))
print(f"Factorial of {n} : ", factorial(n))

# List comprehension
squares = [x * x for x in range(5)]
cubes = [x**3 for x in range(3)]
print("Squares : ", squares, "\n", "Cubes : ", cubes)


# Hands-On Practice

# sum of squares
def sum_squares(a):
    squares = [x**2 for x in a]
    return sum(squares)

print("How many inputs (to calculate sum of squares)? ")
r = int(input())
list_temp = []
for i in range(r):
    temp = float(input(f"Enter number {i+1} : "))
    list_temp.append(temp)

print(sum_squares(list_temp))

# Filtering

# Even Numbers
even_num = list(filter(lambda x: x/2 == 0, list_temp))
print("Even Numbers : ", even_num)

# Greater than a certain number
greater_than_15 = list(filter(lambda x: x > 15, list_temp))
print("List (>15) : ", greater_than_15)


