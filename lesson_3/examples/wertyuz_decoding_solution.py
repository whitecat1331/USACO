import sys

# create 2d array for each key on laptop
qwerty_keys = [
            ['~','!','@','#','$','^','&','*','(',')','_','+'],
            ['1','2','3','4','5','6','7','8','9','0','-','='],
            ['q','w','e','r','t','y','u','i','o','p','[',']','\\'],
            ['a','s','d','f','g','h','j','k','l',';', '\''],
            ['z','x','c','v','b','n','m',',','.','/']
        ]
excluded_keys = [first_key[0] for first_key in qwerty_keys]
sample_input = "O S, GOMR YPFSU/"
expected_result = "I AM FINE TODAY."
string_buffer = ""

# iterate through letter
for letter in sample_input.casefold():
    # check if letter is not in excluded_keys
    if not letter in excluded_keys:
        # check which row the letter is in
        for i in range(len(qwerty_keys)):
           for j in range(len(qwerty_keys[i])):
                if letter is qwerty_keys[i][j]:
                    letter = qwerty_keys[i][j-1]
    string_buffer += letter
    
string_buffer = string_buffer.upper()
sys.stdout.write(string_buffer + '\n')
