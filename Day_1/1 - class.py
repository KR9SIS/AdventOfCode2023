class numFinder:
    def __init__(self, file: str):
        self.content: list[str] = []  # Every line in the file
        self.line_num: set[str] = set()  # Every number in a line
        self.num_ord: list[str] = []  # The order of the numbers in a line
        self.file_num: list[int] = []  # Every lines first and last digit put together

        self.DIGITS: dict[str, list[str]] = {
            "zero": ["0", "zero"],
            "one": ["1", "one"],
            "two": ["2", "two"],
            "three": ["3", "three"],
            "four": ["4", "four"],
            "five": ["5", "five"],
            "six": ["6", "six"],
            "seven": ["7", "seven"],
            "eight": ["8", "eight"],
            "nine": ["9", "nine"],
        }
        self.PARTS: dict[str, set[str]] = {
            "zero": set(("z", "ze", "zer")),
            "one": set(("o", "on")),
            "two": set(("t", "tw")),
            "three": set(("t", "th", "thr", "thre")),
            "four": set(("f", "fo", "fou")),
            "five": set(("f", "fi", "fiv")),
            "six": set(("s", "si")),
            "seven": set(("s", "se", "sev", "seve")),
            "eight": set(("e", "ei", "eig", "eigh")),
            "nine": set(("n", "ni", "nin")),
        }

        self.get_file_content(file)
        for line in self.content:
            self.get_num(line)
            self.get_num_ord(line)
            self.first_last()
        self.show_sum()

    def get_file_content(self, file):
        with open(filename) as file:
            for line in file:
                self.content.append(line)

    def get_num(self, line: str):
        self.line_num = set()
        for number in self.DIGITS.values():
            for version in number:
                if version in line:
                    self.line_num.add(version)

    def get_num_ord(self, line: str):
        """
        Case:
            1. Normal "f1d" extracts 1
            2. Word "feightg" extracts 8
            3. Digit in word "ei9ht" extracts 9
            4. Word in word "oneight" extracts one & eight
        """
        self.num_ord = []
        n_parts = set()
        for key in self.line_num:
            try:
                n_parts = n_parts.union(self.PARTS[key])
            except:
                """"""

        curr_word = ""
        for char in line:
            if char in self.line_num:  # Case 1 & 3
                self.num_ord.append(char)  # Character is a digit
                curr_word = ""
            if char.isalpha():  # Case 2 & 4
                curr_word += char
                if curr_word in self.line_num:  # Case 2
                    self.num_ord.append(curr_word)
                    if curr_word[-1] in n_parts:
                        curr_word = curr_word[-1]  # Case 4
                    else:
                        curr_word = ""
                elif curr_word in n_parts:  # Poosible case 2
                    pass
                else:
                    curr_word = ""  # Not a case

    def first_last(self):
        integers = []
        for i in self.num_ord:
            try:
                int(i)  # Check whether the element is i.e. a "1" or a "one"
                integers.append(i)
            except:
                num = self.DIGITS[i][0]
                integers.append(num)

        first = integers[0]
        last = integers[-1]
        firstNlast = first + last
        self.file_num.append(int(firstNlast))

    def show_sum(self):
        answer = sum(self.file_num)
        print(answer)


if __name__ == "__main__":
    filename = "1_input.txt"
    # filename = "example.txt"

    lookup = numFinder(filename)
