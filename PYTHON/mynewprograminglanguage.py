📖 My New Programming Language (MNPL) Tutorial

Welcome to My New Programming Language (MNPL)! Instead of writing confusing code, you write code like you're telling a story in your diary.

1. Starting a Program

Every program begins with:

dear diary i'm hello.py

This tells the compiler the name of the Python file to create.

2. Comments

Anything starting with # is ignored.

# this is a comment
# comments are just for you
3. Printing

To print text:

tell the computer Hello World!

Output:

Hello World!
4. Variables

Ask the computer for input.

ask the computer 'What is your name?' for name

Python:

name = input("What is your name?")
5. Functions

Create a function.

marks function - invited; friend1 and friend2

This becomes

def marks(friend1, friend2):

Example:

marks function - invited; x and y
    tell the computer Welcome!
6. Calling Functions

To call a function:

tell the computer welcome to marks function: Bob and Alice

Python:

marks("Bob", "Alice")
7. If Statements
Bigger Than
if apples is bigger than bananas then

↓

if apples > bananas:
Smaller Than
if apples is smaller than bananas then

↓

if apples < bananas:
Equal
if apples is the same as bananas then

↓

if apples == bananas:
8. Maths
Addition
tell the computer make x and y highfive

↓

print(x + y)
Subtraction
tell the computer make x and y leave

↓

print(x - y)
Multiplication
make x and y hug

↓

x * y
Division
make x and y share

↓

x / y
9. Example Program
dear diary i'm maths.py

ask the computer 'First number?' for x
ask the computer 'Second number?' for y

tell the computer make x and y highfive
tell the computer make x and y leave
make x and y hug
make x and y share

Compiles to

x = input("First number?")
y = input("Second number?")

print(x + y)
print(x - y)

x * y
x / y
10. Complete Example
dear diary i'm marks.py

# Ask for marks
ask the computer 'Maths mark?' for maths
ask the computer 'English mark?' for english

# Create a function
average function - invited; maths and english
    if maths is bigger than english then
        tell the computer Maths wins!

tell the computer welcome to average function: maths and english
11. Language Rules
Every program starts with dear diary.
Use four spaces to indent inside functions and if statements.
Comments start with #.
Functions are introduced with function - invited;.
Use tell the computer whenever you want to print something.
Use ask the computer whenever you want user input.
12. Planned Features 🚧

These aren't in the compiler yet, but you could add them:

MNPL	Python
remember score is 10	score = 10
otherwise	else:
keep trying while x is bigger than 0	while x > 0:
repeat 5 times	for _ in range(5):
go home	break
keep going	continue
the end	Dedent one indentation level
Your First MNPL Program
dear diary i'm first.py

ask the computer 'What is your name?' for name

tell the computer Hello!

tell the computer make 5 and 10 highfive

Congratulations! You've written your first program in My New Programming Language. 🎉

As you expand the compiler, you can add more diary-style commands and grow MNPL into a complete toy programming language.