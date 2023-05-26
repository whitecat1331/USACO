import sys

"""
Corporate name changes are occurring with ever greater frequency, as companies merge,
buy each other out, try to hide from bad publicity, or even raise their stock price –
remember when adding a .com to a company’s name was the secret to success!
These changes make it difficult to figure out the current name of a company when
reading old documents. Your company, Digiscam (formerly Algorist Technologies), has
put you to work on a program which maintains a database of corporate name changes
and does the appropriate substitutions to bring old documents up to date.
Your program should take as input a file with a given number of corporate name
changes, followed by a given number of lines of text for you to correct. Only exact
matches of the string should be replaced. There will be at most 100 corporate changes,
and each line of text is at most 1,000 characters long. 
"""

class CorporateReplacements:

    def __init__(self, replacemnt_file):
        self.replacement_file = replacemnt_file
        self.replacement_map = {}
        self.string_buff = ""
        self.new_buffer = ""

        self.parse_file()

    def parse_file(self):
        # Open file using context manager
        with open(self.replacement_file, "r") as f:
            # set number of maps to the first number in file
            self.number_of_maps = int(f.readline())
            # Create a map of the word to replace as the key and the word to replace with as the value
            for _ in range(self.number_of_maps):
                # split the word to replace and work to replace with using the keywork to and store that as a list
                line_list = f.readline().split("to")
                # convert the list to a map and strip off any whitespace and quotation marks
                self.replacement_map[line_list[0].strip().strip('"')] = line_list[1].strip().strip('"')

            # read in how many lines should be checked for replacement 
            self.number_of_lines_remaining = int(f.readline())

            # read in the line 
            for _ in range(self.number_of_lines_remaining):
                # read current line 
                current_line = f.readline()
                # for each line, iterate through each old word and new word and replace if a match is found
                for old_word, new_word in self.replacement_map.items():
                    if old_word in current_line:
                        current_line = current_line.replace(old_word, new_word)
                            
                # append the new line to a buffer
                self.new_buffer += current_line

    def print_buff(self):
        sys.stdout.write(self.new_buffer + '\n')

    def print_map(self):
        sys.stdout.write(str(self.replacement_map) + '\n')


def main():
    cr = CorporateReplacements("corporate_renamings.txt")
    cr.print_buff()

if __name__ == "__main__":
    main()
