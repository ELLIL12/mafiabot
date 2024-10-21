import random

class Cards:
    def __init__(self):
        self.cards_in = ["fascist"] * 11 + ["liberal"] * 6     # карты в колоде
        self.cards_out = []     # сюда надо складывать карты, которые откинули игроки

    # выкладка закона на стол
    def card_on_board(self):
        if len(self.cards_in) < 3:
            self.cards_in = self.cards_out + self.cards_in
            self.cards_out = []
        card = random.choice(self.cards_in) # Рандомно выбираем первую карту
        print(card)
        self.cards_in.remove(card)  # Удаляем 1 карту из списка карт в колоде
        card = [card] + [random.choice(self.cards_in)] # Рандомно выбираем вторую карту закидываем обе карты в общий список
        print(card)
        self.cards_in.remove(card[1]) # Удаляем 2 карту из списка
        card = card + [random.choice(self.cards_in)]    # Рандомно выбираем третью карту закидываем три карты в общий список
        self.cards_in.remove(card[2])  # Удаляем 3 карту из списка
        print(card)
        return card

coloda = Cards
coloda.card_on_board(coloda)