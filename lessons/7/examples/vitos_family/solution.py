import sys

sys.stdin = open("sample_input.txt")
input = sys.stdin.readline 
print = sys.stdout.write

def main():

    number_of_test_cases = int(input())

    for i in range(number_of_test_cases):
        # convert line to list of integers
        test_case = [ int(n) for n in input().split(" ") ]
        number_of_relatives = test_case[0]
        test_case = test_case[1::]
        # Ensure the list is sorted by distance and there are no duplicates
        test_case = sorted(set(test_case))

        # Use the equation provided to find the sum of distances between relatives 
        sum = 0
        for i in range(number_of_relatives - 1):
            sum += abs(test_case[i] - test_case[i + 1])

        print(f"{sum}\n")


        
 
    return 0

if __name__ == "__main__":
    main()

