# python packages needed
from tkinter import *
from os import path
import subprocess
import sys
from game import *
try:
    from PIL import Image
    from PIL import ImageTk
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image
    from PIL import ImageTk

class Gui(Canvas):
    def __init__(self, root):
        # init the gui
        self.parent = root
        self.SW = self.parent.winfo_screenwidth()
        self.SH = self.parent.winfo_screenheight()
        self.WIDTH = int(1400 / 2048 * self.SW)
        self.HEIGHT = int(1000 / 1152 * self.SH)
        self.IMAGE_FOLDER = 'images'
        self.parent.resizable(0, 0)
        self.parent.overrideredirect(True)
        width = (self.SW - self.WIDTH) // 2
        height = (self.SH - self.HEIGHT) // 2
        self.parent.geometry(f'+{width}+{height}')
        Canvas.__init__(self, self.parent, width = self.WIDTH, height = self.HEIGHT, highlightthickness = 0)
        self.started = False
        self.split_happening = False
        self.dealer_id = {}
        self.player_id = {}
        self.player1_id = {}
        self.player2_id = {}
        self.text_id = {}
        self.chips = {}
        self.game = Game()
        self.load_data()
        self.board_layout()
        self.button_layout()

    def load_data(self):
        # load images
        dir = path.dirname(__file__)
        Bg_image = Image.open(path.join(dir, self.IMAGE_FOLDER, 'Bg.png'))
        self.Bg_image = ImageTk.PhotoImage(Bg_image)
        Chip = Image.open(path.join(dir, self.IMAGE_FOLDER, 'chip.png'))
        Chip = Chip.resize((int(32 / 2048 * self.SW), int(32 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Chip = ImageTk.PhotoImage(Chip)
        Tirer = Image.open(path.join(dir, self.IMAGE_FOLDER, 'tirer.png'))
        Tirer = Tirer.resize((int(190 / 2048 * self.SW), int(49 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Tirer = ImageTk.PhotoImage(Tirer)
        Split = Image.open(path.join(dir, self.IMAGE_FOLDER, 'split.png'))
        Split = Split.resize((int(190 / 2048 * self.SW), int(49 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Split = ImageTk.PhotoImage(Split)
        Doubler = Image.open(path.join(dir, self.IMAGE_FOLDER, 'doubler.png'))
        Doubler = Doubler.resize((int(190 / 2048 * self.SW), int(49 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Doubler = ImageTk.PhotoImage(Doubler)
        Rester = Image.open(path.join(dir, self.IMAGE_FOLDER, 'rester.png'))
        Rester = Rester.resize((int(190 / 2048 * self.SW), int(49 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Rester = ImageTk.PhotoImage(Rester)
        Regles = Image.open(path.join(dir, self.IMAGE_FOLDER, 'regles.png'))
        Regles = Regles.resize((int(190 / 2048 * self.SW), int(49 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Regles = ImageTk.PhotoImage(Regles)
        Start = Image.open(path.join(dir, self.IMAGE_FOLDER, 'start.png'))
        Start = Start.resize((int(108 / 2048 * self.SW), int(48 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Start = ImageTk.PhotoImage(Start)
        CardBack = Image.open(path.join(dir, self.IMAGE_FOLDER, 'cardBack.png'))
        CardBack = CardBack.resize((int(140 / 2048 * self.SW), int(190 / 1152 * self.SH)), Image.ANTIALIAS)
        self.CardBack = ImageTk.PhotoImage(CardBack)
        White_chip = Image.open(path.join(dir, self.IMAGE_FOLDER, 'white_chip.png'))
        White_chip = White_chip.resize((int(68 / 2048 * self.SW), int(42 / 1152 * self.SH)), Image.ANTIALIAS)
        self.White_chip = ImageTk.PhotoImage(White_chip)
        Red_chip = Image.open(path.join(dir, self.IMAGE_FOLDER, 'red_chip.png'))
        Red_chip = Red_chip.resize((int(68 / 2048 * self.SW), int(42 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Red_chip = ImageTk.PhotoImage(Red_chip)
        Green_chip = Image.open(path.join(dir, self.IMAGE_FOLDER, 'green_chip.png'))
        Green_chip = Green_chip.resize((int(68 / 2048 * self.SW), int(42 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Green_chip = ImageTk.PhotoImage(Green_chip)
        Blue_chip = Image.open(path.join(dir, self.IMAGE_FOLDER, 'blue_chip.png'))
        Blue_chip = Blue_chip.resize((int(68 / 2048 * self.SW), int(42 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Blue_chip = ImageTk.PhotoImage(Blue_chip)
        Black_chip = Image.open(path.join(dir, self.IMAGE_FOLDER, 'black_chip.png'))
        Black_chip = Black_chip.resize((int(68 / 2048 * self.SW), int(42 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Black_chip = ImageTk.PhotoImage(Black_chip)
        Exit = Image.open(path.join(dir, self.IMAGE_FOLDER, 'Exit.png'))
        Exit = Exit.resize((int(50 / 2048 * self.SW), int(48 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Exit = ImageTk.PhotoImage(Exit)
        self.cards_img = {}
        for x in range(len(self.game.cards)):
            self.cards_img[self.game.cards[x][0]] = None
        for x, card in enumerate(self.game.cards):
            x = Image.open(path.join(dir, self.IMAGE_FOLDER, f'{card[0]}.png'))
            x = x.resize((int(140 / 2048 * self.SW), int(190 / 1152 * self.SH)), Image.ANTIALIAS)
            self.cards_img[card[0]] = ImageTk.PhotoImage(x)

    def board_layout(self):
        self.create_image(0, 0, image = self.Bg_image, anchor = NW)
        self.create_image(50, 50, image = self.Chip, anchor = 'center')
        id = self.create_text(75, 50, text = '0', font = int(10 / 2048 * self.SW), fill = 'white', anchor = W)
        self.text_id['bet'] = str(id)
        id = self.create_text(self.WIDTH // 2, self.HEIGHT // 2 - 50, text = 'Pot de départ', font = int(30 / 2048 * self.SW), fill = 'white', anchor = 'center')
        self.text_id['pot'] = str(id)
        self.amount = Entry(self, width = 10, font = int(10 / 2048 * self.SW))
        self.amount.place(x = self.WIDTH // 2, y = self.HEIGHT // 2, anchor = 'center')

    def button_layout(self):
        tirer_btn = Button(self, image = self.Tirer, bd = 0, command = self.tirer).place(x = self.WIDTH // 6, y = self.HEIGHT - 50, anchor = 'center')
        doubler_btn = Button(self, image = self.Doubler, bd = 0, command = self.doubler).place(x = (self.WIDTH // 6) * 2, y = self.HEIGHT - 50, anchor = 'center')
        rester_btn = Button(self, image = self.Rester, bd = 0, command = self.rester).place(x = (self.WIDTH // 6) * 3, y = self.HEIGHT - 50, anchor = 'center')
        split_btn = Button(self, image = self.Split, bd = 0, command = self.split).place(x = (self.WIDTH // 6) * 4, y = self.HEIGHT - 50, anchor = 'center')
        regles_btn = Button(self, image = self.Regles, bd = 0, command = self.regles).place(x = (self.WIDTH // 6) * 5, y = self.HEIGHT - 50, anchor = 'center')
        start_btn = Button(self, image = self.Start, bd = 0, command = self.start).place(x = (self.WIDTH // 8) * 7, y = self.HEIGHT - 200, anchor = 'center')
        exit_btn = Button(self, image = self.Exit, bd = 0, command = self.parent.destroy).place(x = self.WIDTH, y = 0, anchor = NE)

    def bet_chips(self):
        white_btn = Button(self, text = '1', font = int(10 / 2048 * self.SW), bd = 0, command = lambda: self.game.add_bet(1))
        white_btn.place(x = self.WIDTH // 8 * 2, y = self.HEIGHT // 2 - 50, anchor = 'center')
        id = self.create_image(self.WIDTH // 8 * 2, self.HEIGHT // 2, image = self.White_chip)
        self.chips['white_btn'] = white_btn
        self.chips['white_chip'] = str(id)
        red_btn = Button(self, text = '5', font = int(10 / 2048 * self.SW), bd = 0, command = lambda: self.game.add_bet(5))
        red_btn.place(x = self.WIDTH // 8 * 3, y = self.HEIGHT // 2 - 50, anchor = 'center')
        id = self.create_image(self.WIDTH // 8 * 3, self.HEIGHT // 2, image = self.Red_chip)
        self.chips['red_btn'] = red_btn
        self.chips['red_chip'] = str(id)
        green_btn = Button(self, text = '25', font = int(10 / 2048 * self.SW), bd = 0, command = lambda: self.game.add_bet(25))
        green_btn.place(x = self.WIDTH // 8 * 4, y = self.HEIGHT // 2 - 50, anchor = 'center')
        id = self.create_image(self.WIDTH // 8 * 4, self.HEIGHT // 2, image = self.Green_chip)
        self.chips['green_btn'] = green_btn
        self.chips['green_chip'] = str(id)
        blue_btn = Button(self, text = '50', font = int(10 / 2048 * self.SW), bd = 0, command = lambda: self.game.add_bet(50))
        blue_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 2 - 50, anchor = 'center')
        id = self.create_image(self.WIDTH // 8 * 5, self.HEIGHT // 2, image = self.Blue_chip)
        self.chips['blue_btn'] = blue_btn
        self.chips['blue_chip'] = str(id)
        black_btn = Button(self, text = '100', font = int(10 / 2048 * self.SW), bd = 0, command = lambda: self.game.add_bet(100))
        black_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 2 - 50, anchor = 'center')
        id = self.create_image(self.WIDTH // 8 * 6, self.HEIGHT // 2, image = self.Black_chip)
        self.chips['black_btn'] = black_btn
        self.chips['black_chip'] = str(id)

    def start(self):
        if not self.started and self.chips == {}:
            if 'pot' in self.text_id:
                try:
                    self.bet = int(self.amount.get())
                except: return
                self.game = Game(self.bet)
                self.amount.destroy()
                self.delete(self.text_id['pot'])
                del self.text_id['pot']

            self.delete(self.text_id['bet'])
            id = self.create_text(75, 50, text = self.game.bet, font = int(10 / 2048 * self.SW), fill = 'white', anchor = W)
            self.text_id['bet'] = str(id)
            self.bet_chips()

            for element in self.dealer_id:
                self.delete(self.dealer_id[element])
            self.dealer_id = {}
            for element in self.player_id:
                self.delete(self.player_id[element])
            self.player_id = {}
            for element in self.text_id:
                if element != 'bet':
                    self.delete(self.text_id[element])
            for element in self.player1_id:
                self.delete(self.player1_id[element])
            self.player1_id = {}
            for element in self.player2_id:
                self.delete(self.player2_id[element])
            self.player2_id = {}

        if not self.started and self.bet != self.game.bet:
            self.started = not self.started
            for element in self.chips:
                if element[-3:] == 'btn':
                    self.chips[element].destroy()
                else: self.delete(self.chips[element])

            self.delete(self.text_id['bet'])
            id = self.create_text(75, 50, text = self.game.bet, font = int(10 / 2048 * self.SW), fill = 'white', anchor = W)
            self.text_id['bet'] = str(id)

            dealer, player1, player2 = self.game.start()

            id = self.create_image((self.WIDTH // 21) * 8, (self.HEIGHT // 9) * 2, image = self.cards_img[dealer], anchor = 'center')
            self.dealer_id[dealer] = str(id)
            id = self.create_image((self.WIDTH // 21) * 12, (self.HEIGHT // 9) * 2, image = self.CardBack, anchor = 'center')
            self.dealer_id['cardback'] = str(id)
            id = self.create_text((self.WIDTH // 21) * 12  + 80, (self.HEIGHT // 9) * 2 + 95, text = f'({self.game.dealer_total})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
            self.text_id['dealer_count'] = str(id)

            id = self.create_image((self.WIDTH // 21) * 8, (self.HEIGHT // 9) * 5, image = self.cards_img[player1], anchor = 'center')
            self.player_id[player1] = str(id)
            id = self.create_image((self.WIDTH // 21) * 12, (self.HEIGHT // 9) * 5, image = self.cards_img[player2], anchor = 'center')
            self.player_id[player2] = str(id)
            id = self.create_text((self.WIDTH // 21) * 12  + 80, (self.HEIGHT // 9) * 5 + 95, text = f'({self.game.player_total})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
            self.text_id['player_count'] = str(id)

            del self.game.cards[:3]

    def tirer(self):
        if self.started:
            player_card = self.game.tirer()
            self.player_id[player_card] = self.cards_img[player_card]

            for m, card in enumerate(self.player_id):
                self.delete(self.player_id[card])
                id = self.create_image((self.WIDTH // (len(self.player_id) + 2)) * (m + 1.25), (self.HEIGHT // 9) * 5, image = self.cards_img[card], anchor = 'center')
                self.player_id[card] = str(id)

            self.delete(self.text_id['player_count'])
            id = self.create_text((self.WIDTH // (len(self.player_id) + 2)) * (len(self.player_id) + .25) + 80, (self.HEIGHT // 9) * 5 + 95, text = f'({self.game.player_total})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
            self.text_id['player_count'] = str(id)

            del self.game.cards[0]

            if self.game.lost(self.game.player_total): self.end(False)

    def doubler(self):
        if self.started and not self.split_happening:
            self.game.doubler(self.bet - self.game.bet)
            self.tirer()
            self.rester()
            self.delete(self.text_id['bet'])
            id = self.create_text(100, 50, text = self.game.bet, font = int(10 / 2048 * self.SW), fill = 'white', anchor = 'center')
            self.text_id['bet'] = str(id)

    def split(self):
        if self.started and self.game.player_cards[0][0][-1] == self.game.player_cards[1][0][-1] and not self.split_happening:
            self.game.doubler(self.bet - self.game.bet)
            self.delete(self.text_id['bet'])
            id = self.create_text(100, 50, text = self.game.bet, font = int(10 / 2048 * self.SW), fill = 'white', anchor = 'center')
            self.text_id['bet'] = str(id)

            self.split_happening = True
            card1, card2 = self.game.split()
            for m, card in enumerate(self.player_id):
                if m == 0:
                    self.player1_id[card] = self.player_id[card]
                if m == 1:
                    self.player2_id[card] = self.player_id[card]
                self.delete(self.player_id[card])
            self.player1_id[card1], self.player2_id[card2] = self.cards_img[card1], self.cards_img[card2]

            for m, card in enumerate(self.player1_id):
                self.delete(self.player1_id[card])
                id = self.create_image((self.WIDTH // (len(self.player1_id) + 2)) * (m + 1.25), (self.HEIGHT // 9) * 4, image = self.cards_img[card], anchor = 'center')
                self.player1_id[card] = str(id)

            for m, card in enumerate(self.player2_id):
                self.delete(self.player2_id[card])
                id = self.create_image((self.WIDTH // (len(self.player2_id) + 2)) * (m + 1.25), (self.HEIGHT // 9) * 6, image = self.cards_img[card], anchor = 'center')
                self.player2_id[card] = str(id)

            self.delete(self.text_id['player_count'])
            id = self.create_text((self.WIDTH // (len(self.player1_id) + 2)) * (len(self.player1_id) + .25) + 80, (self.HEIGHT // 9) * 4 + 95, text = f'({self.game.player_total1})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
            self.text_id['player1_count'] = str(id)
            id = self.create_text((self.WIDTH // (len(self.player2_id) + 2)) * (len(self.player2_id) + .25) + 80, (self.HEIGHT // 9) * 6 + 95, text = f'({self.game.player_total2})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
            self.text_id['player2_count'] = str(id)

            del self.game.cards[0]
            del self.game.cards[0]

            self.player1 = True
            self.player2 = False

            self.tirer_split_btn = Button(self, image = self.Tirer, bd = 0, command = self.tirer_split)
            self.tirer_split_btn.place(x = self.WIDTH // 6, y = self.HEIGHT - 50, anchor = 'center')
            self.rester_split_btn = Button(self, image = self.Rester, bd = 0, command = self.rester_split)
            self.rester_split_btn.place(x = (self.WIDTH // 6) * 3, y = self.HEIGHT - 50, anchor = 'center')

    def rester(self):
        if self.started:
            if 'cardback' in self.dealer_id:
                self.delete(self.dealer_id['cardback'])
                del self.dealer_id['cardback']
                self.parent.after(250)

            dealer_card = self.game.rester()
            self.dealer_id[dealer_card] = self.cards_img[dealer_card]

            for m, card in enumerate(self.dealer_id):
                self.delete(self.dealer_id[card])
                id = self.create_image((self.WIDTH // (len(self.dealer_id) + 2)) * (m + 1.25), (self.HEIGHT // 9) * 2, image = self.cards_img[card], anchor = 'center')
                self.dealer_id[card] = str(id)

            self.delete(self.text_id['dealer_count'])
            id = self.create_text((self.WIDTH // (len(self.dealer_id) + 2)) * (len(self.dealer_id) + .25) + 80, (self.HEIGHT // 9) * 2 + 95, text = f'({self.game.dealer_total})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
            self.text_id['dealer_count'] = str(id)

            del self.game.cards[0]

            if self.game.dealer_total < 17:
                self.parent.after(750, self.rester)
            else: self.end(self.game.check_win(self.game.player_total))

    def tirer_split(self):
        if self.player1:
            player_card, self.game.player_total1 = self.game.tirer_split(self.game.player_split1)
            self.player1_id[player_card] = self.cards_img[player_card]

            for m, card in enumerate(self.player1_id):
                self.delete(self.player1_id[card])
                id = self.create_image((self.WIDTH // (len(self.player1_id) + 2)) * (m + 1.25), (self.HEIGHT // 9) * 4, image = self.cards_img[card], anchor = 'center')
                self.player1_id[card] = str(id)

            self.delete(self.text_id['player1_count'])
            id = self.create_text((self.WIDTH // (len(self.player1_id) + 2)) * (len(self.player1_id) + .25) + 80, (self.HEIGHT // 9) * 4 + 95, text = f'({self.game.player_total1})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
            self.text_id['player1_count'] = str(id)

            del self.game.cards[0]

            if self.game.lost(self.game.player_total1):
                self.player1 = False
                self.player2 = True
                return

        if self.player2:
            player_card, self.game.player_total2= self.game.tirer_split(self.game.player_split2)
            self.player2_id[player_card]  = self.cards_img[player_card]

            for m, card in enumerate(self.player2_id):
                self.delete(self.player2_id[card])
                id = self.create_image((self.WIDTH // (len(self.player2_id) + 2)) * (m + 1.25), (self.HEIGHT // 9) * 6, image = self.cards_img[card], anchor = 'center')
                self.player2_id[card] = str(id)

            self.delete(self.text_id['player2_count'])
            id = self.create_text((self.WIDTH // (len(self.player2_id) + 2)) * (len(self.player2_id) + .25) + 80, (self.HEIGHT // 9) * 6 + 95, text = f'({self.game.player_total2})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
            self.text_id['player2_count'] = str(id)

            del self.game.cards[0]

            if self.game.lost(self.game.player_total2):
                if self.game.player_total1 > 21:
                    self.split_end1(self.game.check_win(self.game.player_total1))
                else:
                    self.rester_split()

    def rester_split(self):
        if not self.player2:
            self.player1 = False
            self.player2 = True
            return
        if 'cardback' in self.dealer_id:
            self.delete(self.dealer_id['cardback'])
            del self.dealer_id['cardback']
            self.parent.after(250)

        dealer_card = self.game.rester()
        self.dealer_id[dealer_card] = self.cards_img[dealer_card]

        for m, card in enumerate(self.dealer_id):
            self.delete(self.dealer_id[card])
            id = self.create_image((self.WIDTH // (len(self.dealer_id) + 2)) * (m + 1.25), (self.HEIGHT // 9) * 2, image = self.cards_img[card], anchor = 'center')
            self.dealer_id[card] = str(id)

        self.delete(self.text_id['dealer_count'])
        id = self.create_text((self.WIDTH // (len(self.dealer_id) + 2)) * (len(self.dealer_id) + .25) + 80, (self.HEIGHT // 9) * 2 + 95, text = f'({self.game.dealer_total})', font = int(8 / 2048 * self.SW), fill = 'white', anchor = SW)
        self.text_id['dealer_count'] = str(id)

        del self.game.cards[0]

        if self.game.dealer_total < 17:
            self.parent.after(750, self.rester_split)
        else: self.split_end1(self.game.check_win(self.game.player_total1))

    def end(self, win):
        self.started = False
        self.chips = {}
        self.game.benefit(self.bet, self.game.player_total)
        self.bet = self.game.bet
        if win == None: content = 'EGALITE'
        if win: content = 'GAGNE'
        if win == False: content = 'PERDU'
        id = self.create_text(self.WIDTH // 2, (self.HEIGHT // 9) * 3.5, text = content, font = int(20 / 2048 * self.SW), fill = 'white', anchor = 'center')
        self.text_id['end_result'] = str(id)
        self.delete(self.text_id['bet'])
        id = self.create_text(75, 50, text = self.game.bet, font = int(10 / 2048 * self.SW), fill = 'white', anchor = W)
        self.text_id['bet'] = str(id)

    def split_end1(self, win):
        self.game.benefit(self.bet, self.game.player_total1)
        if win == None: content = 'EGALITE'
        if win: content = 'GAGNE'
        if win == False: content = 'PERDU'
        id = self.create_text(self.WIDTH // 2.25, (self.HEIGHT // 9) * 8, text = content, font = int(20 / 2048 * self.SW), fill = 'white', anchor = 'center')
        self.text_id['end_result1'] = str(id)
        self.delete(self.text_id['bet'])
        id = self.create_text(75, 50, text = self.game.bet, font = int(10 / 2048 * self.SW), fill = 'white', anchor = W)
        self.text_id['bet'] = str(id)
        self.split_end2(self.game.check_win(self.game.player_total2))

    def split_end2(self, win):
        self.started = False
        self.split_happening = False
        self.chips = {}
        self.game.benefit(self.bet, self.game.player_total2)
        self.bet = self.game.bet
        if win == None: content = 'EGALITE'
        if win: content = 'GAGNE'
        if win == False: content = 'PERDU'
        id = self.create_text(self.WIDTH // 1.75, (self.HEIGHT // 9) * 8, text = content, font = int(20 / 2048 * self.SW), fill = 'white', anchor = 'center')
        self.text_id['end_result2'] = str(id)
        self.delete(self.text_id['bet'])
        id = self.create_text(75, 50, text = self.game.bet, font = int(10 / 2048 * self.SW), fill = 'white', anchor = W)
        self.text_id['bet'] = str(id)

        self.tirer_split_btn.destroy()
        self.rester_split_btn.destroy()

    def regles(self):
        content = "La partie oppose le joueur contre la banque. Le but est de battre le croupier sans dépasser 21 \n \
                   •    2 à 9 → valeur de la carte \n \
                   •    tête + le 10  → 10 points \n \
                   •    l'As → 1 ou 11 (au choix) \n \
                   La banque tire une carte tant qu’elle est strictement inferieur a 16. \n \
                   Tirer : Prendre une nouvelle carte \n \
                   Split :  Lorsque le joueur obtient deux cartes de même valeur, il lui est possible de séparer ces deux cartes afin de jouer avec deux jeux \n \
                   Doubler : Après avoir reçu deux cartes, le joueur peut choisir de doubler sa mise à la seule condition de ne recevoir qu'une carte après cela \n \
                   \n \
                   Si le joueur gagne il remporte 2x sa mise \n \
                   S’il y a égalité alors le joueur reprend sa mise \n \
                   Si le joueur perd il perd sa mise"

        window = Tk()

        Label(window, text = content).pack()

        window.mainloop()
