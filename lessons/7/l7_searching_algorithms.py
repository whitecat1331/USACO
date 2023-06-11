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
3. On average, there will be n/2 comparisons

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

print("simple_recursion\n\n")
def simple_recursion(n):
    print(f"The current value of n is: {n}\n")

    # base case if n is 0
    if(n == 0):
        print("This is the base condition where n == 0\n\n")
        return
    # else call the function with one less of n
    simple_recursion(n-1)
    return # this is implied but added for clarity

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
Any time a new function is called, all of the data that function needs to execute is pushed to the process stack.
This collection of memory reserved for a function is known as a Stack Frame.

To analyze a function, simply keep track of the current stack frame and the variables within it
to understand what the recursive algorithm is doing.


Analysis of fib function:

Stack Trace

Level 1: fib(5) calls fib(4) and fib(3) 

Level 2: fib(4) calls fib(3) and fib(2)
Level 2: fib(3) calls fib(2) and fib(1)

Level 3: fib(3) calls fib(2) and fib(1)
Level 3: fib(2) returns 1
Level 3: fib(2) returns 1
Level 3: fib(1) returns 1

Level 4: fib(3) calls fib(2) and fib(1) 
Level 4: fib(2) and fib(1) returns 1

| Stack Level | Function Called | Stack Frame Value | Returned Value         |
|-------------|-----------------|-------------------|------------------------|
| 1           | fib(5)          | n=5               | return fib(4) + fib(3) |
| 2           | fib(4)          | n=4               | return fib(3) + fib(2) |
| 2           | fib(3)          | n=3               | return fib(2) + fib(1) |
| 3           | fib(3)          | n=3               | return fib(2) + fib(1) |
| 3           | fib(2)          | n=2               | return 1               |
| 3           | fib(2)          | n=2               | return 1               |
| 3           | fib(1)          | n=1               | return 1               |
| 4           | fib(2)          | n=2               | return 1               |
| 4           | fib(1)          | n=1               | return 1               |


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

print("Binary Search\n\n")

binary_search_explanation = """Binary search is considered a complex algorithm, but can be very useful once you see where it can be used.
Binary search has a faster time complexity on average. 
The Binary Search algorithm must start with a sorted array or list. 
Binary search utilizes this fact to optimize where to search next.
Recursion is typically used for Binary Search as it is a more complex algorithm.

The steps for binary search are as follows:
    1. The array must be sorted
    2. Cut the array in half and check the middle value for the target value.
    3. If the target value equals the middle value, return that index.
    4. If the value does not equal, check if the target value is greater than or less than the middle value.
    5. If the target value is less than the middle, than the assumption can be made it is not in the right half of the array meaning we now only need to search the left half.
    6. If the target value is greater than the middle, than the assumption can be made it is not in the left half of the array meaning we now only need to search the right half.
    7. Repeat steps 3-6 until either the target value is found or the algorithm gets to a single array size and still has not found the value.
    8. Return -1 if the algorithm does not find the target value.

Binary search can be confusing at first, but chances are you have already used this algorithm without even thinking about it.
Think back to how you typically search through a dictionary for the definition of a word. 

Similarities between a Dictionary Search and Binary Search:

- A dictionary is already sorted.
- First you typically divide the dictionary in half.
- If your target word is farther in the dictionary than the middle word you indexed to, than you know you need to search in the right half of the dictionary.
- If your target word is closer to the start of the dictionary than the middle word you indexed to, than you know you need to search in the left half of the dictionary.
- Next you typically divide the chosen half again and compare the new page to the target word you are searching for.
- This repeats until you either find the word or are unsuccessful in the word search. 

Analysis of Binary Search

- In the best case, the key is found on the first try i.e. (low+high)/2 = key
- In the worst case, the key is not in the array or is at an endpoint of the array. Here,
the n elements must be divided by 2 until there is just one element, and then that last
element must be compared with the key. An easy way to find the number of comparisons in the worst
is to round n up to the next power of 2 and take the exponent. For example, if the number of elements 
n = 32 = 2^5, then the number of comparisons refers to the number of passes through the search loop of 
the above algorithm-namely, the outer else piece of code.
- Due to an uneven split in the algorithm,
there's an interesting wrinkle when discussing the worst case of a binary search that uses the above algorithm. 
The worst case can be an endpoint or a value not in the array.
With this being said, not all endpoints or values that are not in the array are the worst case.

"""
print(binary_search_explanation)

# Binary Search Example

def binary_search(arr, target, low, high):
    # Base case (failed search)
    if(low > high):
        return -1
    # find mid-point of array
    # forcing the midpoint to an integer will always round the midpoint to the left of an uneven list.
    # lossy conversion is not always bad.
    mid = int(low + (high - low) / 2)
    # return index if target is found
    if(arr[mid] == target):
        return mid
    # case when target is greater than the midpoint
    if(target > arr[mid]):
        return binary_search(arr, target, mid + 1, high)
    # case when target is less than the midpoint
    else:
        return binary_search(arr, target, low, mid - 1)


sorted_list = [1,3,5,7,9]
binary_target_number = 3

print(f"The target number is at index: {binary_search(sorted_list, binary_target_number, 0, len(sorted_list) - 1)}\n\n")


# Python in operator
print("in operator\n\n")
in_operator_explanation = """The in operator in Python is a quick way to perform a linear search on a list. 
Basic Syntax:
    if x in list:
        pass
It checks if the target value on the left is contained within the iterable on the right.
It will return true if the value is in the list or false if the value is not in the list.

"""

simple_list = [1, 3, 4, 78, 99, -2, -100]
simple_target_value = 1
bad_value = 1.5

print(f"Is {simple_target_value} in {simple_list}? {simple_target_value in simple_list}\n\n")

if not bad_value in simple_list:
    print(f"{bad_value} is not in {simple_list}\n\n")


