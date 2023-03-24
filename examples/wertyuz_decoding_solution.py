# create 2d array for each key on laptop
qwerty_keys = [
            ['~','!','@','#','$','^','&','*','(',')','_','+'],
            ['1','2','3','4','5','6','7','8','9','0','-','='],
            ['q','w','e','r','t','y','u','i','o','p','[',']','\\'],
            ['a','s','d','f','g','h','j','k','l',';', '\''],
            ['z','x','c','v','b','n','m',',','.','/']
        ]
excluded_keys = [first_key[0] for first_key in qwerty_keys]
sample_input = "O S, YPFSU/"
expected_result = "I AM FINE TODAY."

# iterate through each value 
for letter in sample_input:
    for row in qwerty_keys:
        for key in row:
            if letter in excluded_keys:
                pass
            elif letter in row:
                letter = letter
# check if current letter matches
        

# move letter if not first

# iterate through letter
# check if current letter is first key
# check if first key and keep same
# reset the letter to the previous key
# append the letter to a new buffer string
