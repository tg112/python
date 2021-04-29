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
