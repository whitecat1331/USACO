import sys


class CorporateReplacements:
    def __init__(self, replacemnt_file):
        self.replacement_file = replacemnt_file
        self.replacement_map = {}
        self.parse_file()

    def parse_file(self):
        with open(self.replacement_file, "r") as f:
            self.number_of_maps = int(f.readline())
            for _ in range(self.number_of_maps):
                line_list = f.readline().split("to")
                self.replacement_map[line_list[0]] = line_list[1]

    def print_map(self):
        print(self.replacement_map)
        # sys.stdout.write(str(self.replacement_map) + '\n')


CorporateReplacements("corporate_renamings.txt").print_map()
