import sys

CHARS_IN_ALAPHABET = 26

with open("input.txt", "r") as f:
    # read in integer for dictionary
    words_in_dict = int(f.readline())

    # add each word in a list
    dict_words = [f.readline() for _ in range(words_in_dict)]

    # read in the remaining lines
    for encrypted_text in f.readlines():
        decrypt_attempt = ""
        for i in range(CHARS_IN_ALAPHABET):
            for char in encrypted_text:
                if char == " ":
                    decrypt_attempt += " "
                    continue
                    
                # subtract each position in letter by one 


                # use dictionary to guess the letter map

            # check if word is found in the string and print string
            # The any() function takes an iterate
            print(f"The attempt is: {decrypt_attempt}")
            if any(dict_word in decrypt_attempt for dict_word in dict_words):
                sys.std.write(decrypt_attempt + '\n')

            decrypt_attempt = ""
    
    
        # if no solution is found print an * for each char in the string
        for char in encrypted_text:
            if char == " ":
                continue
            decrypt_attempt += "*"

        sys.stdout.write(decrypt_attempt + '\n')
        

