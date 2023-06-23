# # a file named "geek", will be opened with the reading mode.
# file = open('python4.py', 'r')
# # This will print every line one by one in the file
# for each in file:
# 	print (each)

# # Python code to illustrate read() mode
# file = open("python4.py", "r")
# print (file.read(30))

# # Python code to create a file
# file = open('python4.py','w')
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()

# file= open("python4.py","r")
# print(file.read())

# # Python code to illustrate append() mode
# file = open('geek.txt', 'a')
# file.write("This will add this line")
# file.close()

# # Python code to illustrate with()
# with open("geek.txt") as file:
# 	data = file.read()
# # do something with data

# # Python code to illustrate with() alongwith write()
# with open("geek.txt", "w") as f:
# 	f.write("Hello World!!!")

# # Python code to illustrate split() function
# with open("geek.text", "r") as file:
# 	data = file.readlines()
# 	for line in data:
# 		word = line.split()
# 		print (word)


import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(text)
		print("Text appended to file " + filename + " successfully.")
	except IOError:
		print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("Error: could not rename file " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + filename)


if __name__ == '__main__':
	filename = "example.txt"
	new_filename = "new_example.txt"

	create_file(filename)
	read_file(filename)
	append_file(filename, "This is some additional text.\n")
	read_file(filename)
	rename_file(filename, new_filename)
	read_file(new_filename)
	delete_file(new_filename)
