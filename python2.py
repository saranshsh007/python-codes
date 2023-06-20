 # Python program to demonstrate
 # Creation of Set in Python
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)
# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)
# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)
# Creating a Set with
# the use of a tuple
t=("Geeks","for","Geeks")
print("\nSet with the use of Tuple: ")
print(set(t))
# Creating a Set with
# the use of a dictionary
 d={"Geeks":1,"for":2,"Geeks":3}
 print("\nSet with the use of Dictionary: ")
 print(set(d))
 # Creating a Set with
 # a List of Numbers
 # (Having duplicate values)
 set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
 print("\nSet with the use of Numbers: ")
 print(set1)
 # Creating a Set with
 # a mixed type of values
 # (Having numbers and strings)
 set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
 print("\nSet with the use of Mixed Values")
 print(set1)
                                                                                                         
 Python program to demonstrate
 Addition of elements in a Set
 Creating a Set
 set1 = set()
 print("Initial blank Set: ")
 print(set1)
 # Adding element and tuple to the Set
 set1.add(8)
  set1.add(9)
  set1.add((6, 7))
  print("\nSet after Addition of Three elements: ")
  print(set1)
  # Adding elements to the Set
  # using Iterator
  for i in range(1, 6):
  	set1.add(i)
  print("\nSet after Addition of elements from 1-5: ")
  print(set1)
  # Addition of elements to the Set
  # using Update function
  set1 = set([4, 5, (6, 7)])
  set1.update([10, 11])
  print("\nSet after Addition of elements using Update: ")
  print(set1)
  # Creating a set
  set1 = set(["Geeks", "For", "Geeks."])
  print("\nInitial set")
  print(set1)
  #Accessing element using
   # for loop
   print("\nElements of set: ")
   for i in set1:
       print(i, end=" ")

  # Checking the element
  # using in keyword
  print("\n")
  print("Geeks" in set1)
 # Python program to demonstrate
 # Deletion of elements in a Set
 # Creating a Set
  set1 = set([1, 2, 3, 4, 5, 6,
              7, 8, 9, 10, 11, 12])
  print("Initial Set: ")
  print(set1)
 # Removing elements from Set
  # using Remove() method
  set1.remove(5)
  set1.remove(6)
  print("\nSet after Removal of two elements: ")
  print(set1)
 # Removing elements from Set
  # using Discard() method
  set1.discard(8)
  set1.discard(9)
  print("\nSet after Discarding two elements: ")
  print(set1)

  # Removing elements from Set
  # using iterator method
  for i in range(1, 5):
      set1.remove(i)
  print("\nSet after Removing a range of elements: ")
  print(set1)
  #Python program to demonstrate
  #working of a FrozenSet
  #Creating a Set
  String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
  Fset1 = frozenset(String)
  print("The FrozenSet is: ")
  print(Fset1)
  # To print Empty Frozen Set
  # No parameter is passed
  print("\nEmpty FrozenSet: ")
  print(frozenset())
  def create_set():
  	my_set = {1, 2, 3, 4, 5}
  	print(my_set)
  def add_element():
  	my_set = {1, 2, 3, 4, 5}
  	my_set.add(6)
  	print(my_set)
  def remove_element():
  	my_set = {1, 2, 3, 4, 5}
  	my_set.remove(3)
  	print(my_set)
  def clear_set():
  	my_set = {1, 2, 3, 4, 5}
  	my_set.clear()
  	print(my_set)
  def set_union():
  	set1 = {1, 2, 3}
  	set2 = {4, 5, 6}
  	my_set = set1.union(set2)
  	print(my_set)
  def set_intersection():
  	set1 = {1, 2, 3, 4, 5}
  	set2 = {4, 5, 6, 7, 8}
  	my_set = set1.intersection(set2)
  	print(my_set)
  def set_difference():
  	set1 = {1, 2, 3, 4, 5}
  	set2 = {4, 5, 6, 7, 8}
  	my_set = set1.difference(set2)
  	print(my_set)
  def set_symmetric_difference():
  	set1 = {1, 2, 3, 4, 5}
  	set2 = {4, 5, 6, 7, 8}
  	my_set = set1.symmetric_difference(set2)
  	print(my_set)
  def set_subset():
  	set1 = {1, 2, 3, 4, 5}
  	set2 = {2, 3, 4}
  	subset = set2.issubset(set1)
  	print(subset)
  def set_superset():
  	set1 = {1, 2, 3, 4, 5}
  	set2 = {2, 3, 4}
  	superset = set1.issuperset(set2)
  	print(superset)
  if __name__ == '__main__':
  	create_set()
  	add_element()
  	remove_element()
  	clear_set()
  	set_union()
  	set_intersection()
  	set_difference()
  	set_symmetric_difference()
  	set_subset()
  	set_superset()
  Dict = {1:'geeks',2:'For',3:'Geeks'}
  print(Dict)
  Dict={'Name' : 'geeks' , 1: [1,2,3,4]}
  print("\nDictionary with the use of Mixed keys : ",Dict)
  # Creating a Dictionary
  # with each item as a Pair
  Dict = dict([(1, 'Geeks'), (2, 'For')])
  print("\nDictionary with each item as a pair: ")
  print(Dict)
  # Creating a Nested Dictionary
  # as shown in the below image
  Dict = {1: 'Geeks', 2: 'For',
  		3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
  print(Dict)
  # demo for all dictionary methods
  dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
  # copy() method
  dict2 = dict1.copy()
  print(dict2)
  # clear() method
  dict1.clear()
  print(dict1)
  # get() method
  print(dict2.get(1))
  # items() method
  print(dict2.items())
  # keys() method
  print(dict2.keys())
  # pop() method
  dict2.pop(4)
  print(dict2)
  # popitem() method
  dict2.popitem()
  print(dict2)
  # update() method
  dict2.update({3: "Scala"})
  print(dict2)
  # values() method
  print(dict2.values())
  import array as arr
  a = arr.array('i',[1,2,3,4,5])
  for i in range (0,5) :
      print(a[i])
 # Python program to demonstrate
 # Adding Elements to a Array
 # importing "array" for array creations
 import array as arr
 # array with int type
 a = arr.array('i', [1, 2, 3])
 print("Array before insertion : ", end=" ")
 for i in range(0, 3):
 	print(a[i], end=" ")
	print()
 # inserting array using
 # insert() function
 a.insert(1, 4)
 print("Array after insertion : ", end=" ")
 for i in (a):
 	print(i, end=" ")
 print()
 # array with float type
 b = arr.array('d', [2.5, 3.2, 3.3])
 print("Array before insertion : ", end=" ")
 for i in range(0, 3):
 	print(b[i], end=" ")
  print()
  # adding an element using append()
  b.append(4.4)
  print("Array after insertion : ", end=" ")
  for i in (b):
  	print(i, end=" ")
  print()
 # Python program to demonstrate
 # accessing of element from list
 # importing array module
 import array as arr
 # array with int type
 a = arr.array('i', [1, 2, 3, 4, 5, 6])
 # accessing element of array
 print("Access element is: ", a[0])
 # accessing element of array
 print("Access element is: ", a[3])
 # array with float type
 b = arr.array('d', [2.5, 3.2, 3.3])
 # accessing element of array
 print("Access element is: ", b[1])
 # accessing element of array
 print("Access element is: ", b[2])
 #Python program to demonstrate
 #Removal of elements in a Array
 #importing "array" for array operations
 import array
 # initializing array with array values
 # initializes array with signed integers
 arr = array.array('i', [1, 2, 3, 1, 5])
 # printing original array
 print("The new created array is : ", end="")
 for i in range(0, 5):
 	print(arr[i], end=" ")
 print("\r")
 # using pop() to remove element at 2nd position
 print("The popped element is : ", end="")
 print(arr.pop(2))
 # printing array after popping
 print("The array after popping is : ", end="")
 for i in range(0, 4):
 	print(arr[i], end=" ")
 print("\r")
 # using remove() to remove 1st occurrence of 1
 arr.remove(1)
 # printing array after removing
 print("The array after removing is : ", end="")
 for i in range(0, 3):
 	print(arr[i], end=" ")
 #Python code to demonstrate
 #searching an element in array
 #importing array module
import array
# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])
 # printing original array
 print("The new created array is : ", end="")
 for i in range(0, 6):
 	print(arr[i], end=" ")
 print("\r")

 # using index() to print index of 1st occurrence of 2
print("The index of 1st occurrence of 2 is : ", end="")
 print(arr.index(2))
  # using index() to print index of 1st occurrence of 1
 print("The index of 1st occurrence of 1 is : ", end="")
 print(arr.index(1))
 # Python code to demonstrate
 # how to update an element in array
 # importing array module
 import array
 # initializing array with array values
 # initializes array with signed integers
 arr = array.array('i', [1, 2, 3, 1, 2, 5])
# printing original array
print("Array before updation : ", end="")
for i in range(0, 6):
	print(arr[i], end=" ")

 print("\r")

# updating a element in a array
 arr[2] = 6
 print("Array after updation : ", end="")
 for i in range(0, 6):
 	print(arr[i], end=" ")
 print()

# updating a element in a array
 arr[4] = 8
 print("Array after updation : ", end="")
 for i in range(0, 6):
 	print(arr[i], end=" ")


import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 2, 5, 2])

# Count the number of occurrences of the element 2 in the array
count = my_array.count(2)

# Print the result
print("Number of occurrences of 2:", count)


import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Print the original array
print("Original array:", *my_array)

# Reverse the array in place
my_array.reverse()

# Print the reversed array
print("Reversed array:", *my_array)
