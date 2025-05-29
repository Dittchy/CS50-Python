#First Code
print("First code.")
print("Hello, World")

#Second Code
print("\nSecond code.")
name = input("What's your name?\n")
print("Hello,", name)
#Another way fo writing this
print("Hello, " + name) # no coma between the argument under "" and the variable name.

#Third Code
'''
print(*objects, sep = ' ', end = '\n', file = sys.stdout, flush = False) 
This is the code behind the print function
'''
print("\nThird code.")
print("hello, ", end ="")
print(name)

#Fourth Code

'''
Using the f string and keeping the variable in curly brackets.
'''
print("\nFouth code.")
print(f"Hello, {name}")

#Fifth Code
'''
1. Removing whitespaces from the string
2. Capitalizing the very first letter
3. Capitalize the user's names first words
'''
print("\nFifth code.")
name = name.strip() #Removing the whitespace 

#printing the hello world
print(f"hello, {name}")

name = name.capitalize()#Capitalizes the very first letter

#printing the name 
print(f"\n{name}")

name = name.title()#Capitalizing the first letters of the words in the user's name

print(f"{name}")





