# Program to Demonstrate Generator Expressions

squares = (x * x for x in range(1, 6))

print("Squares using Generator Expression:")

for value in squares:
    print(value)
