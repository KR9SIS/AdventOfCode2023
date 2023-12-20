# filename = "4_input.txt"
filename = "example.txt"


class Scratchcards:
    """
    Game rules:
        if card 1 has four matches, then you get A copy of cards 2 til 5
        Then you calculate the copies created by your copies. Keep doing this until no more copies are generated.

    """

    def __init__(self) -> None:
        self.cards: dict[int, tuple[list[int]]] = {}
        self.copies: dict[int, int] = {}
        self.matches: dict[int, int] = {}
        self.card_points: list[int] = []

        self.get_cards_n_copies()
        self.calc_matches()
        points = sum(self.card_points)
        print(points)

    def get_cards_n_copies(self):
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

                self.cards[card] = (win_num, numbers)
                self.copies[card] = 0

    def calc_matches(self):
        for card, numbers in self.cards.items():
            matches = 0
            win_num, num = numbers
            for win in win_num:
                if win in num:
                    matches += 1
            self.matches[card] = matches
            """"""

    def calc_wins(self):
        for card, matches in self.matches.items():
            pass
            # for win in pass:


if __name__ == "__main__":
    cards = Scratchcards()
