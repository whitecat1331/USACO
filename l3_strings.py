# String Intro
print(
    "A String in python and in most programming languages is going to be stored in memory as a series or 'string' of characters"
)

print(
    "We can represent a string in python by using either 'single quotation' or \"double quotation marks.\""
)

# String Example
print("Strings in python typically represent just plain text. For Example: ")
first_name = "Bruce"
last_name = "Banner"
print("first_name: ")
print(first_name)
print("last_name: ")
print(last_name)

multi_line_string = """Strings can also span multiple lines by using:
'''triple single quotes'''
or 
\"\"\"triple double quotes\"\"\"
"""
print(multi_line_string)

# Escaping Strings
escaping_prompt = """
As stated before, a single or double quote can be used to create a string. It is up to personal preference on which is used, 
however my preferece is to use double quotes for the main string
Whichever you use, it is important to stay consistent, exspecially when trying to 'nest' strings.
From the source code, you can see to print out a double quotation mark, a backslash was needed
This is because I am using double quotation marks to represent the opening and closing of my string
This also means if a loose double quotation mark is placed in the string to try to print out the double quote,
the Python interpreter will think that the quotation mark is ending the first string and everythhing to the right of the
ended string will try to be interpreted")"""
print(escaping_prompt)
# Example of using only a double quote in string

# uncomment one of the next two line and run the example
# print("This is a quotation mark ("), it is used to represent a string in python")
# print('This is a quotation mark ('), it is used to represent a string in python')
# this error, or something similar will be printed when the program is run
quotation_error = """
  File "/home/patrickloyd/work/USACO/l3_strings.py", line 13
    print("This is a quotation mark ("), it is used to represent a string in python") 
                                                                                   ^
SyntaxError: unterminated string literal (detected at line 13)
"""
print("Running the example, we would expect to see the error: ")
print(quotation_error)
print(
    "The same issue would occur if we switched the double quotes and single quotes in the previous example"
)
print(
    "One practice to avoid this issue is to use double quotes as your main String literal and then using single quotes to represent a nested string or to print out a single quote"
)
print(
    "The other method would be to use single quotes as your main string literal and then use double quotes inside the string literal"
)
print(
    "This is an example with double quotes for the main 'string' and single quotes for the inner 'string'."
)
print(
    'This is an example with single quotes for the main "string" and double quotes for the inner "string".'
)


# Printing multiple strings and values
print("You can print multiple values and variables within one print statement.")
print(
    "The value of first_name is:", first_name, "The value of last_name is:", last_name
)
print("Each value in the print statement needs to be separated by a comma.")

print(
    "Python is an excellent programming language when it comes to easily manipulating strings."
)

# String concatenation
print("Concatenation means joining or combining two or more strings.")
print(
    "Concatenation can be used by adding the addition (+) operator between two strings."
)
full_name = first_name + last_name
print("The full name is:", full_name)
print("Notice when we use commas to print multiple values, a space was added for us.")
print("Concatenation is going to literally join the two strings so no space is added.")
print("One solution could be to concatenate a space between the two variables.")
full_name = first_name + " " + last_name
print("The full name is:", full_name)
print(
    "You can also concatenate everything you want to say into one variable and print that out."
)
concatenation_prompt = "The full_name is: " + full_name
print(concatenation_prompt)

# String Interpolation
print("Concatenation is one way to format strings based on the value of a variable.")
print("Python also allows for strings to be formatted by other methods.")
print("String Interpolation lets you use the format() method with a place holder {}")
print(
    "Some of the advengers includes: {}, {}, and {}".format(
        full_name, "Thor", "Spider-Man"
    )
)
print(
    "Using String Interpolation, you are able to add a placeholder or curly braces to the string."
)
print(
    "The format function can later be used to pass as many values as there are placeholders to that new string"
)

print(
    "Remembering the order of a large amount of placeholders can be tedious, so python allow you to name placehodlers as well"
)
print("You can the pass a keyword argument to set the value of that named placeholder")
print(
    "A few villians to the advengers are: {Thanos}, {Doom}, {Witch}".format(
        Thanos="Thanos", Witch="The Scarlet Witch", Doom="Doctor Doom"
    )
)
print(
    "Keyword arguments allow you to pass values to a function specific to the parameter or variable name even if it is passed out of order"
)
