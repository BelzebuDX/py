"""
This is a documment for guided study on python basics

"""
# Para comentar código use "#"

"""
Variables

name = "Pedro"

print(name) 

function(arguments)

Variables' names cannot have space, numbers as first char, and are
case sensitive

media = 0
n1 = n2 = n3 = n4 = 10
print(n1,n2,n3,n4)

name, age = "Pedro" , "19" --> multiple inputs

Data Types:
-String
-Float
-Interger
-Boolean
-Complex
print(type(name)) = Str

Boolean types:

status= True
status1= False

Complex types:
complexnum= 1+2j

To test if a variable is a certain data type:

isinstance(var, datatype) --> Return a Boolean

Inputing variables into another:

a=10
b=2

c= a +b

"""

############################


"""
Operators

+ 
-
*
/
//
% --> the rest of a division
** 

For user input:

a = input("Type a number")

Casting
a = int(a)
a = int(input("Type a number"))

"""
###################

"""
Comparision operators


== --> Equal
!=  --> Different
>  --> Higher
<  --> Lower
>=
<=

input a logical test into a boolean variable

test= a > b
test2 = a != b


"""

"""
Logical Operators

and 
or
not --> reverse the bool value

example:

age = 18
height = 1.75

validação = (age >= 18) and (height >=1.70)


"""

"""
Conditionals

Simple, compound, chained

if (condition):
    execute in case of a true condition

elif (condition): --> in case of a False Condition, only executes
when the first "if" condition failed.
    code
else:
    execute in case of a False condition

    

"""

"""
Print() edits and formating 

print(objects, args)

name= "pedro"

print ('The name is : ', name)

Concat:
print ("Hello, " + nome + " welcome")

No line break
print("text", end="")

.format() function:

name= "pedro"
age= 20

specialstr= "his name is {0} , and he is {1} years old".format(name,age)

fstring:

fstrname= f"Hi ! my name is {name} , and I'm {age} years old "

formating floating numbers:

value= 125.325423

print(f"The value is {valor:.2f}")

Table in strings:

name= "Pedro"
age= 32

print(f"name: {name} \tAge: {age}")


"""


"""
Repetition loops

While loop:

ctrlnum = 1

while (ctrlnum <= 10)
    print(num)
    num += 1

    
var = None --> empty variable

while True:

    if var= "exit":
        break --> finishes any loop


        
For loops:

for item in sequence:
    do

list= [1,2,3,45,56,6,10]

for i in list:
    print(i)

range():

--> range(initial_value, last_value, increment)

for num in range(1,11):
    print(num)

for num in range(10):
    print(num)

for i in range(1,10,1):
    print(i)
    
name= input("Your name is: ")
for i in range (10):
    print(f"{i+1} {name}")

stones= ("ruby", "diamond", "saphire", "coblestone")

for stone in stones:
    if stone == "coblestone":
        continue #-->jumps over this iteration
    print (stone)


"""

"""
Nested Loops:

for count_ext in range(1,10)
    print(f"\n Turn: {count_ext}")
    for count_int in range (5,0,-1):
        print(f"value is: {count_int}")



"""

"""
Random numbers

import random as rd

for a in range(1,6):
    print(f"\n set Nº {a}")
    for b in range(5):
        random_num = rd.randint(1,100)
        print(f"The values is: {random_num}")


value= rd.randint(1,100)


value = rd.random() -->float number between 0 and 1
value = rd.uniform(1,100) --> float number defined
value= round(value * 10, 3)

list= [1,2,4,6,3,7,8,11,33]
n = random.choice(list)
print(f"the chosen number is: {n}")

n2= random.sample(list,3)  --> 3 values from the list

Shuffling:

n = random.shuffle(list)


"""

"""
LISTS(array):

sequence of values

sintax: list_name= [values]

scores = [5,8,10,2,22]

scr_num1 = scores[0] --> scr_num1 == 5

scores2 = [10,45,20,60,78]

all_scores = scores + scores2 --> concat of two lists

scores[-1] --> last value of the list

new value to a list:

scores[0] = 9

slicing:

print(scores[0:4]) --> all values from 0 position to 4
print(scores[-2:]) --> last numbers

the size of the list:

size_scores = len(scores)

Built in functions (sorting,sum, max-min):

sorted_scores = sort(scores, reverse=False)
sum_scores = sum(scores)
min_num_scores= min(scores)
max_num_scores= max(scores)


Appending in a list:

scores.append(101)
scores.pop() --> deletes the last element of the list
scores.pop(3) --> deletes from a specified position
scores.insert(4,70) --> insert an item in a specified position

testing a value in a list:

print(17 in scores) --> returns a boolean if an item is in the list or not


creating empty lists:

list= []
list = list()

iterating through a list:

numbers = [1, 10, 2, 20 ,3 ,30 ,4 ,40]

for number in numbers:
    print(number)

"""

