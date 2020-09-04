import random

class Game:
    def __init__(self, bet = 0):
        self.deck()
        self.bet = bet

    def deck(self):
        self.cards = [('h1',11),('h2',2),('h3',3),('h4',4),('h5',5),('h6',6),('h7',7),('h8',8),('h9',9),('h10',10),('hj',10),('hq',10),('hk',10),
                      ('c1',11),('c2',2),('c3',3),('c4',4),('c5',5),('c6',6),('c7',7),('c8',8),('c9',9),('c10',10),('cj',10),('cq',10),('ck',10),
                      ('d1',11),('d2',2),('d3',3),('d4',4),('d5',5),('d6',6),('d7',7),('d8',8),('d9',9),('d10',10),('dj',10),('dq',10),('dk',10),
                      ('s1',11),('s2',2),('s3',3),('s4',4),('s5',5),('s6',6),('s7',7),('s8',8),('s9',9),('s10',10),('sj',10),('sq',10),('sk',10)]

    def start(self):
        self.deck()
        random.shuffle(self.cards)
        self.dealer_total = self.cards[0][1]
        self.player_total = self.cards[1][1] + self.cards[2][1]
        self.dealer_cards = [self.cards[0]]
        self.player_cards = [self.cards[1], self.cards[2]]
        if self.player_total > 21:
            for card in range(len(self.player_cards)):
                if self.player_cards[card][0] == 'c1':
                    self.player_cards.pop(card)
                    self.player_cards.append(('c1', 1))
                if self.player_cards[card][0] == 'h1' :
                    self.player_cards.pop(card)
                    self.player_cards.append(('h1', 1))
                if self.player_cards[card][0] == 's1' :
                    self.player_cards.pop(card)
                    self.player_cards.append(('s1', 1))
                if self.player_cards[card][0] == 'd1':
                    self.player_cards.pop(card)
                    self.player_cards.append(('d1', 1))
                self.player_total = sum(self.player_cards[x][1] for x in range(len(self.player_cards)))
                if self.player_total <= 21:
                    break
        return self.cards[0][0], self.cards[1][0], self.cards[2][0]

    def add_bet(self, bet):
        if self.bet - bet < 0:
            return
        else: self.bet -= bet

    def tirer(self):
        self.player_cards.append(self.cards[0])
        self.player_total = sum(self.player_cards[x][1] for x in range(len(self.player_cards)))
        if self.player_total > 21:
            for card in range(len(self.player_cards)):
                if self.player_cards[card][0] == 'c1':
                    self.player_cards.pop(card)
                    self.player_cards.append(('c1', 1))
                if self.player_cards[card][0] == 'h1' :
                    self.player_cards.pop(card)
                    self.player_cards.append(('h1', 1))
                if self.player_cards[card][0] == 's1' :
                    self.player_cards.pop(card)
                    self.player_cards.append(('s1', 1))
                if self.player_cards[card][0] == 'd1':
                    self.player_cards.pop(card)
                    self.player_cards.append(('d1', 1))
                self.player_total = sum(self.player_cards[x][1] for x in range(len(self.player_cards)))
                if self.player_total <= 21:
                    break
        return self.cards[0][0]

    def tirer_split(self, player_cards):
        player_cards.append(self.cards[0])
        total = sum(player_cards[x][1] for x in range(len(player_cards)))
        if total > 21:
            for card in range(len(player_cards)):
                if player_cards[card][0] == 'c1':
                    player_cards.pop(card)
                    player_cards.append(('c1', 1))
                if player_cards[card][0] == 'h1' :
                    player_cards.pop(card)
                    player_cards.append(('h1', 1))
                if player_cards[card][0] == 's1' :
                    player_cards.pop(card)
                    player_cards.append(('s1', 1))
                if player_cards[card][0] == 'd1':
                    player_cards.pop(card)
                    player_cards.append(('d1', 1))
                total = sum(player_cards[x][1] for x in range(len(player_cards)))
                if total <= 21:
                    break
        return self.cards[0][0], total

    def doubler(self, bet):
        if self.bet - bet >= 0:
            self.bet -= bet

    def rester(self):
        self.dealer_cards.append(self.cards[0])
        self.dealer_total = sum(self.dealer_cards[x][1] for x in range(len(self.dealer_cards)))
        if self.dealer_total > 21:
            for card in range(len(self.dealer_cards)):
                if self.dealer_cards[card][0] == 'c1':
                    self.dealer_cards.pop(card)
                    self.dealer_cards.append(('c1', 1))
                if self.dealer_cards[card][0] == 'h1' :
                    self.dealer_cards.pop(card)
                    self.dealer_cards.append(('h1', 1))
                if self.dealer_cards[card][0] == 's1' :
                    self.dealer_cards.pop(card)
                    self.dealer_cards.append(('s1', 1))
                if self.dealer_cards[card][0] == 'd1':
                    self.dealer_cards.pop(card)
                    self.dealer_cards.append(('d1', 1))
                self.dealer_total = sum(self.dealer_cards[x][1] for x in range(len(self.dealer_cards)))
        return self.cards[0][0]

    def split(self):
        self.player_split1 = [self.player_cards[0], self.cards[0]]
        self.player_split2 = [self.player_cards[1], self.cards[1]]
        self.player_total1 = sum(self.player_split1[x][1] for x in range(len(self.player_split1)))
        self.player_total2 = sum(self.player_split2[x][1] for x in range(len(self.player_split2)))

        return self.cards[0][0], self.cards[1][0]

    def check_win(self, total):
        if total > 21:
            return False
        if self.dealer_total > 21:
            return True
        if self.dealer_total > total:
            return False
        if total > self.dealer_total:
            return True
        if total == self.dealer_total:
            return None

    def benefit(self, bet, total):
        if self.check_win(total) == None:
            self.bet = bet
        if self.check_win(total):
            self.bet += 2 * (bet - self.bet)

    def lost(self, total):
        if total > 21:
            return True
