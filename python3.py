# python program to demonstrate the use of "//"
print(10//3)
print (-5//2)
print (5.0//2)
print (-5.0//2)

# Examples of Arithmetic Operator
a = 9
b = 4

# Addition of numbers
add = a + b

# Subtraction of numbers
sub = a - b

# Multiplication of number
mul = a * b

# Modulo of both number
mod = a % b

# Power
p = a ** b

# print results
print(add)
print(sub)
print(mul)
print(mod)
print(p)

# Examples of Relational Operators
a = 13
b = 33

a > b is False
print(a > b)

a < b is True
print(a < b)

a == b is False
print(a == b)

a != b is True
print(a != b)

a >= b is False
print(a >= b)

a <= b is True
print(a <= b)

# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)

# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)


# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")

# python program to illustrate If statement

i = 10

if (i > 15):
	print("10 is less than 15")
print("I am Not in if")

# python program to illustrate If else statement
i = 20
if (i < 15):
	print("i is smaller than 15")
	print("i'm in if Block")
else:
	print("i is greater than 15")
	print("i'm in else Block")
print("i'm not in if and not in else Block")

# python program to illustrate nested If statement
i = 10
if (i == 10):
	
	# First if statement
	if (i < 15):
		print("i is smaller than 15")
		
	# Nested - if statement
	# Will only be executed if statement above
	# it is true
	if (i < 12):
		print("i is smaller than 12 too")
	else:
		print("i is greater than 15")

# Python program to illustrate if-elif-else ladder
i = 20
if (i == 10):
	print("i is 10")
elif (i == 15):
	print("i is 15")
elif (i == 20):
	print("i is 20")
else:
	print("i is not present")

# Python program to illustrate short hand if
i = 10
if i < 15: print("i is less than 15")

# Python program to illustrate short hand if-else
i = 10
print(True) if i < 15 else print(False)
