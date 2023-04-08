import sys
from queue import Queue

# Sets Prompt
sets_prompt = """A set in Python is a type of container/collection that is
unordered, unchangeable, and does not allow duplicate values. 

Unordered - the items in a set do not have a defined order 
and cannot be reffered to by index or key.

Unchangeable - items cannot be changed meaning once the value is added to the set it will not change it's value.
items can be removed from the set, however the item itself cannot be changed.

Duplicates Not Allowed - Sets cannot have two items with the same value.

"""
sys.stdout.write(sets_prompt)

# Unordered Examples
the_witch = "The Scarlet Witch"
sys.stdout.write("Unordered Examples:\n")
set_of_avengers = {"Thor",the_witch, "Hulk"}
ordered_numbers = {1,2,3,4,5,6,7}
unordered_examples_prompt = f"""The order that the write statement prints sets will be random each time. 
avengers: {set_of_avengers}
ordered_numbers: {ordered_numbers}

"""
sys.stdout.write(unordered_examples_prompt)

# Unchangeable Examples
sys.stdout.write("Unchangeable Examples:\n")
unchangeable_examples_prompt = """Remember, items cannot be changed once added to a set.
Items can be added and removed from a set

Add items to a set using set.update(iter) or set.add(item)
set.update() - add items to a list
set.add() - add item to a list

Remove items from a set using set.discard(item) or set.remove(item)
set.discard() - removes an item from the set and does nothing if item is not found. 
set.remove() - removes an item from the set and throws an exception if item is not found. 

"""
sys.stdout.write(unchangeable_examples_prompt)
villians = {"Thanos", "Loki"}
set_of_avengers.remove(the_witch)
sys.stdout.write(str(set_of_avengers) + '\n')
villians.add(the_witch)
sys.stdout.write(str(villians) + '\n\n')

# Duplicates Not Allowed Examples
duplicate_set = {1, 1, 2, 2, 3, 3, 4, 4}
villians.add(the_witch)
sys.stdout.write("Duplicates Not Allowed Examples\n")
sys.stdout.write(f"Duplicates will not be added within a set\nduplicate_set: {duplicate_set}\nvillians: {villians}\n\n")

# Queues
queue_prompt = """Queues are similar to a stack. 
Remember, a stack is a data structure that uses a FILO (First In Last Out) model.
A Queue is another type of data structure that uses a FIFO (First In First Out) model. 
Just like a stack of pancackes, the first pancake added to the stack is on the bottom and will be the last one eaten.
A queue is just like waiting in line to an amusement park where the fist one in the queue is the first one to ride the ride. 

Python does not have a queue data type built-in to the language.
There are still a few techiniques and libraries that can be used to emulate a queue using Python data structures.
The closest built-in data structure Python offeres that is simlar to a queue is a list.
"""
sys.stdout.write(queue_prompt)

# Queue Implementation Using Lists
sys.stdout.write("Queue Implementation Using Lists\n")

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

sys.stdout.write("Initial queue\n")
sys.stdout.write(str(queue) + '\n')

# Removing elements from the queue
sys.stdout.write("Elements dequeued from queue\n")
sys.stdout.write(queue.pop(0) + '\n')
sys.stdout.write(queue.pop(0) + '\n')
sys.stdout.write(queue.pop(0) + '\n')

# Uncommenting sys.stdout.write(queue.pop(0))
# will raise and IndexError
# as the queue is now empty

sys.stdout.write("\nQueue after removing elements\n")
sys.stdout.write(str(queue) + '\n\n')

# Queue Implementation Using Queue Library
sys.stdout.write("Queue Implementation Using Queue Library\n")
  
# Initializing a queue
q = Queue(maxsize = 3)
  
# qsize() give the maxsize 
# of the Queue 
sys.stdout.write("The size of the queue is: " + str(q.qsize()) + '\n')
  
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
  
sys.stdout.write("The size of the queue is: " + str(q.qsize()) + '\n')

