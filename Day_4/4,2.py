# filename = "4_input.txt"
filename = "example.txt"


class Scratchcards:
    """
    Game rules:
        if card 1 has four matches, then you get A copy of cards 2 til 5
        Then you calculate the copies created by your copies. Keep doing this until no more copies are generated.

    """

    def __init__(self) -> None:
        self.cards: dict[int, tuple[list[int], list[int], list[int], list[int]]] = {}
        self.copies: list[int] = []
        self.count = 0

        self.get_cards()
        self.card_counter()
        print(self.count)

    def get_cards(self):
        with open(filename) as file:
            for line in file:
                front, numbers = line.split("|")
                card, win_num = front.split(":")
                _, card = card.split()
                card = int(card)

                numbers = numbers.strip().split()
                win_num = win_num.strip().split()

                numbers = list(map(int, numbers))
                win_num = list(map(int, win_num))

                self.cards[card] = (win_num, numbers, [], [])

    def card_counter(self):
        for cur_card in self.cards:
            # self.count = 0
            # self.check_summary()
            self.copies.append(cur_card)
            while self.copies:
                self.calc_copies()
            self.summarise(cur_card)

    def check_summary(self):
        check = self.copies[0]
        raise NotImplemented

    def calc_copies(self):
        self.count += 1
        card = self.copies.pop(0)
        win_num, num, win_list, summary = self.cards[card]

        if win_list:
            self.copies.extend(win_list)
            # self.count += summary

        else:
            wins = 0
            for win in win_num:
                if win in num:
                    wins += 1
            if wins:
                copies = card
                for i in range(wins):
                    copies += 1
                    self.copies.append(copies)
                    win_list.append(copies)

                self.cards[card] = win_num, num, win_list, summary

    def summarise(self, current_card):
        """
        Go through every copy created by the previous card

        """
        card_points = 0
        win_num, num, copies, total = self.cards[current_card]
        for copy in reversed(copies):
            copy_win_num, copy_num, copy_copies, copy_points = self.cards[copy]
            card_points += len(copy_copies) + 1
            copy_points = card_points

            self.cards[copy] = copy_win_num, copy_num, copy_copies, copy_points

        card_points += len(copies)
        self.cards[current_card] = win_num, num, copies, card_points
        # self.count += card_points


if __name__ == "__main__":
    cards = Scratchcards()
