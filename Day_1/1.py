# filename = "1_input.txt"
filename = "example.txt"

ZERO = set(("0", "zero"))
ONE = set(("1", "one"))
TWO = set(("2", "two"))
THREE = set(("3", "three"))
FOUR = set(("4", "four"))
FIVE = set(("5", "five"))
SIX = set(("6", "six"))
SEVEN = set(("7", "seven"))
EIGHT = set(("8", "eight"))
NINE = set(("9", "nine"))
DIGITS = set()
DIGITS.update(ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


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
    letters = ""
    line_num: list[str] = []
    line = set((line))
    line = line.intersection(DIGITS)

    first = line_num[0]
    last = line_num[-1]
    firstNlast = first + last
    return int(firstNlast)


if __name__ == "__main__":
    main(filename)

    char = ""
    char.isdigit()
