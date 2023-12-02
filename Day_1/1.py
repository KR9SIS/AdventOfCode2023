with open(r"Day_1\1_input.txt", "r") as file:
    first_last = []
    for line in file:
        numbers = []
        for letter in line:
            try:
                number = int(letter)
                numbers.append(number)
            except:
                """"""
        first = str(numbers[0])
        last = str(numbers[-1])
        comp = first + last
        comp = int(comp)
        first_last.append(comp)

answer = sum(first_last)
print(answer)
