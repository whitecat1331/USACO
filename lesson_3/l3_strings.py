import sys

# String Intro
sys.stdout.write("String Intro\n")
string_intro_prompt = """A String in python and in most programming languages is going to be stored in memory as a series or 'string' of single characters.
We can represent a string on a single line in python by using either a 'single quotation' mark or a \"double quotation mark.
A large string can also be defined over multiple lines be using either '''triple single quotationmarks''' or \"\"\"trible double quotation marks\"\"\"\n\n"""
sys.stdout.write(string_intro_prompt)

# Printing  String
sys.stdout.write("Printing Strings: ")
print_string_prompt = (
    "Strings should be printed using the sys library Ex. 'sys.stdout.write(String)'\n\n"
)
sys.stdout.write(print_string_prompt)

# Ascii Chart
# A formatted table can be found within the lesson slides
sys.stdout.write("Ascii chart")
possible_characters = 128  # There are only 128 bits allocated for the Ascii chart
ascii_prompt = ""
for i in range(possible_characters):
    ascii_prompt += f"The Ascii value for {i} is {chr(i)}\n"
ascii_prompt += "Depending on your terminal, The full output for this table might not display all characters\n\n"
sys.stdout.write(ascii_prompt)


# Add Newlines
sys.stdout.write("Add Newlines\n")
add_newlines_prompt = """Notice in the last example, no newline was added after 'Printing Strings'. 
'sys.stdout.write()' does not add a new line at the end of the print stream.
A newline character can be added at the end using '\\n'.
Another alternative is to use multi-line strings as the return character will be printed as a newline

"""
sys.stdout.write(add_newlines_prompt)

# String Examples
sys.stdout.write(
    "String Examples\nStrings in python typically represent any plain text. For Example:\n"
)
first_name = "Bruce"
address = "1234 This Does Not Exist Ln."
email = "randomemail@randomaddress.com"
sys.stdout.write("first_name: ")
sys.stdout.write(first_name)
sys.stdout.write("\n")
sys.stdout.write("address")
sys.stdout.write(address)
sys.stdout.write("email: ")
sys.stdout.write(email)
sys.stdout.write("\n\n")

# Escaping Strings
sys.stdout.write("Escaping Strings\n")
escaping_prompt = """As stated before, a single or double quote can be used to create a string. It is up to personal preference on which is used, 
however my preferece is to use double quotes for the main string.
Whichever you use, it is important to stay consistent, exspecially when trying to 'nest' strings.
From the source code, you can see to print out a double quotation mark, a backslash was needed
This is because I am using double quotation marks to represent the opening and closing of my string
This also means if a loose double quotation mark is placed in the string to try to print out the double quote,
the Python interpreter will think that the quotation mark is ending the first string and everythhing to the right of the
ended string will try to be interpreted")\n"""
sys.stdout.write(escaping_prompt)

# Example of using only a double quote in string
# uncomment one of the next two line and run the example
# sys.stdout.write("This is a quotation mark ("), it is used to represent a string in python")
# sys.stdout.write('This is a quotation mark ('), it is used to represent a string in python')

# this error, or something similar will be printed when the program is run
quotation_error = """
Running the next example, we would expect to see this error or something similar: 
Running Line: sys.stdout.write("This is a quotation mark ("), it is used to represent a string in python")

Output:

  File "/home/patrickloyd/work/USACO/l3_strings.py", line 13
    sys.stdout.write("This is a quotation mark ("), it is used to represent a string in python") 
                                                                                   ^
SyntaxError: unterminated string literal (detected at line 13)
"""
sys.stdout.write(quotation_error)

# Resolving Quotation Error
sys.stdout.write("Resolving Quotation Errors\n")
resolving_quotation_error = """The same issue would occur if we switched the double quotes and single quotes in the previous example
One practice to avoid this issue is to use double quotes as your main String literal and then using single quotes to represent a nested string or to print out a single quote
The other method would be to use single quotes as your main string literal and then use double quotes inside the string literal.\n"""
sys.stdout.write(resolving_quotation_error)
sys.stdout.write(
    "This is an example with double quotes for the main 'string' and single quotes for the inner 'string'.\n"
)
sys.stdout.write(
    'This is an example with single quotes for the main "string" and double quotes for the inner "string".\n\n'
)

# Special Characters
sys.stdout.write("Special Characters:\n")
python_special_characters = """It is always important to remeber some of the most common special characters to use them effectively and without any issues.
Characters in python that already have special functionality:
" - used to open or close a single line string
' - used to open or close a single line string
\"\"\" - used to open or close a multi-line string
''' - used to open or close a multi-line string
\\ - escapes the functionality of the character to the right\n\n"""
sys.stdout.write(python_special_characters)

