print ("hello world")


a= 'this is a string'
print(a)
b= "this is also a string"
print(b)
L = [1 , "saransh" , "a" , 10*8]
print (L)
L.append(6)
print(L)
L.pop(2)
print(L)
print("2nd values is :- ",L[2])

tup = (1 , "tuple" , "a" , 10+8)
print(tup)  
print(tup[1])

s ="Hello World"
for i in s : 
    print(i)

L = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
for i in L:
    print(i+2)


c='''this is also a string'''
print(c)
print(c[::-1])
c = "".join(reversed(c))
print(c)

string1 = "saranshSharma"
print("Initial String : ",string1)
print("\nSlicing characters from 3-12 : ",string1[3:12])
print("\nSlicing characters between " + "3rd and 2nd last character : ",string1[3:-2])

string1 = "hello , i m geek"
print(string1)

list1 = list(string1)
list1[2] = 'p'
string2 = ''.join(list1)
print("\nUpdating character at 2nd Index ",string2)
print(string2)

string3 = string1[0:2] + 'p' + string1[3:]
print(string3)


string1 = "Hello , i m geek"
print("Initial String : ",string1)
string1 ="welcome to the club"
print("Updated string : ",string1)

string1 = "Hello , i m geek"
print("Initial String : ",string1)
string2 = string1[0:2]+string1[3:]
print("Deleting character at 2nd index : ",string2)


string1 = "Hello , i m geek"
print("Initial String : ",string1)
del string1
print("Deleting entire string : ",string1)
   
string1 = '''I'm a "Geek"'''
print(string1)
string2 = "I'm a \"geek\""
print(string2)
string3 = "C:\\Python\\Geeks\\"
print("\nEscaping backslashes : ",string3)
string4 = "Python\nGeeks"
print("\ntab: ",string4)
string5 = "Python\nGeeks"
print("\nNew Line : ",string5)


string1 = "{} {} {}".format('geeks','for','life')
print("\nPrint String in default order : ",string1)

string1 = "{1} {0} {2}".format('Geeks','for','life')
print("\nPrint string in positional order : ",string1)

string1 = "{l} {f} {g}".format(g='Geeks',f='for',l='life')
print("\nPrint string in order of keywords : ",string1)
