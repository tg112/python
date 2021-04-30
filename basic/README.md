# Basic

## Integers, Floats, Lists, Dictionaries, Tuples, dir, help

`Integers` are for representing whole numbers:

```
rank = 10
eggs = 12
people = 3
```

`Floats` represent continuous values:

```
temperature = 10.2
rainfall = 5.98
elevation = 1031.88
```

`Strings` represent any text:

```
message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
```

`Lists` represent arrays of values that may change during the course of the program:

```
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
```

`Dictionaries` represent pairs of keys and values:

```
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
```

Keys of a dictionary can be extracted with: `phone_numbers.keys()`  
Values of a dictionary can be extracted with: `phone_numbers.values()`

`Tuples` represent arrays of values that are not to be changed during the course of the program:

```
vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

To find out what attributes a type has:

```
dir(str)
dir(list)
dir(dict)
```

To find out what Python builtin functions there are: `dir(__builtins__)`

Documentation for a Python command can be found with:

```
help(str)
help(str.replace)
help(dict.values)
```

From tuple to list:

```
data = (1, 2, 3)
list(data) # [1, 2, 3]
```

From list to tuple:

```
data = [1, 2, 3]
tuple(data) # (1, 2, 3)
```

From list to dictionary:

```
data = [["name", "John"], ["surname", "smith"]]
dict(data) # {'name': 'John', 'surname': 'smith'}
```

## Positive/Negative Indexes, Slicing

Lists, strings, and tuples have `a positive index` system:

```
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
```

And `a negative index` system:

```
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
```

In a list, the 2nd, 3rd, and 4th items can be accessed with:

```
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']
```

First three items of a list:

```
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed']
```

Last three items of a list:

```
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
```

Everything but the last:

```
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1]
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
```

Everything but the last two:

```
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2]
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
```

A single in a dictionary can be accessed using its key:

```
phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'
```

## Functions and Conditionals

Define a `function:`

```
def cube_volume(a):
    return a * a * a
```

Write a conditional block:

```
message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")
```

Write a conditional block of multiple conditions:

```
message = "hello there"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
```

Use the and operator to check if both conditions are True at the same time:

```
x = 1
y = 1

if x == 1 and y==1:
    print("Yes")
else:
    print("No")
```

Use the or operator to check if at least one condition is True:

```
x = 1
y = 2

if x == 1 or y==2:
    print("Yes")
else:
    print("No")
```

Check if a value is of a particular type with:

```
isinstance("abc", str)
isinstance([1, 2, 3], list)

or

type("abc") == str
type([1, 2, 3]) == lst
```

Functions can have more than one parameter:

```
def volume(a, b, c):
    return a * b * c
```

Functions can have default parameters (e.g. coefficient):

```
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters

print(converter(10))
```

Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):

```
def volume(a, b, c):
    return a * b * c

print(volume(1, b=2, c=10))
```

An \*args parameter allows the function to be called with an arbitrary number of non-keyword arguments:

```
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
```

An \*\*kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:

```
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)

print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
```

## Processing User Input

A Python program can get user input via the `input` function:

The input function halts the execution of the program and gets text input from the user:

```
name = input("Enter your name: ")
```

The input function converts any input to a string, but you can convert it back to int or float:

```
experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
```

You can format strings with (works both on Python 2 and 3):

```
# ①
name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))

# ②
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
```

## Loops

- List

```
for letter in 'abc':
    print(letter.upper())
```

- Dictionary keys:

```
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
```

- Dictionary values:

```
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
```

- Dictionary items:

```
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
```

- While loops will run as long as a condition is true:

```
while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
```

## List Comprehensions

- A list comprehension is an expression that creates a list by iterating over another container.

- A basic list comprehension:

```
[i*2 for i in [1, 5, 10]]
```

- List comprehension with if condition:

```
[i*2 for i in [1, -2, 10] if i>0]
```

- List comprehension with an if and else condition:

```
[i*2 if i>0 else 0 for i in [1, -2, 10]]
```