# Escaping Characters
# Uncomment next line for example
# sys.stdout.write("'\' - print a backslash)
# This will result in an error since python thinks we are trying to escape the double quotation mark
sys.stdout.write("Escaping Characters:\n")
escaping_characters_prompt = """Sometimes you will still need to print the same type of quotation mark within a string defined with that same type of mark.
The backslash is a special character called an escape character.
The backslash is used to escape original characters meaning and give it extra functionality within the string.
Some escape characters, such as the single and double quotation marks,
will also stop original functionality that a character might already have and treat it as a normal printable string character.\n\n
Run Line: sys.stdout.write("'\\' - print a backslash")
This will result in an error since python thinks we are trying to escape the double quotation mark
Not all characters can be escaped for extra functionality
Some of the most common escape characters are:
'\\' - backslash created by escaping the escape character and make it function normally
'\\n' - newline \ncharacter
'\\t' - tab \t character\n"""
sys.stdout.write(escaping_characters_prompt)

# LunarVim Formatter will not stop changing the next two examples, be sure to uncomment before merging to master
# sys.stdout.write("'\\\"' - print a double quote in a string literal defined with double quotes")
# sys.stdout.write('\'\\\'\' - print a single quote in a string literal defined with single quotes\n')

# String Repetition
sys.stdout.write("String Repetition\n")
sys.stdout.write(
    "Strings can also easily be copied by multiplying the string by the integer number of copies\n"
    * 3
)

# String Formatting
sys.stdout.write(
    """\nFormatting strings\nThere are also multiple methods for dynamically formatinng a string based on a variable
Which method you chose is ultimately up to personal preferece.\n\n"""
)

# String concatenation
sys.stdout.write("Method 1: String Concatenation\n")
first_name = "Peter"
last_name = "Parker"
string_concatenation_prompt = """Concatenation means joining or combining two or more strings.
Concatenation can be used by adding the addition (+) operator between two strings.
String variables can also be concatenated with a string to format the string.
The first example concatenates this prompt with the first and last name added to the end.
The second example concatenates this prompt with the first and last name with a formatted space between.
The last example concatenates this prompt with the string 'The full_name is: ' and the full name.
Examples:\n"""

string_concatenation_prompt = (
    string_concatenation_prompt + first_name + last_name + "\n"
)
string_concatenation_prompt += first_name + " " + last_name + "\n"
full_name = first_name + " " + last_name
string_concatenation_prompt += "The full_name is: " + full_name + "\n\n"
sys.stdout.write(string_concatenation_prompt)

# Concatenation with non-String types
# Uncomment next line to cause error
# sys.stdout.write("This will attempt to concatenate a string with an int: " + 100)
sys.stdout.write("Concatenation with non-String types\n")
non_string_concatenation_prompt = """Python only knows how to concatenate two strings.
Anything other than a string will need to be converted to the string data type, or simply a string representation of that type.
Attempting to concatenate a String and a Non-String type will result in an error.

Running the Line: sys.stdout.write("This will attempt to concatenate a string with an int: " + 100) 
Will produce the Error:
Traceback (most recent call last):
  File "/home/patrickloyd/work/USACO/l3_strings.py", line 154, in <module>
    sys.stdout.write("This will attempt to concatenate a string with an int: " + 100)
TypeError: can only concatenate str (not "int") to str

Solution:
Any "primtive" data type in python can easily be converted to a string using the str() function\n
Example:\n"""
non_string_concatenation_prompt += "Concat an integer: " + str(100) + "\n"
non_string_concatenation_prompt += "Concat a double: " + str(3.14) + "\n"
non_string_concatenation_prompt += "Concat a boolean: " + str(True) + "\n\n"
sys.stdout.write(non_string_concatenation_prompt)


# String Interpolation
sys.stdout.write("Method 2: String Interpolation\n")
string_interpolation_prompt = """Concatenation is one way to format strings based on the value of a variable.
Python also allows for strings to be formatted by other methods.
String Interpolation lets you use the format() method with a place holder {} for any value.
Example:\n"""
string_interpolation_prompt += "Some of the advengers includes: {}, {}, and {}".format(
    full_name, "Thor", "Spider-Man"
)
string_interpolation_prompt += """Using String Interpolation, you are able to add a placeholder or curly braces to the string.
    "The format function can later be used to pass as many values as there are placeholders to that new string
    Remembering the order of a large amount of placeholders can be tedious, so python allow you to name placehodlers as well
You can create a keyword argument by naming the placeholder {named_placeholder}.
Keyword arguments allow you to pass values to a function specific to the parameter or variable name even if it is passed out of order.
Example:\n"""
string_interpolation_prompt += (
    "A few villians to the advengers are: {Thanos}, {Doom}, {Witch}\n\n".format(
        Thanos="Thanos", Witch="The Scarlet Witch", Doom="Doctor Doom"
    )
)
sys.stdout.write(string_interpolation_prompt)