"""
Tuples:
Immutables, all data are acceptable,
repetitions are acceptable

tuple = (2,4,5,6,78)

size_tuple= len(tuple)
print(tuple[2])
print(tuple[-1])

new_tuple= (2,4,5,3,67,34,4,2,5,75,3)

print(new_tuple.count(2)) --> sees how many times an item is in the tuple

Slicing:

print(new_tuple[0:4])
print(new_tuple[-2:])

existence test:

print(2 in new_tuple)


sum(), min(), max() are possible with tuples

functions impossible in tuples:
sort(), append(), reverse(), pop()

Iterating through a tuple:

for number in new_tuple:
    print(f"the number is: {number}")

Creating a list from a tuple:

tuple_list = list(new_tuple)

Creating a tuple from a list:

car_group = ["gol", "golf", "uno", "palio", "santana"]
cars = tuple(car_group)
print(f"the type is: {type(cars)} and the cars are: {cars}")

print(sorted(new_tuple))



"""

"""
Math () &  Built in functions

values = [1,2,5,6,4,6,8,19]
a=2
b-5
c= 2.423423
max(values)--> 19
min(values) --> 1
abs(b) --> 5
pow(a,b) --> 32
round(c,2) --> 2.42

Using math library:

import math

x=8
y=100

square_root= math.sqrt(x)
math.floor()
math.ceil()
print(math.pi)
math.factorial(x)
math.inf + 1 --> infinite

"""

"""
String manipulation:

name= "pedro"

letter2= name[2]
size_name= len(name)
print("the name is " + name)

text1 = "lets learn python today!"
words1 = text1.split()

print("k"*10)

Slicing:

print(text1[3:10])

Finding:

email_call = input("write down your email address")
atsign = email_call.find("@")

user =  email_call[0:atsign]
domain = email_call[atsign+1:]

Validation of substrings:

text1= "let build a red car in our garage"
print("red" in text1)
print("keys" in text1)
print("keys" not in text1)

word1= helicopter
substr_pos= word1.find("cop")

print("12345".isdigit()) -->True
print("12345abc".isdigit()) -->False

Manipulating strings:

str1 = "nonsensE"
str1 = str1.upper()
str1 = str1.lower()
str1 = str1.capitalize()
str1 = str1.title()

Replacing:

car1= "fiat palio"
old_car = car1.replace("palio","elba")

Removing spaces:

text1= "   old cars are great !    "

print(text1.lstrip()) --> left removal
print(text1.rstrip()) --> right removal
print(text1.strip()) --> both sides removal


Justify text:

fruit ="Avocado"
print(fruit)
print(fruit.rjust(20))
print(fruit.ljust(20))
print(fruit.center(20))
print(fruit.center(20,"#"))


first and last char validation:

phrase1 = "Massachussets"
print(phrase1.startswith("M")) --> True
print(phrase1.endswith("t")) --> False

Docstrings:
é literalmente oq eu to usando pra comentar...

"""
"""
"""

"""
Dictionaries or Hash maps

No duplicates, 
key-value storage,
Any data type

person = {
    "name":"Pedro",
    "age": 21,
    "height": 1.78,
    "gender": "male",
    "is_handsome": "hell yeah"
}

print(f"This person name is: {person["name"]}")
print(f"This person age is: {person["age"]}")

print(f"This dictionary has {len(person)} elements")

Updating values:

person["age"]="22"

Inserting new values:

person["weight"] = 80

Deleting values:

del person["is_handsome"]

person.clear() -->empty the dictionary

del person --> desapears from memory

Iterating through a hashmap:

all_items = person.items()
for i in person.items():
    print(i) --> (key,item)

print(person.keys())
for i in person.keys():
    print(i)

print(person.values())
for i in person.values():
    print(i)

for keys, values in person.items():
    print(f"{keys}: {values}")


"""

