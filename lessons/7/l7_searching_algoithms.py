import sys

print = sys.stdout.write

# Linear/Sequential Search

linear_search_explination = f"""The linear search algorithm is a very common algorithm to find a key value within a list.
This algorithm started by iterating through a list one by one from left to right (or right to left) and will check the current value to the target value.
If the target value is found then the index or a true value will be returned.
If the algorithm finishes without finiding a target then -1 or false can be returned

"""

print(linear_search_explination)

# Linear/Sequential Search Example
list_of_numbers = [100, 25, 75, 50, 99, 5, 2]
target_number = 50


def linear_search_index(list_to_search, target_number):
    # iterate through each item in the list and compare against the target_number
    for i in range(len(list_of_numbers)):
        if list_to_search[i] == target_number:
            return i

    return -1

def linear_search_boolean(list_to_search, target_number):
    result = linear_search_index(list_to_search, target_number)
    return True if result >= 0 else False

# Linear Aearch Analysis

linear_search_analysis = """Analysis
1. The best case has the key in the first slot.
2. The worst case occurs if the key is in the last slot or not in the list. In the worst case, all n elements must be examined.
3. On average, the will be n/2 comparisons

"""


# Recursion

# Binary Search