# f-Strings
sys.stdout.write("Method 3: f-strings\n")
fstring_promp = """Format strings, or f'' strings are a special type of string recently added to python
f-strings use curly brace to run an expression in the strings to format it. For example: """
thanos = "Thanos"
witch = "The Scarlet Witch"
doom = "Doctor Doom"
fstring_promp += (
    f"Some of the villians in advengers include: {doom}, {thanos}, {witch}\n\n"
)
sys.stdout.write(fstring_promp)

# Reviewing arrays or lists
villain_advengers = [thanos, witch, doom, "Loki"]
sys.stdout.write("Intro to lists\n")
reviewing_lists_prompt = f"""A list is simply a named container, much like a variable, that can hold multiple values
The values of the list is: {villain_advengers}
To index into an individual item in a list, use index notation or []
Arrays start counting their index position at index zero (0)
The first villain in the array is {villain_advengers[0]}
The second item in the array is: {villain_advengers[1]}
To print from the last item of an array, use a negative index
The last item in the array is: {villain_advengers[-1]}
The second to last item in the array is: {villain_advengers[-2]}
List slicing allows the user to copy parts of the list
Slice syntax is list[start:end] where start is the beginning index and end is the last index (exclusive)
The second and third value of villain_advengers is: {villain_advengers[1:3]}
To copy from the start index to the end of the of the list use the syntax: list[start:]
The items after the first item are: {villain_advengers[1:]}
The syntax to copy from the start of the list to the ending index is: list[:end]
The first three items in the list are: {villain_advengers[:3]}\n\n"""
sys.stdout.write(reviewing_lists_prompt)


# Strings as arrays or lists
hello_string = "Hello, World!"
list_representation_of_hello_string = [
    "H",
    "e",
    "l",
    "l",
    "o",
    ",",
    " ",
    "W",
    "o",
    "r",
    "l",
    "d",
    "!",
]
sys.stdout.write("Strings as lists\n")
string_lists_prompt = f"""A string is technically a linked-list of characters saved in your program
A linked-list can be though of as an array or a list
In other words, the String data type is an array or 'string' of linked characters
Knowing that Strings funcationally work the same as array, you can use array syntax to work with substrings
A substring is simply a small sub-section of a larger string. For example:
the variables hello_string: {hello_string} and list_representation_of_hello_string: {list_representation_of_hello_string} are practically identical
Arrays and Strings both start counting their index position at index zero (0)
This means the first character in any string will always be at index 0
Each character or element after that will have an incremental index
Use index notation to print an individual character
The first letter in {hello_string} is: {hello_string[0]}
The second letter in {hello_string} is: {hello_string[1]}
The last letter in {hello_string} is: {hello_string[-1]}
The last word in hello_string is {hello_string[7:]}
The first word in hello_string is: {hello_string[:7]}\n\n"""
sys.stdout.write(string_lists_prompt)

# Comparing String
sys.stdout.write("Comparing Strings\n")
s1 = "Hello"
s2 = "Hello"
s3 = "World"
s4 = f"{s1} {s3}"
comparing_strings_prompt = f"""s1 = {s1}
s2 = {s2}
s3 = {s3}
The == and != operators will compare to see if the strings are exactly equal or not equal."
s1 == s2: {s1 == s2}
s1 == s2: {s2 == s3}
s1 != s2: {s1 != s3}
s1 == s2: {s2 != s3}
The <, <=, >, >= operators are used to compare based on alphabetical order
s1 < s2: {s1 < s2}
s1 < s3: {s1 < s3}
s1 <= s2: {s1 <= s2}
s1 <= s3: {s1 <= s3}
s1 > s2: {s1 > s2}
s1 > s3: {s1 > s3}
s1 >= s2: {s1 >= s2}
s1 >= s3: {s1 >= s3}
The 'in' operator is used to check if value is in a sequence or collection
Is 'world' in '{s4}'? {"world" in s4}
Is '{s3}' in '{s4}'? {s3 in s4}
This syntax also applies to a list
Is 'Loki' in {villain_advengers}? {'Loki' in villain_advengers}\n\n"""
sys.stdout.write(comparing_strings_prompt)
