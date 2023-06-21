num = 0
for i in range(10):
	num += 1
	if num == 8:
		break
	print("The num has value:", num)
print("Out of loop")
# Python program to
# demonstrate break statement

s = 'geeksforgeeks'
# Using for loop
for letter in s:

	print(letter)
	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'e' or letter == 's':
		break

print("Out of for loop" )
print()

i = 0

# Using while loop
while True:
	print(s[i])

	# break the loop as soon it sees 'e'
	# or 's'
	if s[i] == 'e' or s[i] == 's':
		break
	i += 1

print("Out of while loop ")


# prints all the elements in the nested list
# except for the ones with value 3
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in nested_list:
	for j in i:
		if j == 3:
			continue
		print(j)

li =['a', 'b', 'c', 'd']

for i in li:
	if(i =='a'):
		pass
	else:
		print(i)

# python code to demonstrate working of enumerate()

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
	print(key, value)

questions = ['name' , 'color','shape']
answers = ['apple','red','circle']

for questions , answers in zip(questions,answers):
    print('what is your {0} ? i am {1}'.format(questions,answers))

# python code to demonstrate working of items()

king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
		'Modi': 'The Changer'}

# using items to print the dictionary key-value pair
for key, value in king.items():
	print(key, value)

# python code to demonstrate working of sorted()

# initializing list
lis = [1, 3, 5, 6, 2, 1, 3]

# using sorted() to print the list in sorted order
print("The list in sorted order is : ")
for i in sorted(lis):
	print(i, end=" ")

print("\r")

# using sorted() and set() to print the list in sorted order
# use of set() removes duplicates.
print("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
	print(i, end=" ")


# python code to demonstrate working of reversed()

# using reversed() to print in reverse order
for i in reversed(range(1, 10, 3)):
	print(i)