# Return Boolean for Full 
# Queue 
sys.stdout.write("\nFull: " +  str(q.full()) + '\n') 
  
# Removing element from queue
sys.stdout.write("Elements dequeued from the queue\n\n")
sys.stdout.write(q.get() + '\n')
sys.stdout.write(q.get() + '\n')
sys.stdout.write(q.get() + '\n')
  
# Return Boolean for Empty 
# Queue 
sys.stdout.write("Empty: "+ str(q.empty()) + '\n')
  
q.put(1)
sys.stdout.write("Empty: "+ str(q.empty()) + '\n' )
sys.stdout.write("Full: "+ str(q.full()) + '\n\n')

# Dictionaries 
sys.stdout.write("Dictionaries\n")
dictionary_prompt = """A dictionary in Python is a built-in data type that allows for key value pairs.
Dictionaries are useful for containing data that is grouped in pairs.
There are many practical uses for a dictionary in Python.
Dictionaries can be indexed by key to return the grouped value. 
A key in python can either be a String or a number type. 
The value of a dictionary can hold any type of object or value.

Dictionary Declaration:
Dictionaries are declared using curly braces {}. 
The key and values are sperated by a colon :.
Each key-value pair is sperated with a comma ,.

Example: 
    my_dict = {"key": "value", "another_key": "another_value"}

The value of a dictionary can be accessed by key
Example:
print(my_dict["key"]) # prints value
my_dict["key"] = "some_value"
print(my_dict["key"]) # prints some_value

Use Cases:
When working with APIs, Python uses dictionaries to model JSON objects.
They are useful anytime you have a key value pair you are trying to save in Python

"""

sys.stdout.write(dictionary_prompt)

# Dictionary Indexing
sys.stdout.write("Dictionary Indexing\n")
avengers = {"Spider-Man": "Peter Parker", "Iron-Man": "Tony Stark","Hulk": "Bruce Banner"}

US_currency = {
        "penny": .01,
        "nickel": .05,
        "dime": .10,
        "quarter": .25,
        "half-dollar": .50,
        "dollar": 1.00
                }



sys.stdout.write(f"avengers: {avengers}\nUS_currency: {US_currency}\n\n")


# Nested Dictionaries
sys.stdout.write("Nested Dictionaries\n")
ranked_avengers = {
        1: {"first_name": "Tony", "last_name": "Stark", "alias": "Iron-Man", "abilities": ["propultion thrusters", "plasma shot", "Jarvis"]},
        2: {"first_name": "Peter", "last_name": "Parker", "alias": "Spider-Man", "abilities": ["spin webs", "swing", "spidey sense"]},
        3: {"first_name": "Bruce", "last_name": "Banner", "alias": "Hulk", "abilities": ["smash", "smash", "smash"]}
        }
hulk_dict = ranked_avengers[3]
hulk_abilities = hulk_dict["abilities"]
hulk_first_ability = hulk_abilities[0]
nested_dicts_prompt = f"""Dictionaries can hold any type of object as their value.
This means that dictionaries can also hold any container type as their value, including other dictionaries.
If the value you initially index into is another container type, simply index into that type using that notation to index 
into the individual value within the entire dictionary.
There is not limit to the amount of information that is nested within a dictionary, in fact some JSON dictionaries can have five or six nested items.
With so much nesting, it can be easy to get lost in a large dictionary.
Luckily, python gives us other tools to effectively navigate a dictionary in our program.


Most manuel dictionary indexing is done with the developer knowing the values to index to.
If the developer created the dictionary, then they should know how to index into it.
If a developer is working with a large dictionary that was externally imported into the program,
then reading the documentation associated with the imported data would be the best way to find what keys to index to.

Hulk Dictionary: {ranked_avengers[3]}
Hulk Abilities: {ranked_avengers[3]["abilities"]}
Hulks First Ability: {ranked_avengers[3]["abilities"][0]}

Each object can also be saved in a variable

Hulk Dictionary: {hulk_dict}
Hulk Abilities: {hulk_abilities}
Hulks First Ability: {hulk_first_ability}

"""
sys.stdout.write(nested_dicts_prompt)

