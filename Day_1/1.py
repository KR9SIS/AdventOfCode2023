filename = "1_input.txt"
# filename = "example.txt"
digits = [
    "0",
    "zero",
    "1",
    "one",
    "2",
    "two",
    "3",
    "three",
    "4",
    "four",
    "5",
    "five",
    "6",
    "six",
    "7",
    "seven",
    "8",
    "eight",
    "9",
    "nine",
]


def main(filename):
    file_num = check_file(filename)
    answer = sum(file_num)
    print(answer)


def check_file(filename):
    with open(filename, "r") as file:
        numbers = []
        for line in file:
            l_num = check_line(line)
            numbers.append(l_num)
        return numbers


def check_line(line):
    line_num: list[str] = []
    for digit in digits:
        if digit in line:
            try:
                int(digit)
                line_num.append(digit)
            except:
                index = digits.index(digit)
                line_num.append(digits[index - 1])
    first = line_num[0]
    last = line_num[-1]
    firstNlast = first + last
    return int(firstNlast)


if __name__ == "__main__":
    main(filename)
