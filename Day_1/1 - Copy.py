# filename = "1_input.txt"
filename = "example.txt"

ZERO = set(("0", "z", "ze", "zer", "zero"))
ONE = set(("1", "o", "on", "one"))
TWO = set(("2", "t", "tw", "two"))
THREE = set(("3", "th", "thr", "thre", "three"))
FOUR = set(("4", "f", "fo", "fou", "four"))
FIVE = set(("5", "fi", "fiv", "five"))
SIX = set(("6", "s", "si", "six"))
SEVEN = set(("7", "se", "sev", "seve", "seven"))
EIGHT = set(("8", "e", "ei", "eig", "eigh", "eight"))
NINE = set(("9", "n", "ni", "nin", "nine"))
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
    for letter in line:
        letters += letter
        if letters not in DIGITS:
            letters = letters[1:]

        if letters == "zero" or letters == "0":
            line_num.append("0")
            letters = ""
        elif letters == "one" or letters == "1":
            line_num.append("1")
            letters = ""
        elif letters == "two" or letters == "2":
            line_num.append("2")
            letters = ""
        elif letters == "three" or letters == "3":
            line_num.append("3")
            letters = ""
        elif letters == "four" or letters == "4":
            line_num.append("4")
            letters = ""
        elif letters == "five" or letters == "5":
            line_num.append("5")
            letters = ""
        elif letters == "six" or letters == "6":
            line_num.append("6")
            letters = ""
        elif letters == "seven" or letters == "7":
            line_num.append("7")
            letters = ""
        elif letters == "eight" or letters == "8":
            line_num.append("8")
            letters = ""
        elif letters == "nine" or letters == "9":
            line_num.append("9")
            letters = ""

        if letters not in DIGITS and letters:
            letters = ""

    first = line_num[0]
    last = line_num[-1]
    firstNlast = first + last
    return int(firstNlast)


if __name__ == "__main__":
    main(filename)

    char = ""
    char.isdigit()
