'''
Blackjack Game
'''

import random

class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Hand():

    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0


    def add_card(self,card):
        self.cards.append(card)
        if card.rank == 'Ace':
            if (self.values + values[card.rank] < 22):
                self.values = self.values + values[card.rank]
            else:
                self.values = self.values + 1
        else:
            self.values = self.values + values[card.rank]
        if card.rank == 'Ace':
            self.aces = self.aces + 1

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        return f'The deck contains {len(self.deck)} cards'

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Place your bet (integer value): '))
        except TypeError:
            print('Try again, not integer value')
            continue
        else:
            if chips.total < chips.bet:
                print(f'The bet can not exceed: {chips.total}')
                continue
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input('Would you like to Hit or Stand? h/s: ')

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player is standing')
            playing = False
        else:
            print('Sorry, try again')
            continue
        break

def show_some(player,dealer):
    i=0
    print('\nDealers cards')
    print('HiddenCard')
    print(dealer.cards[1])
    print('\nPlayers hand: ') 
    while i < len(player.cards):
        print(player.cards[i])
        i = i + 1

def show_all(player,dealer):
    i=0
    j=0
    print('\nDealers cards: ')
    while j < len(dealer.cards):
        print(dealer.cards[j])
        j = j + 1
    print('\nDealers value: ',dealer.values)
    print('\nPlayers hand: ')
    while i < len(player.cards):
        print(player.cards[i])
        i = i + 1
    print('\nPlayers value: ',player.values)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    print('Welcome to Daniels BlackJack')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    chips = Chips()

    take_bet(chips)

    show_some(player_hand,dealer_hand)

    playing = True

    while playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.values > 21:
            player_busts(player_hand,dealer_hand,chips)
            break

    if player_hand.values <= 21:

        while dealer_hand.values < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.values > 21:
            dealer_busts(player_hand,dealer_hand,chips)

        elif dealer_hand.values > player_hand.values:
            dealer_wins(player_hand,dealer_hand,chips)

        elif dealer_hand.values < player_hand.values:
            player_wins(player_hand,dealer_hand,chips)

        else:
            push(player_hand,dealer_hand)

    print("\nPlayer's winnings stand at",chips.total)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break