"""
Sets(conjuntos)
no duplicates
no order
mutable
any data types
follow matematical properties of sets

dwarf_planets = {"pluto", "ceres", "eris", "haumea"}
for little_planet in dwarf_planets:
    print(little_planet)

    
num_list= [1, 2, 3, 5, 4, 2]
num_set= set(num_list)

Comparison between sets:

num_set1 = {1,2,3,4,5,6}
num_set2 = {1,2,3,4,5,10}

print(num_set1 == num_set2) --> false
print(num_set1 != num_set2) --> true

print(num_set1 | num_set2) --> {1,2,3,4,5,6,10}
print(num_set1.union(num_set2)) --> {1,2,3,4,5,6,10}

print(num_set1 & num_set2) --> {1,2,3,4,5}
print(num_set1.intersection(num_set2))

print(num_set1 ^ num_set2) --> {6,10}
print(num_set1.symmetric_difference(num_set2)) --> {6,10}

Adding new items:

num_set1.add(7)
num_set1.remove(1) or num_set.discard(1)

num_set1.pop() -->removes a random item

num_set1.clear()


"""

"""
Functions
*Modularization, code reusing
*Readability

def <function_name> ([args]):
    <code>

def message():
    print("Hello World ! ")

message() --> no args needed

def sum_func(a,b):
    print(a+b)

sum_func(1,10) --> 11

Returning a value:

def mult(x,y):
    return x *y

a = 5
b = 8
c = mult(a,b)
print(f"the product of {a} and {b} is: {c}")


def division_func (k,j):
    if j != 0:
        return k /j
    else:
        return "0 division is not possible in this universe"

if __name__ == "__main__":
    a = int(input("type a number"))
    b = int(input("type other number"))
    res = division_func(a,b)

    print (f"{a} divided by {b} is: {res} ")

Using a list as a parameter 

def power_2 (list_a):
    squares= []
    for i in list_a:
        squares.append(i**2)
    return squares        

Optional arguments:

def count_num(num=12, letter="#")
    for i in range(1,num):
        print(letter)

count_num()
count_num(letter="&")
count_num(num=2)
count_num(4,"%")

the order for parameters are (required,optional):
def count(letter, num=10):

def sum_mult(a, b, c=0):
    if c==o:
        return a * b
    else:
        return a + b + c

print(sum_mult(2,3)) --> 6 (2*3)
print(sum_mult(2,3,1)) --> 5 (2+3+1)

Global or local variables, visibility:

Local: only exists inside a function

Global: accessable for each script block

#EXAMPLE:

global_var = "abcdef"
def show_text():
    local_var = "tiger running"
    print(f"Global variable: {global_var}")
    print(f"Local variable: {local_var}")

show_text()
print(f"Global variable: {global_var}")
print(f"Local variable: {local_var}") --> not defined

Accessing and changing a global variable inside a function:

global_var = "abcdef"
def show_text():
    global global_var
    global_var = "fedcba"
    local_var = "tiger running"
    print(f"Global variable: {global_var}")
    print(f"Local variable: {local_var}")


"""

"""
Error exception:
#object that represents an error during the code execution

try...except
##################
num1 = int(input("Type a number for division))
num2 = int(input("Type other number for division))

try:   
    res = num1 / num2
except ZeroDivisionError:
    print("0 is not a possible divisor, please provide other number")
    num2 = int(input("Type other number for division))
else:
    print(f"The result is {res}")

##################
res = 0
num1 = int(input("Type a number for division: "))
num2 = int(input("Type other number for division: "))

try:
    res = num1 / num2
except ZeroDivisionError:
    print("0 is not a possible divisor, please provide other number")
    num2 = int(input("Type other number for division: "))
    res = num1 / num2
    print(f"The result is {res}")
else:
    print(f"The result is {res}")


def division_nums(k,j):
    return k / j

if __name__ == "__main__":
    while True:
        try:
            num1 = int(input("Type a number for division: "))
            num2 = int(input("Type other number for division: "))
            break
        except ValueError:
            print("Please type interger numbers")
    try:
        res = division_nums(num1, num2)
    except ZeroDivisionError:
        print("0 is not a possible divisor, please provide other number")
    except:
        print(f"One error has happened")
    else:
        print(f"result of division is: {res}")
    finally:
        print("The end")

raise exceptions:

try:
    positive_num = int(input("Type a positive number: "))
    if positive_num < 0:
        raise ArithmeticError
except ArithmeticError:
        print("This number is negative !")
else:
    print(f"The number squared is: {positive_num**2} ")
finally:
    print("The end of the script, bye !!")

    
Creating specific exceptions:

Class NegativeNumberProvidedError(Exception):
    def __init__(self):
        pass

try:
    positive_num = int(input("Type a positive number: "))
    if positive_num < 0:
        raise NegativeNumberProvidedError
except NegativeNumberProvidedError:
        print("This number is negative !")
else:
    print(f"The number squared is: {positive_num**2} ")
finally:
    print("The end of the script, bye !!")


"""