# Dictionary Methods
dict_methods_prompt = """Dictionary Methods
dict.clear() - Remove all the elements from the dictionary
dict.copy() - Returns a deep copy of the dictionary Note: setting dictionaries equal will perform a shallow copy")
dict.get(key, default="None") - Returns the value of the specified key
dict.items() - Returns a list containing a tuple for each key value pair
dict.keys() - Returns a list containing dictiaonry's keys
dict.update(dict2) - updates a dictionary with specified key-value pairs
dict.values() - Returns a list of all the values of a dictionay
dict.pop() - Remove the element with specified key
dict.popItem() Removes the last inserted key-value pair
dict.setdefault(key, default="None") - set the key to the default value if the key is not specified in the dictionary
key in dictionary - returns True if the dictionary contains the specified key
del dict[key] - remove the key-value pair at the specified key

"""
sys.stdout.write(dict_methods_prompt)

# dict.copy() - set the variable to reference the dictionary performing a shallow copy which can have unexpected results
deep_avengers_copy = avengers.copy()
shallow_avengers_copy = avengers
shallow_avengers_copy["Nick Fury"] = "Nick Fury"
sys.stdout.write(f"dict.copy()\nAny changes to a shallow copy will reflect in the original object {avengers['Nick Fury']}\n")
# dict.get(key, default="None") - Returns the value of the specified key
sys.stdout.write(f"dict.get()\nReturn a value from the dictionary by key {avengers.get('Spider-Man')}\n")
sys.stdout.write(f"Return a value from the dictionary by key {ranked_avengers.get(2)}\n")
sys.stdout.write("It is up to personal preference on how you choose to index dictionaries\n")
# dict.items() - Returns a list containing a tuple for each key value pair
sys.stdout.write(f"dict.items()\nThe key value pairs for advengers are: {avengers.items()}\n" )
# dict.keys() - Returns a list containing dictiaonry's keys
sys.stdout.write(f"dict.keys()\nThe keys in avengers are: {avengers.keys()}\n")
# dict.update(dict2) - updates a dictionary with specified key-value pairs
avengers.update({"Captain America": "Steve Rogers"})
sys.stdout.write(f"dict.update()\nThe key-value pairs in avengers is now: {avengers}\n")
# dict.values() - Returns a list of all the values of a dictionay
sys.stdout.write(f"dict.values()\nThe values for avengers are: {avengers.values()}\n")
# dict.pop() - Remove the last element with specified key.
sys.stdout.write(f"dict.pop()\nRemoved: {avengers.pop('Spider-Man')}\n")
sys.stdout.write(f"The key-value pairs in avengers is now: {avengers}\n")
# dict.popItem() - Removes the last inserted key-value pair
sys.stdout.write(f"dict.popItem()\nRemoved: {avengers.popitem()}\n")
sys.stdout.write(f"The key-value pairs in avengers is now: {avengers}\n")
# dict.setdefault(key, default="None") - set the key to the default value if the key is not specified in the dictionary
sys.stdout.write(f"dict.setdefault()\nThe value for Black-Widow is: {avengers.setdefault('Black-Widow', 'Natasha Romanoff')}\n")
# key in dictionary - returns True if the dictionary contains the specified key
sys.stdout.write(f"key in dictionary\nDoes Black-Window exist in avengers? {'Black-Widow' in avengers}\n")
# del dict[key] - remove the key-value pair at the specified key
del avengers["Iron-Man"]
sys.stdout.write(f"del dict[key]\nThe key-value pairs in avengers is now: {avengers}\n")
# dict.clear() - Remove all the elements from the dictionary
avengers.clear()
sys.stdout.write(f"The key-value pairs in avengers is now: {avengers}\n\n")
# Traversing Dictionaries

