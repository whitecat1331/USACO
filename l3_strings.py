print(
    "A String in python and in most programming languages is going to be saved as a series or 'string' of characters"
)

print("Strings in python typically represent just plain text. For example: ")
first_name = "Bruce"
last_name = "Banner"

print(
    "Python is an excellent programming language when it comes to easily manipulating strings."
)
escaping_prompt = """We can represent a string in python by using either 'single quotation' or \"double quotation marks.\"
It is up to personal preference on which is used, however my preferece is to use double quotes for the main string
Whichever you use, it is important to stay consistent, exspecially when trying to 'nest' strings.
From the source code, you can see to print out a double quotation mark, a backslash was needed
This is because I am using double quotation marks to represent the opening and closing of my string
This also means if a loose quotation mark is placed in the string to try to print out the double quote,
the Python interpreter will think that the quotation mark is ending the first string and everythhing to the right of the
ended string will be interpreted")"""
# Example of using only a double quote in string

# uncomment this line and run the example
# print("This is a quotation mark ("), it is used to represent a string in python")
# this error, or something similar will be printed when the program is run
quotation_error = """
  File "/home/patrickloyd/work/USACO/l3_strings.py", line 13
    print("This is a quotation mark ("), it is used to represent a string in python") 
                                                                                   ^
SyntaxError: unterminated string literal (detected at line 13)
"""
print("")
