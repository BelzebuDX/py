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
