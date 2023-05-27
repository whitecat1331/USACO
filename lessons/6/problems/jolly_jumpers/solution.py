import sys

print = sys.stdout.write
sys.stdin = open("input.txt", "r")

# convert line to list 
def line_to_list(line):
    string_list = line.split()
    string_list = [int(n) for n in string_list]
    return string_list

def is_jolly(list_of_numbers):
    # iterate through each number
    absolute_difference = 0
    for i in range(len(list_of_numbers) - 1):
        # find absolute difference
        absolute_difference = abs(list_of_numbers[i] - list_of_numbers[i + 1])

        # check if not jolly
        if not absolute_difference in list_of_numbers:
            return False

        # reset 
        absolute_difference = 0

    # if the for loops finishes it means the list is jolly
    return True

def main():
    # iterate through each line
    for line in sys.stdin.readlines():
        # convert line to list
        list_of_numbers = line_to_list(line)
        # check if jolly 
        jolly = is_jolly(list_of_numbers)
        # set display to correct output
        display = "Jolly\n" if jolly else "Not Jolly\n"
        print(display)

if __name__ == "__main__":
    main()
