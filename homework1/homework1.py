#the start of homework 1
# --- Variable and Data Types ---
# - Variables -
a=10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b=1.5
print(b)
print(type(b)) # b is a floating-point number, or a float, a number with a decimal place

c=3j
print(c)
print(type(c)) # c is a complex number, made of a real and imaginary part

d="hello"
print("hello")
print(type(d)) # d is a string, a sequence of characters

e = [1,2,3]
print(e)
print(type(e)) # e is a list, a mutable sequence of objects that can be of any type

f={"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, made to store key:value pairs

g=(1,2)
print(g)
print(type(g)) # g is a tuple, an immutable squence of objects that can be of any type

h=["apple", "banna", "strawberry"]
print(h)
print(type(h)) # h is a list, this one a sequence of strings

i=True
print(i)
print(type(i)) # i is a boolean, made to represent the truth value of an expression

j=None
print(j)
print(type(j)) # j is a nonetype, or null, an absent value

k=[True, "blue", 12]
print(k)
print(type(k)) # k is a list, this one holding a sequence of different objects

l=str(14)
print(l)
print(type(l)) # l is a string, this one listing numerical characters

m=1e4
print(m)
print(type(m)) # m is a float, as it has a decimal place

# - Questions -
# I found nine different data types.
# All the data types I found are: integer, float, complex number, string, list, dictionary, tuple, boolean, and nonetype.
# The variables that have the same data types are as listed: "b and m", "d and l", and "e, h, and k".
# The data type of "l" was a string. It's not an integer because of the command "str()", which converts the value into a string.

n = b"Food"
print(n)
print(type(n)) # n is a bytes, made to represent and manipulate immutable sequences of bytes

# --- Booleans ---
# - Expressions -
print(10>9) # true, 10 is greater than nine
print(10==9) # false, 10 is not equal to nine
print(10<=9) # false, 10 is not less than or equal to nine
print(bool("abc")) # true, "abc" is true
print(bool(123)) # true, "123" is true
print(bool(["apple", "cherry", "banana"])) # true, the sequence of objects is true
print(bool(True)) # true, the value is true
print(bool(False)) # false, the value is false
print(bool(0)) # false, the value "0" is false
print(bool("")) # false, the empty value is false
print(bool(" ")) # true, the value of " " is true
print(bool(())) # false, the empty value is false
print(bool([])) # false, the empty value is false
print(bool({})) # false, the empty value is false
print(bool(True and False)) # false, the value cannot be true and false
print(bool(True and True)) # true, the values are both true
print(bool(False and False)) # false, the values are both false
print(bool(True or False)) # true, the value can be either true or false
print(bool(True or True)) # true, the values are both true
print(bool(False or False)) # false, the values are both false
print(bool(not(False))) # true, the value isn't false, so therefore it is true
print(bool(not(True))) # false, the value isn't true, so therefore it is false

# - Questions -
# Expressions reutrning true tend to have something of value within the parameters or are stated to be true. Meanwhile, expressions returning false either have nothing inside them, are contradictions, or simply are stated to be false.
# I was surprised by the result of print(bool(" ")) because I would've expected it to be false, but because of the value of the space, it is true.

print(bool("The Glembays")) # This object is true because it has a value. 
print(4>10) # This object is false because four is not greater than 10.

# --- Operators ---
# - Arithmetic Operators -
print(10+5) # 15, + performs addition
print(10-5) # 5, - performs subtraction
print(2*4) # 8, * performs multiplication
print(6/3) # 2.0, / performs division
print(5%2) # 1, % performs division and gives remainder
print(3**2) # 9, ** performs exponential
print(15//2) #7, // performs floor division and returns greatest integer

# - Comparison Operators -
print(5==2) # false, == performs equal comparison
print(10!=10) # false, != performs unequal comparison
print(2<5) # true, < performs less than check
print(12>5) # true, > performs greater than check
print(5<=6) # true, <= performs less than or equal to check
print(1>=10) # false, >= performs greater than or equal to check

# - Assignments Operators -
x=5
x+=5
print(x) # 10, the right-hand value is added to the left-hand value

x=5
x-=4
print(x) # 1, the right-hand value is subtracted from the left-hand value

x=5
x*=3
print(x) # 15, the right-hand value is multipled to the left-hand value

# - Logical Operators -
# The operator "and" combines conditional statements and returns true if both are true.
print(1<9 and 4<16) # true, one is less than nine and four is less than 16.
print(0==10 and 10==10) # false, 0 is not equal to 10 and 10 is equal to 10.

# The operator "or" combines conditional statements and returns true if one is true.
x=10
print(x>9 or x<4) # true, x is greater than nine but x is not less than four
print(x==1 or x<0.3) # false, x is not equal to 1 and x is not less than 0.3

#The operator "not" combines conditional statements and reverses the result, returning false with a true result.
x=3
x/=9
print(not(x is int)) # true, x is not an integer
print(not(x==1/3)) # false, x is equal to 1/3

# - More Questions -
# "/" is the command referring to division while "//" refers to floor division. The former gets the exact value while the latter gets the greatest integer.
# "%" is the module operator while "//" refers to floor division. The former calculates the remainder of the objects while the latter gets the greatest integer.
# When dividing two numbers, you'd use "%" to get the remainder. Example:
print(10%4) # The command returns "2", which is the remainder of 10/4.
# Assignment operators work by taking the right-hand value and applying the effects of the operator onto the left-hand value.

# --- Strings ---
# - Mutations -
my_string="hello"
print(my_string) # Prints: hello

my_string[0]
print(my_string[0]) # Prints: h

my_string[1]
print(my_string[1]) # Prints: e

my_string[2]
print(my_string[2]) # Prints: l

my_string[3]
print(my_string[3]) # Prints: l

my_string[4]
print(my_string[4]) # Prints: o

my_string[-1]
print(my_string[-1]) # Prints: o

my_string[1:3]
print(my_string[1:3]) # Prints: el

my_string[0:5:2]
print(my_string[0:5:2]) # Prints: hlo

print(len(my_string)) # Prints: 5

my_string="goodbye"
print(my_string) # Prints: goodbye

print(7*my_string) # Prints: goodbye seven times

# - Questions -
# The term "slicing" refers to a command that returns a range of characters, beginning from a certain position and not including the end position. I sliced my string in the manipulations containing a colon.

name="Oski"
print("Hello, my name is", name) # Prints: Hello, my name is Oski

name="Oski"
print(f"Hello, my name is {name}") # Prints: Hello, my name is Oski

#The difference between the last two print statements is that the second one is a f-string, which allows the variable to be directly embedded within the string using curly brackets. Meanwhile, the first is a print string, which requires the variable to be separate from the string.

# --- Terminal Commands ---
# - Commands -
# cd
# Changes directories, use it to move from one folder to another
# Example: cd Desktop

# ls
# List directory, tells you the contents of the current directory
# Example: ls Library

# ls -a
# List directory, including hidden contents, which are marked by a "." at the front.
# Example: cd Public --> ls -a

# mkdir
# Make directory, literally creates a directory
# Example: mkdir Elk

# cat
# Concatenate, isplays a file's contents, can also be used to combine and create new files
# Example: cat test.py

# pwd
# Print working directory, lists the path to the working directory
# Example: cd Music --> pwd

# cd ..
# Changes to parent directory
# Example: cd Pictures --> cd ..

# cd .
# Changes to current directory
# Example: cd Desktop --> cd .

# cd ~
# Changes to home directory
# Example: cd Movies --> cd ~

# cp
# Copy file, duplicates files or directories from one location to another
# Example: cp Knight.txt Chovy.txt

# mv
# Move, can move or rename files and directories
# Example: mv Zeus.txt HLE.txt

# rm
# Remove, removes objects, including files and directories
# Example: rm Peter.py

# clear
# Clear, clears the terminal
# Example: clear

# grep
# Global regular expression print, searches for certain words, phrases, or patterns inside text files and displays matching results
# Example: grep "Meteor" vlr.txt

# - Questions -
# date
# Date, displays the current date and time
# Simply type in "date" in terminal and the information above should appear.

# whoami
# Who am I, displays the current user that is logged in
# Type "whoami" in terminal and it will display the user that is currently logged in.

# man
# Manual, used right before a command to generate a manual of how to use that command
# Type "man", followed by the command. For example, "man ls" will generate a manual on how to use "ls".

# The difference between "ls" and "ls -a" is that the latter additionally reveals hidden files.
# A hidden file is a file that is excluded from the main directory unless it is specifically requested.

# ls -r
# Lists contents in reverse order
# Type "ls -r" into the command line to display contents of current directory in reverse order.

# ls -l
# Also known as long listing, lists contents with additional info, such as permissions
# Type "ls -l" into the command line to display a long list of contents in the current directory.

# rm -rf
# Removes a directory and its contents
# Type "rm -rf [file name]" in the command line to remove everything inside a directory, including the directory itself.