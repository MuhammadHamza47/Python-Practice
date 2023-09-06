print("Muhammad Hamza");
if 5 > 2:
  print("Five is greater than two!")
#   This is a comment
"""
 this is a comment 
 about variable declaration
 for example:
 """
x = 4;
y =5;
z = x+y;
print(z)
a = "Hello"
b= str(3)
c = int(3)
d = float(3)
print(type(d))
# A and a are both different
a= 4;
A = 5
print(a)
print(A)

# declare a multiple variable and assign a value in single line

a, d, e = 2, 3, 4;
print(a)
print(d)
print(e)

x = ("apple", "banana", "cherry")
print(type(x))

# global scope

x= "awesome"

def myFunc ():
    global x
    x= "funtastic"
myFunc()
print("Python is" ,x)


# string 

x= "python"
print(x[3])

for item in "skdvsfnvfkj":
    print(item)
    
x = "python is very simple"
if "is " in x:
    print("Yes, 'Is' present in x")
    

# formate 

age = 24
txt = "My name is Hamza and my age is {}"
print(txt.format(age))

# slice

a = "Hamza"

print(a[0])
print(a[0:-1])
print(a[2:])
print(a[:2])

# split

a = "Mhammad Hamza"
print(a.split(" "))

# upper
a = "Mhammad \\Hamza\\"
print(a.upper())
print(a.lower())
print(a.replace(" ", "_"))

