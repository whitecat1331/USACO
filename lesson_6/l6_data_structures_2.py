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


