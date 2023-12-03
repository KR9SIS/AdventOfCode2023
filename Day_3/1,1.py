from string import punctuation

# filename = "3_input.txt"

filename = "example.txt"


class find_parts:
    def __init__(self) -> None:
        self.valid_num = []
        self.numbers_in_line: dict[int, list[int]] = {}
        self.lines: list[str] = []
        self.line_number = 0
        self.curr_line_1: str = ""
        self.curr_line_2: str = ""
        self.line1_index = 0
        self.line2_index = 0
        self.string_index = 0

        self.get_file_lines(filename)
        for line_index in range(len(self.lines)):
            self.line1_index = line_index
            self.line2_index = line_index + 1
            self.get_two_lines()
            self.comp_lines()

    def get_file_lines(self, filename):
        with open(filename) as file:
            for line in file:
                self.lines.append(line.strip())

    def get_two_lines(self):
        """
        Finds the index of a specific line and the line below it and returns those.
        """
        try:
            self.curr_line_2 = self.lines[self.line2_index]
            self.curr_line_1 = self.lines[self.line1_index]
        except IndexError:
            """"""

    def checks(self, check, checked_line, cl_index):
        check = check.strip(punctuation)
        try:
            num = int(check)  # See if check is unbroken int i.e. not 1..2
            self.numbers_in_line[cl_index].append(num)
        except ValueError:
            check: str = checked_line[self.string_index - 4 : self.string_index + 5]
            curr_num = ""
            last_num = 0
            for i in check:
                try:
                    int(i)
                    curr_num += i
                except ValueError:
                    if self.numbers_in_line[cl_index]:
                        last_num = self.numbers_in_line[cl_index][-1]
                    if last_num != curr_num:
                        self.numbers_in_line[cl_index].append(curr_num)
                    curr_num = ""

    def line_check(self, i, checked_line, cl_index):
        """
        Checks if i1 is not a "." or an integer and if it is then it checks the corresponding index of line2
        """
        if i != ".":
            try:
                int(i)  # Filter awway numbers
            except ValueError:
                if self.string_index > 0:  # Account for index error
                    check: str = checked_line[
                        self.string_index - 2 : self.string_index + 1
                    ]
                    self.checks(check, checked_line, cl_index)
                else:
                    check = checked_line[: self.string_index + 2]
                    self.checks(check, checked_line, cl_index)

                    # TODO First step is to see if there are any values across or diagonally to the symbol, and then if there is I need to get that entire number.

    def comp_lines(self):
        """
        Iterate over line 1 and 2 and if line 1 shows something other than a "."
        then it checks what is in line 2 and if that is a number, then logs it as a valid num
        """
        curr_line1 = self.curr_line_1
        curr_line1_index = self.line1_index
        if curr_line1_index not in self.numbers_in_line:
            self.numbers_in_line[curr_line1_index] = []
        curr_line2 = self.curr_line_2
        curr_line2_index = self.line2_index
        if curr_line2_index not in self.numbers_in_line:
            self.numbers_in_line[curr_line2_index] = []
        for i1, i2 in zip(self.curr_line_1, self.curr_line_2):
            self.string_index += 1
            self.line_check(i1, curr_line2, curr_line2_index)
            self.line_check(i2, curr_line1, curr_line1_index)

        ""


if __name__ == "__main__":
    parts = find_parts()
