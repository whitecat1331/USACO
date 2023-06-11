import sys

sys.stdin = open("diamond.in")
input = sys.stdin.readline
sys.stdout = open("diamond.out", "w")
print = sys.stdout.write

def main():
    first_row = [ int(n) for n in input().split(" ") ]
    N = first_row[0]
    K = first_row[1]
    
    diamonds = []

    for i in range(N):
        diamonds.append(int(input()))

    most = 0
     # Iterate through all diamonds.
     # Test setting them as the smallest diamond in the case.
    for x in diamonds:
        fittable = 0

        # Get all diamonds at least as large as x (including x iteself)
        # that differ from it by no more than k.
        for y in diamonds:
            if (x <= y and y <= x + K):
                fittable += 1

        most = max(most, fittable)

    print(f"{most}\n")




if __name__ == "__main__":
    main()

