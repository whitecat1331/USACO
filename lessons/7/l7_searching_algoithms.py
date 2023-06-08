import sys

print = sys.stdout.write

# Linear/Sequential Search
print("Linear Search\n\n")

linear_search_explanation = """The linear search algorithm is a very common algorithm to find a key value within a list.
This algorithm started by iterating through a list one by one from left to right (or right to left) and will check the current value to the target value.
If the target value is found then the index or a true value will be returned.
If the algorithm finishes without finding a target then -1 or false can be returned

"""

print(linear_search_explanation)

# Linear/Sequential Search Example
list_of_numbers = [100, 25, 75, 50, 99, 5, 2]
target_number = 50


def linear_search_index(list_to_search, target_number):
    # iterate through each item in the list and compare against the target_number
    # i is the index for the current value
    for i in range(len(list_of_numbers)):
        if list_to_search[i] == target_number:
            return i

    # if the function does not find the value within the list then -1 is returned.
    return -1

def linear_search_boolean(list_to_search, target_number):
    result = linear_search_index(list_to_search, target_number)
    return True if result >= 0 else False

print(f"Is the target_number in the list of numbers?: {linear_search_boolean(list_of_numbers, target_number)}\n")
print(f"The index of the target number is: {linear_search_index(list_of_numbers, target_number)}\n\n")

# Linear Search Analysis

linear_search_analysis = """Analysis
1. The best case has the key in the first slot.
2. The worst case occurs if the key is in the last slot or not in the list. In the worst case, all n elements must be examined.
3. On average, the will be n/2 comparisons

"""
print(linear_search_analysis)

# Recursion
print("Recursion\n\n")

recursion_explanation = """A recursive function is simply a function that calls itself within the function implementation.
A recursive function solves problems similar to how iteration works. 
In fact, any problem that can be iteratively can also be solved recursively. 

The basic syntax for a recursive function is

def recursive_method(some_value):
    # The base case is what will stop the function from calling itself again.
    # In other words, the base condition is the condition that is met for the algorithm to be finished.
    if (some_value == some_condition):
        end the function and return
    else:
        call recursive_method(some_value)

General Rules for recursion
1. Avoid recursion for algorithms that involve large local arrays
2. Use recursion when it significantly simplifies code.
3. Avoid recursion for simple iterative methods i.e. fib
4. Recursion is especially useful for:
    - Branching processes like traversing trees or directories
    - Divide-and-conquer algorithms like merge sort and binary search.

"""

print(recursion_explanation)


# Recursion Examples
print("Recursion Examples\n\n")

def simple_recursion(n):
    print(f"The current value of n is: {n}\n")

    # base case if n is 0
    if(n == 0):
        print("This is the base condition where n == 0\n\n")
        return
    # else call the function with one less of n
    simple_recursion(n-1)
    return # this is implied but added for clarity

print("simple_recursion\n\n")
simple_recursion(10)

print("raise_power\n\n")
def raise_power(base, power):
    if (power == 0):
        return 1
    print(f"{base} * raise_power({base}, {power - 1})\n")
    return base * raise_power(base, power - 1)
power_result = raise_power(2,3)
print(f"2 ** 3 = {power_result}\n\n")

print("fib\n\n")
def fib(n):
    if(n == 1 or n == 2):
        return 1
    return fib(n-1) + fib(n-2)

print(f"The fib value at sequence 5 is: {fib(5)}\n\n")

# Analyzing and Understanding Recursion
analyzing_recursion = f"""To fully understand recursion, you need to understand how the Stack work.
Programs are divided into three sections of memory, the Stack, the Heap, and Static memory.
The Heap and Static memory are not important right now.
Stack memory is a stack data structure meaning it follows the FILO (First In Last Out) rule.
By convention, programs use the stack to run functions by pushing parameters and other data to the stack.
Any time a new function is called, all of the data that function needs is pushed to the process stack.
This collection of memory reserved for a function is known as a Stack Frame.

To analyze a function, simply keep track of the current stack frame and the variables within it
to understand what the recursive algorithm is doing.


Analysis of fib function:

Stack Trace

Level 1: fib(5) calls fib(4) and fib(3)

Level 2: fib(4) call fib(3) and fib(2)
Level 2: fib(3) calls fib(2) and fib(1)

Level 3: fib(4) calls fib(3) and fib(2)
Level 3: fib(3) calls fib(2) and fib(1)

Level 4: fib(3) calls fib(2) and fib(1)

| Stack Level | Function Called | Stack Frame Value | Returned Value       |
|-----------|-----------------|-------------------|------------------------|
| 1         | fib(5)          | n=5               | return fib(4) + fib(3) |
| 2         | fib(4)          | n=4               | return fib(3) + fib(2) |
| 2         | fib(3)          | n=3               | return fib(2) + fib(1) |
| 3         | fib(3)          | n=3               | return fib(2) + fib(1) |
| 3         | fib(2)          | n=2               | return 1               |
| 3         | fib(2)          | n=2               | return 1               |
| 3         | fib(1)          | n=1               | return 1               |
| 4         | fib(2)          | n=2               | return 1               |
| 4         | fib(1)          | n=1               | return 1               |


Working back up the tree
fib(1) = 1
fib(2) = 1
fib(3) = 1 + 1 = 2
fib(4) = 2 + 1 = 3
fib(5) = 3 + 2 = 5


"""
print(analyzing_recursion)

# Infinite Recusion
print("Infinite Recusion\n\n")

infinite_recursion = """A recursive method that does not have a base case will result in a Stackoverflow error.
A Stackoverflow error is known as a RecursionError in Python. 
This occurs when too many functions are called at one without returning and the stack runs out of memory. 

"""
print(infinite_recursion)

def infinite_recursion():
    infinite_recursion()

# infinite_recursion() # RecursionError

# Binary Search
