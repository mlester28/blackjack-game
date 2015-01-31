#game of blackjack, Miriam Lester, Jan 29 2015
import random
import sys


def make_deck(lst):
    suits = ["hearts", "spades", "clubs", "diamonds"]
    numbers = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    for i in numbers:
        for s in suits:
            lst.append((i,s))
    return lst


class Player:
    hand = []
    name = input("What is your name?")

    def hit(self,card):
        return self.hand.append(card)

    def sum_hand(self):
        sum = 0
        for card,suit in self.hand:
            if card == "A":
                sum += int(input("1 or 11?"))
            elif isinstance(card,int):
                sum += card
                #print("added {}".format(card))
            else:
                sum += 10
                #print("added 10")
        return sum

    def __str__(self):
        return "{}'s turn".format(self.name)


class Dealer(Player):
    name = "Dealer"
    hand = []

    #dealer's sum_hand doesn't ask for input if its an A
    def sum_hand(self):
        sum = 0
        numberA = 0
        for card,suit in self.hand:
            if card == "A":
                sum += 1
                numberA +=1
            elif isinstance(card,int):
                sum += card
                #print("added {}".format(card))
            else:
                sum += 10
                #print("added 10")

        #if A in hand and sum < 11, add 10
        if numberA > 0 and sum < 11:
            sum += 10
        return sum


class Game:
    def setup(self,deck1):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = deck1
        print("========================================================")

    def dealer_turn(self):
        self.dealer.hit(self.deck.pop(0))
        print(self.dealer.hand[0], end = '')
        self.dealer.hit(self.deck.pop(0))
        print(" X ", end = '')
        while self.dealer.sum_hand()<17:
            self.dealer.hit(self.deck.pop(0))
            print("X ", end = '')

        print("\n\n========================================================")

    def player_turn(self):
        self.player.hit(self.deck.pop(0))
        self.player.hit(self.deck.pop(0))
        while True:
            print("Your hand is...")
            print(self.player.hand)
            move = input("Would you like to [h]it or [s]tay?")
            if move.lower() == 's':
                break
            elif self.player.sum_hand() >21:
                break
            else:
                self.player.hit(self.deck.pop(0))
        print("\n========================================================")

    def gameover(self):
        print("The dealer's hand was: {}".format(self.dealer.sum_hand()))
        print(self.dealer.hand)
        print("\nYour hand was: {}".format(self.player.sum_hand()))
        print(self.player.hand)

    def cleanup(self):
        if self.dealer.sum_hand() > 21:
            print("Dealer busts!")
            self.gameover()
        elif self.player.sum_hand() > 21:
            print("You busted!")
            self.gameover()
        else:
            self.gameover()
            if self.player.sum_hand() < self.dealer.sum_hand():
                print("\n\n\nYou Lose! \n\n")
            else:
                print("\n\n\nYou Win! \n\n")

    def __init__(self):
        deck1 = make_deck([])
        random.shuffle(deck1)
        self.setup(deck1)

        print(self.dealer)
        self.dealer_turn()
        print(self.player)
        self.player_turn()
        self.cleanup()
        sys.exit()



Game()

