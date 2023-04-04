import sys

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
advengers = {"Thor",the_witch, "Hulk"}
ordered_numbers = {1,2,3,4,5,6,7}
unordered_examples_prompt = f"""The order that the write statement prints sets will be random each time. 
advengers: {advengers}
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
advengers.remove(the_witch)
sys.stdout.write(str(advengers) + '\n')
villians.add(the_witch)
sys.stdout.write(str(villians) + '\n\n')

