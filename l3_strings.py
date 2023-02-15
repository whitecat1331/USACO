# String Intro
print("String Intro")
print(
    "A String in python and in most programming languages is going to be stored in memory as a series or 'string' of characters"
)

print(
    "We can represent a string in python by using either 'single quotation' or \"double quotation marks.\""
)

# String Example
print("\nString Examples")
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
print("\nEscaping Strings")
escaping_prompt = """As stated before, a single or double quote can be used to create a string. It is up to personal preference on which is used, 
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

# Escaping Characters
print("\nEscaping Characters")
print("The backlash is a special character called an escape character.")
print(
    "The backslah is used to escape the character meaning and give it extra functionality within the string."
)
print(
    "Some escape characters will also stop the functionality that a special character might already have and treat it as a normal printable string character"
)
print(
    "The backslash is already a special character, you need to escape the first backslash to print one backslash"
)
# uncomment next line
# print("This is a backlash: \")
print(
    "This will result in an error since python thinks we are trying to escape the double quotation mark"
)
print("This is a backslash: \\")
print("Not all characters can be escaped for extra functionality.")
print("Some of the most common escape characters are: ")
print("'\\n' - newline \ncharacter")
print("'\\t' - tab \t character")
print(
    "'\\' - backslash created by escaping the escape character and make it function normally"
)
print("'\\\"' - print a double quote in a string literal defined with double quotes")
print('\'\\\'\' - print a single quote in a string literal defined with single quotes')
print("In the previous example, the single quote, backslash, and next two single quotes are escaped")

# String Repetition
print("\nString Repetition")
print(
    "Strings can also easily be copied by multiplying the string by the integer number of copies\n"
    * 3
)

print("In python, there are multiple ways to print and format strings in your program")


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
print("\nString Concatenation")
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
print("\nString Interpolation")
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

# f-Strings
print("\n f-strings")
print("Format strings, or f'' strings are a special type of string recently added to python")
print("f-strings use curly brace to run an expression in the strings to format it. For example: ")
thanos = "Thanos"
witch = "The Scarlet Witch"
doom = "Doctor Doom"
print(f"Some of the villians in advengers include: {doom}, {thanos}, {witch}")
print("Which formatting method you use with strings is ultimately up to personal preferece")

# Reviewing arrays or lists
print("\nIntro to lists")
print("A list is simply a named container, much like a variable, that can hold multiple values")
villian_advengers = [thanos, witch, doom, "Loki"]
print(f"The values of the list is: {villian_advengers}")
print("To index into an individual item in a list, use index notation or []")
print("Arrays start counting their index position at index zero (0)")
print(f"The first villian in the array is {villian_advengers[0]}")
print(f"The second item in the array is: {villian_advengers[1]}")
print("To print from the last item of an array, use a negative index")
print(f"The last item in the array is: {villian_advengers[-1]}")
print(f"The second to last item in the array is: {villian_advengers[-2]}")
print("List slicing allows the user to copy parts of the list")
print("Slice syntax is list[start:end] where start is the beginning index and end is the last index (exclusive)")
print(f"The second and third value of villian_advengers is: {villian_advengers[1:3]}")
print("To copy from the start index to the end of the of the list use the syntax: list[start:]")
print(f"The items after the first item are: {villian_advengers[1:]}")
print("The syntax to copy from the start of the list to the ending index is: list[:end]")
print(f"The first three items in the list are: {villian_advengers[:3]}")

# Strings as arrays or lists
print("\nStrings as lists")
print("A string is technically a linked-list of characters saved in your program")
print("A linked-list can be though of as an array or a list")
print("In other words, the String data type is an array or 'string' of linked characters")
print("Knowing that Strings funcationally work the same as array, you can use array syntax to work with substrings")
print("A substring is simply a small sub-section of a larger string. For example: ")
main_string = "Hello, World!"
list_representation_of_main_string = ['H','e','l','l','o',' ','W','o','r','l','d','!' ]
print(f"the variables main_string: {main_string} and list_representation_of_main_string: {list_representation_of_main_string} are practically identical")
print("Arrays and Strings both start counting their index position at index zero (0)")
print("This means the first character in any string will always be at index 0")
print("Each character or element after that will have an incremental index")
print("Use index notation to print an individual character")
print("The first letter in {} is: ".format(main_string) + main_string[0])
print("In the previous print statement, both string interpolation and concatenation is used for formatting.")
print("Another just as viable solution would be... ")
print(f"The first letter in {main_string} is: {main_string[0]}")
print(f"The second letter in {main_string} is: {main_string[1]}")
print(f"The last word in main_string is {main_string[7:]}")
print(f"The first word in main_string is: {main_string[:7]}")

# Comparing String
print("You can use any comparision operator with strings")
s1 = "Hello"
s2 = "Hello"
s3 = "World"
print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")
print("The == and != operators will compare to see if the strings are exactly equal or not equal.")
print(f"s1 == s2: {s1 == s2}")
print(f"s1 == s2: {s2 == s3}")
print(f"s1 != s2: {s1 != s3}")
print(f"s1 == s2: {s2 != s3}")
print("The <, <=, >, >= operators are used to compare based on alphabetical order")
print(f"s1 < s2: {s1 < s2}")
print(f"s1 < s3: {s1 < s3}")
print(f"s1 > s2: {s1 > s2}")
print(f"s1 > s3: {s1 > s3}")
